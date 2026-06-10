from __future__ import annotations

import importlib.machinery
import importlib.util
import subprocess
from types import SimpleNamespace
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_cli():
    loader = importlib.machinery.SourceFileLoader("ai_lab_cli", str(ROOT / "bin" / "ai-lab"))
    spec = importlib.util.spec_from_loader("ai_lab_cli", loader)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def valid_spec() -> dict[str, object]:
    return {
        "schema_version": "ai_lab_cell_run_v1",
        "cell_id": "demo__autoresearch__v1",
        "task_id": "demo",
        "scheme_id": "autoresearch",
        "profile_id": "demo_fixed_loop",
        "loop": {
            "mode": "continuous",
            "sleep_seconds": 0,
            "max_cycles": 1,
            "max_wall_minutes": 10,
            "stop_file": "STOP",
            "stop_on_no_artifact_change": False,
        },
        "source_gates": [
            {
                "source_id": "demo_source",
                "head_policy": "require_registered_ref",
                "tracked_clean": True,
                "allow_untracked": ["results/"],
            }
        ],
        "commands": {
            "preflight": [{"id": "status", "builtin": "source_status", "args": ["demo_source"]}],
            "cycle": [
                {
                    "id": "echo",
                    "cwd": "{root}",
                    "argv": ["python", "-c", "print('{run_id}', '{cycle}', '{cell_id}', '{scheme_id}')"],
                    "timeout_seconds": 30,
                    "artifacts": ["results/**"],
                }
            ],
            "synthesis": [{"id": "synthesis", "builtin": "synthesize", "timeout_seconds": 30}],
        },
    }


def cell_spec_path(tmp_path: Path) -> Path:
    path = tmp_path / "evaluations" / "active" / "demo__autoresearch__v1" / "run-spec.yaml"
    path.parent.mkdir(parents=True)
    (path.parent / "evaluation-cell.yaml").write_text(
        """cell_id: demo__autoresearch__v1
task_id: demo
scheme_id: autoresearch
status: active
""",
        encoding="utf-8",
    )
    return path


def test_run_spec_validation_accepts_valid_cell_shape(tmp_path: Path) -> None:
    cli = load_cli()
    assert cli.validate_run_spec(valid_spec(), path=cell_spec_path(tmp_path)) == []


def test_run_spec_validation_rejects_old_scientist_shape(tmp_path: Path) -> None:
    cli = load_cli()
    spec = {
        "schema_version": "ai_lab_scientist_run_v1",
        "task_id": "demo",
        "scientist_id": "demo_scientist",
        "profile_id": "demo_fixed_loop",
        "loop": {"mode": "continuous"},
        "source_gates": [],
        "commands": {"preflight": [], "cycle": [], "synthesis": []},
    }
    issues = cli.validate_run_spec(spec, path=cell_spec_path(tmp_path))
    assert any("ai_lab_cell_run_v1" in issue for issue in issues)
    assert any("scientist_id is obsolete" in issue for issue in issues)
    assert any("cell_id must be a non-empty string" in issue for issue in issues)


def test_run_spec_validation_rejects_ambiguous_command_and_unknown_placeholder(tmp_path: Path) -> None:
    cli = load_cli()
    spec = valid_spec()
    commands = spec["commands"]
    assert isinstance(commands, dict)
    commands["cycle"] = [
        {
            "id": "bad",
            "argv": ["echo", "{unsupported}"],
            "builtin": "source_status",
        }
    ]
    issues = cli.validate_run_spec(spec, path=cell_spec_path(tmp_path))
    assert any("exactly one of argv, script, or builtin" in issue for issue in issues)
    assert any("{unsupported}" in issue for issue in issues)


