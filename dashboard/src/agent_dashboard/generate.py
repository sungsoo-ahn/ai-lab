from __future__ import annotations

import argparse
import html
import http.server
import os
import re
import shutil
import socketserver
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
DASHBOARD_ROOT = REPO_ROOT / "dashboard"
DIST_ROOT = DASHBOARD_ROOT / "dist"
ACTIVE_ROOT = REPO_ROOT / "research" / "active"

SECTION_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TOKEN_RE = re.compile(
    r"(?i)\b("
    r"xox[baprs]-[A-Za-z0-9.-]+|"
    r"xapp-[A-Za-z0-9.-]+|"
    r"sk-[A-Za-z0-9_-]{20,}|"
    r"gh[pousr]_[A-Za-z0-9_]{20,}|"
    r"[A-Za-z0-9_]*(?:token|secret|password|api[_-]?key)[A-Za-z0-9_]*\s*[:=]\s*[^`\s]+"
    r")"
)


@dataclass
class Report:
    kind: str
    title: str
    status: str
    date: str
    path: Path
    source_rel: str
    markdown: str
    sections: dict[str, str]
    metadata: dict[str, Any]
    project_id: str | None = None
    hypothesis_id: str | None = None


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def repo_rel(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def redact(text: str) -> str:
    text = text.replace(str(REPO_ROOT), "<repo>")
    text = text.replace(str(REPO_ROOT.parent), "<home>")
    return TOKEN_RE.sub("[REDACTED]", text)


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "section"


def parse_sections(markdown: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = "_preamble"
    for line in markdown.splitlines():
        match = SECTION_RE.match(line)
        if match:
            current = match.group(2).strip()
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def first_match(sections: dict[str, str], names: list[str]) -> str:
    lowered = {key.lower(): value for key, value in sections.items()}
    for name in names:
        if name.lower() in lowered and lowered[name.lower()].strip():
            return lowered[name.lower()].strip()
    return ""


def first_paragraph(markdown: str) -> str:
    lines: list[str] = []
    in_code = False
    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.startswith("#") or line.startswith("|"):
            continue
        if re.match(r"^(Date|Status):\s+", line):
            continue
        if not line.strip():
            if lines:
                break
            continue
        if line.strip().startswith(("-", "*")):
            continue
        lines.append(line.strip())
    return " ".join(lines)


def parse_simple_yaml(path: Path) -> dict[str, Any]:
    text = read_text(path)
    data: dict[str, Any] = {}
    current_key: str | None = None
    current_list: list[Any] | None = None
    current_item: dict[str, Any] | None = None

    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        if indent == 0 and ":" in line and not line.startswith("- "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            current_item = None
            if value:
                data[key] = yaml_scalar(value)
                current_list = None
            else:
                data[key] = []
                current_list = data[key]
            continue
        if line.startswith("- ") and current_key:
            value = line[2:].strip()
            if ":" in value:
                key, item_value = value.split(":", 1)
                current_item = {key.strip(): yaml_scalar(item_value.strip())}
                assert isinstance(current_list, list)
                current_list.append(current_item)
            else:
                assert isinstance(current_list, list)
                current_list.append(yaml_scalar(value))
                current_item = None
            continue
        if current_item is not None and ":" in line:
            key, value = line.split(":", 1)
            current_item[key.strip()] = yaml_scalar(value.strip())
    return data


def yaml_scalar(value: str) -> Any:
    if value in {"null", "~"}:
        return None
    if value in {"true", "false"}:
        return value == "true"
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def markdown_to_html(markdown: str) -> str:
    markdown = redact(markdown)
    out: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    in_code = False
    code_lines: list[str] = []
    table_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline_md(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            out.append("<ul>" + "".join(f"<li>{inline_md(item)}</li>" for item in list_items) + "</ul>")
            list_items = []

    def flush_table() -> None:
        nonlocal table_lines
        if not table_lines:
            return
        rows = [split_table_row(row) for row in table_lines if row.strip()]
        if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in rows[1]):
            head, body = rows[0], rows[2:]
            html_rows = [
                "<thead><tr>"
                + "".join(f"<th>{inline_md(cell.strip())}</th>" for cell in head)
                + "</tr></thead>"
            ]
            html_rows.append(
                "<tbody>"
                + "".join(
                    "<tr>" + "".join(f"<td>{inline_md(cell.strip())}</td>" for cell in row) + "</tr>"
                    for row in body
                )
                + "</tbody>"
            )
            out.append("<div class=\"table-wrap\"><table>" + "".join(html_rows) + "</table></div>")
        else:
            out.append("<pre><code>" + html.escape("\n".join(table_lines)) + "</code></pre>")
        table_lines = []

    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            flush_list()
            flush_table()
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            flush_list()
            table_lines.append(line)
            continue
        flush_table()
        match = SECTION_RE.match(line)
        if match:
            flush_paragraph()
            flush_list()
            level = min(len(match.group(1)) + 1, 6)
            text = match.group(2).strip()
            out.append(f"<h{level} id=\"{slugify(text)}\">{inline_md(text)}</h{level}>")
        elif stripped.startswith(("- ", "* ")):
            flush_paragraph()
            list_items.append(stripped[2:].strip())
        elif not stripped:
            flush_paragraph()
            flush_list()
        else:
            flush_list()
            paragraph.append(stripped)
    flush_paragraph()
    flush_list()
    flush_table()
    return "\n".join(out)


def split_table_row(row: str) -> list[str]:
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return [cell.strip() for cell in row.split("|")]


def inline_md(text: str) -> str:
    text = redact(text)
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: link_html(m.group(1), m.group(2)), text)
    return text


def link_html(label: str, href: str) -> str:
    safe_href = html.escape(redact(href), quote=True)
    return f'<a href="{safe_href}">{html.escape(label)}</a>'


def load_report(path: Path, kind: str, metadata: dict[str, Any], project_id: str | None = None, hypothesis_id: str | None = None) -> Report:
    markdown = read_text(path)
    sections = parse_sections(markdown)
    title = markdown.splitlines()[0].lstrip("# ").strip() if markdown.splitlines() else path.stem
    inferred_status = "proposal" if path.name == "proposal.md" else "unknown"
    status = str(extract_field(markdown, "Status") or metadata.get("status") or inferred_status)
    date = str(extract_field(markdown, "Date") or metadata.get("updated_at") or metadata.get("created_at") or "")
    return Report(
        kind=kind,
        title=title,
        status=status,
        date=date,
        path=path,
        source_rel=repo_rel(path),
        markdown=markdown,
        sections=sections,
        metadata=metadata,
        project_id=project_id,
        hypothesis_id=hypothesis_id,
    )


def extract_field(markdown: str, field: str) -> str:
    prefix = f"{field}:"
    for line in markdown.splitlines()[:12]:
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return ""


def summary_for(report: Report) -> str:
    summary = first_match(
        report.sections,
        [
            "Goal",
            "Plain-English Summary",
            "Summary",
            "Current Result",
            "Result",
            "Purpose",
            "Answer",
        ],
    )
    return summary or first_paragraph(report.markdown) or "No summary available yet."


def recommendation_for(report: Report) -> str:
    return first_match(report.sections, ["Recommendation", "Next Step", "Open Questions"])


def project_takeaway(project: dict[str, Any]) -> str:
    project_id = str(project["id"])
    if project_id == "btc":
        return (
            "BTC research is still pre-holdout. The strongest candidate is interesting, "
            "but its returns are too concentrated; the next work should test robustness, not promotion."
        )
    if project_id == "slack-agent-bridge":
        return (
            "The Slack bridge is a local control surface for the account agent. The important design constraint "
            "is privacy: useful responses without storing message bodies or tokens."
        )
    return excerpt(summary_for(project["report"]), 260)


def project_next_step(project: dict[str, Any]) -> str:
    project_id = str(project["id"])
    if project_id == "btc":
        return "Run a narrow t094 robustness pass before any sealed holdout decision."
    if project_id == "slack-agent-bridge":
        return "Keep the bridge operational but conservative: minimal logs, explicit approvals for external writes."
    return excerpt(recommendation_for(project["report"]) or "Review the source report for the next action.", 220)


def source_report(markdown: str, title: str = "Source report") -> str:
    return f"""
    <section class="section">
      <details class="source-details">
        <summary>{html.escape(title)}</summary>
        <div class="article">
          {markdown_to_html(markdown)}
        </div>
      </details>
    </section>
    """


def load_projects() -> list[dict[str, Any]]:
    projects: list[dict[str, Any]] = []
    if not ACTIVE_ROOT.exists():
        return projects
    for project_dir in sorted(path for path in ACTIVE_ROOT.iterdir() if path.is_dir()):
        report_path = first_existing(project_dir / "report.md", project_dir / "proposal.md")
        project_yaml_path = project_dir / "project.yaml"
        if report_path is None and not project_yaml_path.exists():
            continue
        project_yaml = parse_simple_yaml(project_yaml_path)
        project_id = str(project_yaml.get("project_id") or project_dir.name)
        report = load_report(report_path or project_dir / "report.md", "project", project_yaml, project_id=project_id)
        hypotheses = []
        hypotheses_dir = project_dir / "hypotheses"
        if hypotheses_dir.exists():
            for hyp_dir in sorted(path for path in hypotheses_dir.iterdir() if path.is_dir()):
                hyp_yaml = parse_simple_yaml(hyp_dir / "hypothesis.yaml")
                hyp_id = str(hyp_yaml.get("hypothesis_id") or hyp_dir.name)
                hyp_report = load_report(
                    hyp_dir / "report.md",
                    "hypothesis",
                    hyp_yaml,
                    project_id=project_id,
                    hypothesis_id=hyp_id,
                )
                hypotheses.append({"id": hyp_id, "metadata": hyp_yaml, "report": hyp_report})
        assets = parse_simple_yaml(project_dir / "assets.yaml").get("assets", [])
        projects.append(
            {
                "id": project_id,
                "dir": project_dir,
                "metadata": project_yaml,
                "report": report,
                "hypotheses": hypotheses,
                "assets": assets if isinstance(assets, list) else [],
            }
        )
    return projects


def first_existing(*paths: Path) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


def page(title: str, body: str, current: str = "") -> str:
    nav = f"""
    <header class="site-header">
      <a class="brand" href="{current}index.html">
        <span class="brand-mark">A</span>
        <span><strong>Agent System</strong><small>Research dashboard</small></span>
      </a>
      <nav>
        <a href="{current}index.html">System</a>
        <a href="{current}index.html#projects">Projects</a>
        <a href="{current}index.html#activity">Activity</a>
      </nav>
    </header>
    """
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} - Agent System</title>
  <link rel="stylesheet" href="{current}assets/styles.css">
</head>
<body>
  {nav}
  <main>{body}</main>
</body>
</html>
"""


def badge(text: str) -> str:
    value = html.escape(str(text))
    cls = slugify(str(text))
    return f'<span class="badge badge-{cls}">{value}</span>'


def card(title: str, body: str, href: str | None = None) -> str:
    heading = f'<h3>{"<a href=\"" + html.escape(href) + "\">" if href else ""}{html.escape(title)}{"</a>" if href else ""}</h3>'
    return f'<article class="card">{heading}{body}</article>'


def build_home(projects: list[dict[str, Any]]) -> str:
    status = load_report(REPO_ROOT / "reports" / "system-status.md", "system", {})
    activity = read_text(REPO_ROOT / "logs" / "activity.md")
    recent_rows = parse_activity(activity)[-6:][::-1]
    total_hypotheses = sum(len(project["hypotheses"]) for project in projects)
    completed_hypotheses = sum(
        1
        for project in projects
        for hyp in project["hypotheses"]
        if str(hyp["report"].status).lower() == "complete"
    )
    latest_date = recent_rows[0]["date"] if recent_rows else "n/a"
    project_cards = []
    takeaway_cards = []
    for project in projects:
        report: Report = project["report"]
        href = f"projects/{project['id']}/index.html"
        body = f"""
        <p>{inline_md(project_takeaway(project))}</p>
        <div class="meta-row">{badge(report.status)}<span>{len(project['hypotheses'])} hypotheses</span></div>
        """
        project_cards.append(card(str(project["metadata"].get("title") or project["id"]), body, href))
        takeaway_cards.append(
            f"""
            <article class="takeaway">
              <span>{html.escape(str(project["metadata"].get("title") or project["id"]))}</span>
              <h3>{inline_md(project_takeaway(project))}</h3>
              <p>{inline_md(project_next_step(project))}</p>
              <a href="{html.escape(href)}">Open project</a>
            </article>
            """
        )

    recent_html = "".join(
        f"<li><time>{html.escape(row['date'])}</time><span>{inline_md(row['activity'])}</span><small>{inline_md(row['notes'])}</small></li>"
        for row in recent_rows
    )
    body = f"""
    <section class="hero">
      <div>
        <p class="eyebrow">Research operations</p>
        <h1>A readable trail of current agent work.</h1>
        <p class="lede">A public status page for active research: what changed, what matters, and where the evidence lives.</p>
      </div>
      <div class="hero-panel">
        <span class="label">Latest state</span>
        <strong>{completed_hypotheses}/{total_hypotheses or 0} work units complete</strong>
        <p>Generated from the repo's Markdown and YAML reports, with source material kept one click away.</p>
      </div>
    </section>
    <section class="metric-strip">
      <div><span>Projects</span><strong>{len(projects)}</strong></div>
      <div><span>Work units</span><strong>{total_hypotheses}</strong></div>
      <div><span>Latest log</span><strong>{html.escape(latest_date)}</strong></div>
      <div><span>Publication</span><strong>Public-safe</strong></div>
    </section>
    <section class="section">
      <div class="section-head"><p class="eyebrow">What matters now</p><h2>Current read</h2></div>
      <div class="takeaway-grid">{''.join(takeaway_cards)}</div>
    </section>
    <section id="projects" class="section">
      <div class="section-head"><p class="eyebrow">Research</p><h2>Active projects</h2></div>
      <div class="grid">{''.join(project_cards) or '<p>No active projects found.</p>'}</div>
    </section>
    <section id="activity" class="section split">
      <div>
        <p class="eyebrow">Recent changes</p>
        <h2>Activity log</h2>
      </div>
      <ol class="timeline">{recent_html}</ol>
    </section>
    {source_report(status.markdown, "Read system source report")}
    """
    return page("Dashboard", body)


def build_project(project: dict[str, Any]) -> str:
    report: Report = project["report"]
    hypotheses = project["hypotheses"]
    hypothesis_cards = []
    for hyp in hypotheses:
        hyp_report: Report = hyp["report"]
        href = f"hypotheses/{hyp['id']}/index.html"
        recommendation = recommendation_for(hyp_report)
        recommendation_html = (
            f"<p><span class=\"label-inline\">Next</span> {inline_md(excerpt(recommendation, 260))}</p>"
            if recommendation
            else ""
        )
        hypothesis_cards.append(
            f"""
            <article class="summary-card">
              <div class="summary-card-head">
                <h3><a href="{html.escape(href)}">{html.escape(hyp['id'])}</a></h3>
                {badge(hyp_report.status)}
              </div>
              <p>{inline_md(excerpt(summary_for(hyp_report), 360))}</p>
              {recommendation_html}
            </article>
            """
        )
    assets = project.get("assets", [])
    asset_rows = []
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        asset_rows.append(
            "<tr>"
            f"<td>{html.escape(str(asset.get('id', '')))}</td>"
            f"<td>{html.escape(str(asset.get('type', '')))}</td>"
            f"<td>{inline_md(excerpt(str(asset.get('description') or asset.get('role') or ''), 160))}</td>"
            "</tr>"
        )
    body = f"""
    <section class="page-title">
      <p class="eyebrow">Project</p>
      <h1>{html.escape(str(project['metadata'].get('title') or project['id']))}</h1>
      <div class="meta-row">{badge(report.status)}<span>{html.escape(report.date)}</span><span>{html.escape(report.source_rel)}</span></div>
      <p class="lede">{inline_md(project_takeaway(project))}</p>
    </section>
    <section class="metric-strip">
      <div><span>Hypotheses</span><strong>{len(hypotheses)}</strong></div>
      <div><span>Assets</span><strong>{len(asset_rows)}</strong></div>
      <div><span>Evidence</span><strong>Reports</strong></div>
      <div><span>State</span><strong>{html.escape(report.status)}</strong></div>
    </section>
    <section class="section">
      <div class="section-head"><p class="eyebrow">Work units</p><h2>Hypotheses</h2></div>
      <div class="summary-grid">{''.join(hypothesis_cards) or '<p>No hypotheses found.</p>'}</div>
    </section>
    <section class="section">
      <div class="section-head"><p class="eyebrow">Materials</p><h2>Assets</h2></div>
      <div class="table-wrap"><table><thead><tr><th>Asset</th><th>Type</th><th>Description</th></tr></thead><tbody>{''.join(asset_rows)}</tbody></table></div>
    </section>
    {source_report(report.markdown, "Read full project report")}
    """
    return page(str(project["id"]), body, current="../../")


def build_hypothesis(project: dict[str, Any], hyp: dict[str, Any]) -> str:
    report: Report = hyp["report"]
    project_id = project["id"]
    body = f"""
    <section class="page-title">
      <p class="eyebrow">Hypothesis / work unit</p>
      <h1>{html.escape(hyp['id'])}</h1>
      <div class="meta-row">{badge(report.status)}<span>{html.escape(report.date)}</span><span>{html.escape(report.source_rel)}</span></div>
      <p class="lede">{inline_md(excerpt(summary_for(report), 420))}</p>
    </section>
    <section class="metric-strip">
      <div><span>Project</span><strong>{html.escape(project_id)}</strong></div>
      <div><span>Status</span><strong>{html.escape(report.status)}</strong></div>
      <div><span>Decision</span><strong>{html.escape(excerpt(first_match(report.sections, ['Decision']) or 'Recorded in report', 42))}</strong></div>
      <div><span>Source</span><strong>report.md</strong></div>
    </section>
    {source_report(report.markdown, "Read full work-unit report")}
    """
    return page(f"{project_id} / {hyp['id']}", body, current="../../../../")


def parse_activity(markdown: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in markdown.splitlines():
        if not line.startswith("|") or "---" in line or "Date" in line:
            continue
        cells = split_table_row(line)
        if len(cells) >= 3:
            rows.append({"date": cells[0], "activity": cells[1], "notes": cells[2]})
    return rows


def excerpt(text: str, limit: int) -> str:
    compact = re.sub(r"\s+", " ", redact(text)).strip()
    compact = re.sub(r"^[-*]\s+", "", compact)
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1].rstrip() + "..."


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build() -> None:
    if DIST_ROOT.exists():
        shutil.rmtree(DIST_ROOT)
    (DIST_ROOT / "assets").mkdir(parents=True)
    projects = load_projects()
    write_file(DIST_ROOT / "assets" / "styles.css", CSS)
    write_file(DIST_ROOT / "index.html", build_home(projects))
    for project in projects:
        project_dir = DIST_ROOT / "projects" / project["id"]
        write_file(project_dir / "index.html", build_project(project))
        for hyp in project["hypotheses"]:
            write_file(project_dir / "hypotheses" / hyp["id"] / "index.html", build_hypothesis(project, hyp))
    write_file(DIST_ROOT / "robots.txt", "User-agent: *\nDisallow:\n")


def serve(port: int) -> None:
    os.chdir(DIST_ROOT)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Serving dashboard at http://127.0.0.1:{port}/")
        httpd.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the agent-system dashboard.")
    parser.add_argument("--serve", action="store_true", help="Build and serve the dashboard locally.")
    parser.add_argument("--port", type=int, default=8008, help="Local preview port.")
    args = parser.parse_args()
    build()
    print(f"Built dashboard at {DIST_ROOT}")
    if args.serve:
        serve(args.port)


CSS = r"""
:root {
  --bg: #f4f5f4;
  --surface: #ffffff;
  --surface-soft: #ebf8f0;
  --ink: #181d18;
  --muted: #5a7763;
  --line: #dce7df;
  --green: #14793b;
  --green-strong: #0c5c30;
  --green-bright: #24b256;
  --orange: #9e5f24;
  --red: #bc4629;
  --blue: #155dfc;
  --shadow: 0 18px 48px rgba(24, 29, 24, 0.08);
}

* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.55;
}
a { color: var(--green-strong); text-decoration: none; }
a:hover { text-decoration: underline; }
main { width: min(1180px, calc(100% - 40px)); margin: 0 auto 72px; }
.site-header {
  width: min(1180px, calc(100% - 40px));
  margin: 18px auto 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 12px 0 28px;
}
.brand { display: flex; align-items: center; gap: 12px; color: var(--ink); }
.brand:hover { text-decoration: none; }
.brand-mark {
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: var(--ink);
  color: #fff;
  font-weight: 750;
}
.brand small { display: block; color: var(--muted); font-size: 12px; margin-top: 1px; }
nav { display: flex; gap: 18px; font-size: 14px; }
.hero {
  min-height: 410px;
  display: grid;
  grid-template-columns: minmax(0, 1.4fr) minmax(280px, 0.6fr);
  gap: 28px;
  align-items: end;
  padding: 74px 0 44px;
}
.eyebrow {
  margin: 0 0 12px;
  color: var(--green);
  font-size: 12px;
  font-weight: 720;
  letter-spacing: 0;
  text-transform: uppercase;
}
h1, h2, h3 { line-height: 1.05; letter-spacing: 0; }
h1 { margin: 0; font-size: clamp(46px, 8vw, 92px); max-width: 930px; }
h2 { margin: 0; font-size: 34px; }
h3 { margin: 0 0 12px; font-size: 20px; }
.lede {
  max-width: 780px;
  color: #334337;
  font-size: 20px;
  margin: 22px 0 0;
}
.hero-panel, .card, .article, .metric-strip, .table-wrap {
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.76);
  box-shadow: var(--shadow);
}
.hero-panel {
  padding: 24px;
  border-radius: 8px;
}
.hero-panel .label {
  display: block;
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 10px;
}
.hero-panel strong { display: block; font-size: 30px; line-height: 1.1; }
.hero-panel p { color: var(--muted); margin-bottom: 0; }
.metric-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 58px;
}
.metric-strip div { padding: 20px; border-right: 1px solid var(--line); }
.metric-strip div:last-child { border-right: 0; }
.metric-strip span { display: block; color: var(--muted); font-size: 13px; }
.metric-strip strong { display: block; margin-top: 4px; font-size: 22px; }
.section { margin-top: 58px; }
.section-head { display: flex; justify-content: space-between; align-items: end; margin-bottom: 18px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; }
.card {
  border-radius: 8px;
  padding: 22px;
}
.card p { color: #34483a; margin: 0 0 18px; }
.takeaway-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 18px;
}
.takeaway {
  position: relative;
  min-height: 260px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 20px;
  border: 1px solid #cfe2d5;
  border-radius: 8px;
  background: linear-gradient(180deg, #ffffff 0%, #ebf8f0 100%);
  padding: 24px;
  box-shadow: var(--shadow);
}
.takeaway span {
  color: var(--green);
  font-size: 12px;
  font-weight: 720;
  text-transform: uppercase;
}
.takeaway h3 {
  max-width: 820px;
  margin: 0;
  font-size: 26px;
  line-height: 1.12;
}
.takeaway p {
  margin: 0;
  color: var(--muted);
}
.takeaway a {
  width: fit-content;
  font-weight: 720;
}
.summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 16px;
}
.summary-card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255,255,255,0.82);
  padding: 20px;
}
.summary-card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 14px;
}
.summary-card h3 {
  overflow-wrap: anywhere;
  margin-bottom: 0;
}
.summary-card p {
  color: #34483a;
  margin: 0 0 12px;
}
.summary-card p:last-child { margin-bottom: 0; }
.label-inline {
  color: var(--green);
  font-size: 12px;
  font-weight: 720;
  text-transform: uppercase;
}
.meta-row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; color: var(--muted); font-size: 13px; }
.badge {
  display: inline-flex;
  align-items: center;
  min-height: 26px;
  border-radius: 999px;
  padding: 3px 10px;
  background: var(--surface-soft);
  color: var(--green-strong);
  border: 1px solid #cfe2d5;
  font-size: 12px;
  font-weight: 720;
}
.badge-complete, .badge-active { color: var(--green-strong); }
.badge-needs-refinement, .badge-pending { color: var(--orange); background: #fef5ed; border-color: #f7dcc5; }
.badge-reject, .badge-blocked { color: var(--red); background: #fff0ed; border-color: #f1ccc4; }
.split {
  display: grid;
  grid-template-columns: 0.45fr 1fr;
  gap: 30px;
  align-items: start;
}
.timeline {
  list-style: none;
  margin: 0;
  padding: 0;
  border-top: 1px solid var(--line);
}
.timeline li {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 16px;
  padding: 16px 0;
  border-bottom: 1px solid var(--line);
}
.timeline time { color: var(--green); font-weight: 700; }
.timeline small { grid-column: 2; color: var(--muted); }
.page-title { padding: 56px 0 30px; }
.page-title h1 { font-size: clamp(40px, 7vw, 78px); }
.article {
  border-radius: 8px;
  padding: min(5vw, 52px);
  background: var(--surface);
}
.source-details {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255,255,255,0.72);
  box-shadow: var(--shadow);
  overflow: hidden;
}
.source-details summary {
  cursor: pointer;
  list-style: none;
  padding: 18px 22px;
  color: var(--green-strong);
  font-weight: 720;
}
.source-details summary::-webkit-details-marker { display: none; }
.source-details summary::after {
  content: "+";
  float: right;
  color: var(--muted);
}
.source-details[open] summary::after { content: "-"; }
.source-details .article {
  border: 0;
  border-top: 1px solid var(--line);
  border-radius: 0;
  box-shadow: none;
}
.article h2 { margin-top: 38px; font-size: 28px; }
.article h3 { margin-top: 28px; }
.article p, .article li { color: #29372d; }
.article code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.92em;
  background: #f0f3f1;
  border: 1px solid var(--line);
  border-radius: 5px;
  padding: 1px 5px;
}
pre {
  overflow: auto;
  border-radius: 8px;
  background: #191d1c;
  color: #d4d4d4;
  padding: 18px;
}
pre code {
  background: transparent !important;
  border: 0 !important;
  color: inherit;
  padding: 0 !important;
}
.table-wrap {
  width: 100%;
  overflow-x: auto;
  border-radius: 8px;
  box-shadow: none;
}
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th, td { text-align: left; vertical-align: top; padding: 13px 14px; border-bottom: 1px solid var(--line); }
th { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0; background: #f8faf8; }
td { color: #29372d; }
tr:last-child td { border-bottom: 0; }

@media (max-width: 820px) {
  main, .site-header { width: min(100% - 28px, 1180px); }
  .site-header { align-items: flex-start; flex-direction: column; }
  nav { width: 100%; justify-content: space-between; }
  .hero { grid-template-columns: 1fr; min-height: unset; padding-top: 44px; }
  .metric-strip { grid-template-columns: 1fr 1fr; }
  .metric-strip div:nth-child(2) { border-right: 0; }
  .metric-strip div { border-bottom: 1px solid var(--line); }
  .split { grid-template-columns: 1fr; }
  .timeline li { grid-template-columns: 1fr; gap: 4px; }
  .timeline small { grid-column: 1; }
}

@media (max-width: 520px) {
  h1 { font-size: 42px; }
  .lede { font-size: 17px; }
  .metric-strip { grid-template-columns: 1fr; }
  .metric-strip div { border-right: 0; }
  .article { padding: 24px 18px; }
}
"""


if __name__ == "__main__":
    main()