def test_active_cell_ids_discovers_active_cells(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    root = tmp_path / "evaluations" / "active"
    active = root / "demo__autoresearch__v1"
    inactive = root / "demo__autoscientist__v1"
    active.mkdir(parents=True)
    inactive.mkdir()
    (active / "evaluation-cell.yaml").write_text("status: active\n", encoding="utf-8")
    (inactive / "evaluation-cell.yaml").write_text("status: inactive\n", encoding="utf-8")
    monkeypatch.setattr(cli, "EVALUATIONS", root)
    assert cli.active_cell_ids() == ["demo__autoresearch__v1"]


def test_source_gate_rejects_disallowed_untracked_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, stdout=subprocess.PIPE)
    (repo / "tracked.txt").write_text("ok\n", encoding="utf-8")
    subprocess.run(["git", "add", "tracked.txt"], cwd=repo, check=True)
    subprocess.run(
        ["git", "-c", "user.email=test@example.com", "-c", "user.name=Test", "commit", "-m", "init"],
        cwd=repo,
        check=True,
        stdout=subprocess.PIPE,
    )
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True, text=True, stdout=subprocess.PIPE).stdout.strip()
    registry = tmp_path / "sources.yaml"
    registry.write_text(
        f"""sources:
  - source_id: demo_source
    remote_url: file://{repo}
    git_ref: {head}
    materialized_path: {repo}
""",
        encoding="utf-8",
    )
    monkeypatch.setattr(cli, "SOURCE_REGISTRY", registry)

    cli.check_source_gate(
        {
            "source_id": "demo_source",
            "head_policy": "require_registered_ref",
            "tracked_clean": True,
            "allow_untracked": ["results/"],
        },
        strict=True,
    )
    (repo / "scratch.txt").write_text("not allowed\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        cli.check_source_gate(
            {
                "source_id": "demo_source",
                "head_policy": "require_registered_ref",
                "tracked_clean": True,
                "allow_untracked": ["results/"],
            },
            strict=True,
        )


def test_run_command_respects_elapsed_wall_deadline(tmp_path: Path) -> None:
    cli = load_cli()
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    context = {
        "cell_id": "demo__autoresearch__v1",
        "task_id": "demo",
        "scheme_id": "autoresearch",
        "run_id": "deadline-test",
        "cycle": "1",
        "run_dir": str(run_dir),
        "cell_dir": str(tmp_path),
        "root": str(ROOT),
    }
    code = cli.run_command(
        {"id": "late", "argv": ["python", "-c", "print('should not run')"]},
        group="cycle",
        context=context,
        run_dir=run_dir,
        dry_run=False,
        deadline_epoch=0,
    )
    assert code == 124
    assert "command_skipped" in (run_dir / "events.jsonl").read_text(encoding="utf-8")


def test_codex_lab_wrapper_uses_exec_for_noninteractive_synthesis() -> None:
    text = (ROOT / "bin" / "codex-lab").read_text(encoding="utf-8")
    assert "codex --cd \"$HOME\" --ask-for-approval never" in text
    assert "codex exec -c approval_policy='never'" in text


def test_runtime_check_skips_brew_for_python_only_profile(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    monkeypatch.setattr(
        cli,
        "RUNTIME_PROFILES",
        {
            "python-only": {
                "homebrew": [],
                "python_imports": ["numpy"],
                "description": "Python-only test profile.",
            }
        },
    )

    def fail_run_print(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("python-only runtime profile should not check the Brewfile")

    def fake_run_capture(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(args=[], returncode=0, stdout="ok\n", stderr="")

    monkeypatch.setattr(cli, "run_print", fail_run_print)
    monkeypatch.setattr(cli, "run_capture", fake_run_capture)

    cli.cmd_runtime_check(SimpleNamespace(profile="python-only", repo=str(tmp_path)))


def test_public_terminology_audit_rejects_manual_language(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text("# Scientist Manual\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("# README\n", encoding="utf-8")
    (tmp_path / "mkdocs.yml").write_text("site_name: AI Lab\n", encoding="utf-8")
    templates = tmp_path / "research" / "templates"
    templates.mkdir(parents=True)
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    monkeypatch.setattr(cli, "DOCS", docs)
    issues: list[str] = []
    cli.check_public_terminology(issues)
    assert any("Scientist Manual" in issue for issue in issues)


def test_docs_audit_rejects_old_active_scientist_paths(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text("See tasks/active/demo/scientists/old/report.md\n", encoding="utf-8")
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    monkeypatch.setattr(cli, "DOCS", docs)
    monkeypatch.setattr(cli, "TASKS", tmp_path / "tasks" / "active")
    monkeypatch.setattr(cli, "SCHEMES", tmp_path / "schemes")
    monkeypatch.setattr(cli, "EVALUATIONS", tmp_path / "evaluations" / "active")
    monkeypatch.setattr(cli, "META", tmp_path / "meta" / "active")
    issues: list[str] = []
    cli.check_matrix_docs(issues)
    assert any("old task-nested scientist path" in issue for issue in issues)
