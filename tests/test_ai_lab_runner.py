from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

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


def valid_manifest() -> dict[str, object]:
    return {
        "schema_version": "ai_lab_task_v1",
        "task_id": "demo",
        "title": "Demo",
        "status": "active",
        "goal": "Find a useful observation.",
        "metric": {"name": "score", "direction": "maximize"},
        "observability": {"provider": "wandb_weave", "required": True},
    }


def valid_loop() -> dict[str, object]:
    return {
        "schema_version": "ai_lab_loop_v1",
        "task_id": "demo",
        "loop": {"mode": "continuous", "sleep_seconds": 0, "max_cycles": 1, "max_wall_minutes": 10},
        "source_gates": [],
        "commands": {
            "preflight": [{"id": "echo", "argv": ["python", "-c", "print('{run_id}', '{cycle}', '{task_id}')"]}],
            "cycle": [],
            "agent": [{"id": "agent", "builtin": "ai_scientist", "timeout_seconds": 30}],
        },
    }


def write_task(root: Path, task_id: str = "demo") -> Path:
    task = root / task_id
    task.mkdir(parents=True)
    (task / "README.md").write_text("# Demo\n", encoding="utf-8")
    (task / "task.yaml").write_text(
        """schema_version: ai_lab_task_v1
task_id: demo
title: Demo
status: active
goal: Find a useful observation.
metric:
  name: score
  direction: maximize
observability:
  provider: wandb_weave
  required: true
""",
        encoding="utf-8",
    )
    (task / "loop.yaml").write_text(
        """schema_version: ai_lab_loop_v1
task_id: demo
loop:
  mode: continuous
  sleep_seconds: 0
  max_cycles: 1
  max_wall_minutes: 10
source_gates: []
commands:
  preflight:
    - id: echo
      argv:
        - python
        - -c
        - print('ok')
  cycle: []
  agent: []
""",
        encoding="utf-8",
    )
    (task / "scientist.md").write_text("# Scientist\n", encoding="utf-8")
    reports = task / "reports"
    reports.mkdir()
    (reports / "current.md").write_text("# Current\n", encoding="utf-8")
    (reports / "observations.md").write_text("# Observations\n", encoding="utf-8")
    return task


def write_lab_config(path: Path) -> None:
    path.write_text(
        """schema_version: ai_lab_config_v1
observability:
  provider: wandb_weave
  entity: sungsoo-ahn
  project: ai-lab
  required: true
  payload: full_trace
""",
        encoding="utf-8",
    )


def test_task_manifest_validation_accepts_current_shape() -> None:
    cli = load_cli()
    assert cli.validate_task_manifest("demo", valid_manifest()) == []


def test_loop_validation_rejects_unknown_placeholder() -> None:
    cli = load_cli()
    spec = valid_loop()
    commands = spec["commands"]
    assert isinstance(commands, dict)
    commands["preflight"] = [{"id": "bad", "argv": ["echo", "{cell_id}"]}]
    issues = cli.validate_loop_spec("demo", spec)
    assert any("{cell_id}" in issue for issue in issues)


def test_active_task_ids_discovers_active_tasks(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    root = tmp_path / "tasks"
    write_task(root)
    inactive = root / "inactive"
    inactive.mkdir()
    (inactive / "task.yaml").write_text("status: inactive\n", encoding="utf-8")
    monkeypatch.setattr(cli, "TASKS", root)
    assert cli.active_task_ids() == ["demo"]


def test_task_run_dry_run_skips_wandb_and_commands(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    cli = load_cli()
    tasks = tmp_path / "tasks"
    write_task(tasks)
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "TASKS", tasks)
    monkeypatch.setattr(cli, "CONFIG", config)
    cli.cmd_task_run(
        SimpleNamespace(
            task_id="demo",
            once=True,
            continuous=False,
            dry_run=True,
            run_id="dry",
            max_cycles=None,
            no_wandb=False,
        )
    )
    out = capsys.readouterr().out
    assert "dry_run: demo run_id=dry" in out
    assert "[preflight] echo" in out
    assert not (tasks / "demo" / "runs" / "dry").exists()


def test_observability_requires_credentials_for_normal_runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "CONFIG", config)
    monkeypatch.delenv("WANDB_API_KEY", raising=False)
    obs = cli.Observability("demo", "run", dry_run=False)
    monkeypatch.setattr(obs, "_has_credentials", lambda: False)
    with pytest.raises(SystemExit) as exc:
        obs.start({"task_id": "demo"})
    assert "W&B observability is required" in str(exc.value)


def test_observability_logs_to_mocked_wandb_and_weave(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "CONFIG", config)
    monkeypatch.setenv("WANDB_API_KEY", "test-key")
    logged: list[dict[str, object]] = []
    weave_calls: list[dict[str, object]] = []

    class FakeRun:
        url = "https://wandb.ai/sungsoo-ahn/ai-lab/runs/test"

        def log(self, payload: dict[str, object]) -> None:
            logged.append(payload)

        def finish(self, exit_code: int = 0) -> None:
            logged.append({"finish": exit_code})

    fake_wandb = SimpleNamespace(init=lambda **_kwargs: FakeRun())

    def fake_op(name: str):
        def decorator(fn):
            def wrapped(event):
                weave_calls.append(event)
                return fn(event)

            return wrapped

        return decorator

    fake_weave = SimpleNamespace(init=lambda _project: None, op=fake_op)
    monkeypatch.setitem(sys.modules, "wandb", fake_wandb)
    monkeypatch.setitem(sys.modules, "weave", fake_weave)

    obs = cli.Observability("demo", "run", dry_run=False)
    obs.start({"task_id": "demo"})
    obs.log({"event": "command_start", "command_id": "x"})
    obs.finish("completed")

    assert obs.url.endswith("/runs/test")
    event_payloads = []
    for item in logged:
        payload = item.get("event_payload")
        if isinstance(payload, dict):
            event_payloads.append(payload)
    assert any(payload.get("event") == "command_start" for payload in event_payloads)
    assert any(item.get("event") == "command_start" for item in weave_calls)
    assert {"finish": 0} in logged


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

    run_dir = tmp_path / "run"
    run_dir.mkdir()
    cli.check_source_gate(
        {
            "source_id": "demo_source",
            "head_policy": "require_registered_ref",
            "tracked_clean": True,
            "allow_untracked": ["results/"],
        },
        strict=True,
        run_dir=run_dir,
    )
    assert "source_gate_pass" in (run_dir / "events.jsonl").read_text(encoding="utf-8")
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


def test_run_command_records_declared_artifacts_in_summary(tmp_path: Path) -> None:
    cli = load_cli()
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    cli.write_run_summary(run_dir, "demo", "running", None)
    artifact = run_dir / "result.json"
    context = {
        "task_id": "demo",
        "run_id": "artifact-test",
        "cycle": "1",
        "run_dir": str(run_dir),
        "task_dir": str(tmp_path),
        "root": str(ROOT),
    }
    obs = cli.Observability("demo", "artifact-test", dry_run=True)
    code = cli.run_command(
        {
            "id": "write_artifact",
            "argv": [sys.executable, "-c", f"from pathlib import Path; Path({str(artifact)!r}).write_text('{{}}')"],
            "artifacts": [str(artifact)],
        },
        group="cycle",
        context=context,
        run_dir=run_dir,
        dry_run=False,
        observability=obs,
    )
    assert code == 0
    summary = (run_dir / "run-summary.md").read_text(encoding="utf-8")
    assert "| `write_artifact` |" in summary
    assert "| `write_artifact` | `{}` | yes | `result.json` |".format(artifact) in summary
    artifact_rows = (run_dir / "artifacts.jsonl").read_text(encoding="utf-8")
    assert '"schema_version": "ai_lab_artifact_v1"' in artifact_rows


def test_task_summarize_writes_run_metadata_and_observation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    tasks = tmp_path / "tasks"
    task = write_task(tasks)
    monkeypatch.setattr(cli, "TASKS", tasks)
    run_dir = task / "runs" / "run1"
    run_dir.mkdir(parents=True)
    artifact = run_dir / "result.json"
    artifact.write_text("{}", encoding="utf-8")
    cli.append_event(run_dir, {"event": "run_start", "task_id": "demo", "run_id": "run1"})
    cli.append_event(
        run_dir,
        {
            "event": "command_finish",
            "group": "cycle",
            "cycle": 1,
            "command_id": "candidate",
            "returncode": 0,
            "artifacts": [{"pattern": str(artifact), "present": True, "matches": [str(artifact)]}],
        },
    )
    cli.append_event(run_dir, {"event": "run_finish", "task_id": "demo", "run_id": "run1"})
    (run_dir / "run-summary.md").write_text(
        """# AI Scientist Run: demo

Run ID: run1
Status: running
Started: 2026-06-11T00:00:00+00:00
Finished: pending
W&B: not started

## Observation

EMA baseline is weak after fees.

## Next Action

Audit turnover reduction.
""",
        encoding="utf-8",
    )

    cli.cmd_task_summarize(SimpleNamespace(task_id="demo", run_id="run1"))

    run = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    assert run["schema_version"] == "ai_lab_run_v1"
    assert run["status"] == "completed"
    observations = [json.loads(line) for line in (run_dir / "observations.jsonl").read_text(encoding="utf-8").splitlines()]
    assert observations[0]["claim"] == "EMA baseline is weak after fees."
    artifacts = [json.loads(line) for line in (run_dir / "artifacts.jsonl").read_text(encoding="utf-8").splitlines()]
    assert artifacts[0]["matches"] == ["result.json"]
    assert cli.validate_run_files("demo", "run1") == []


def test_memory_promote_creates_task_memory_and_docs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    tasks = tmp_path / "tasks"
    task = write_task(tasks)
    docs = tmp_path / "docs"
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "TASKS", tasks)
    monkeypatch.setattr(cli, "DOCS", docs)
    monkeypatch.setattr(cli, "CONFIG", config)
    run_dir = task / "runs" / "run2"
    run_dir.mkdir(parents=True)
    cli.append_event(run_dir, {"event": "run_finish", "task_id": "demo", "run_id": "run2"})
    (run_dir / "run-summary.md").write_text(
        """# AI Scientist Run: demo

Run ID: run2
Status: completed
Started: 2026-06-11T00:00:00+00:00
Finished: 2026-06-11T00:01:00+00:00
W&B: not started

## Observation

Funding-aware filters need a lower-turnover variant.

## Next Action

Test a weekly turnover cap.
""",
        encoding="utf-8",
    )

    cli.cmd_memory_promote(["demo", "--run-id", "run2"])
    cli.cmd_docs_sync(SimpleNamespace(check=False))

    insights = cli.load_yaml_file(task / "memory" / "insights.yaml")
    runs = cli.load_yaml_file(task / "memory" / "runs.yaml")
    assert insights["insights"][0]["claim"] == "Funding-aware filters need a lower-turnover variant."
    assert runs["runs"][0]["run_id"] == "run2"
    task_doc = (docs / "task" / "demo.md").read_text(encoding="utf-8")
    assert "Funding-aware filters need a lower-turnover variant." in task_doc
    assert "Recent Curated Runs" in task_doc


def test_run_command_respects_elapsed_wall_deadline(tmp_path: Path) -> None:
    cli = load_cli()
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    context = {
        "task_id": "demo",
        "run_id": "deadline-test",
        "cycle": "1",
        "run_dir": str(run_dir),
        "task_dir": str(tmp_path),
        "root": str(ROOT),
    }
    obs = cli.Observability("demo", "deadline-test", dry_run=True)
    code = cli.run_command(
        {"id": "late", "argv": ["python", "-c", "print('should not run')"]},
        group="cycle",
        context=context,
        run_dir=run_dir,
        dry_run=False,
        observability=obs,
        deadline_epoch=0,
    )
    assert code == 124
    assert "command_skipped" in (run_dir / "events.jsonl").read_text(encoding="utf-8")


def test_docs_audit_accepts_minimal_task_dashboard(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    docs = tmp_path / "docs"
    (docs / "task").mkdir(parents=True)
    (docs / "index.md").write_text("[Task](task/demo.md)\n", encoding="utf-8")
    (docs / "task" / "demo.md").write_text("# Demo\n", encoding="utf-8")
    tasks = tmp_path / "tasks"
    write_task(tasks)
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "DOCS", docs)
    monkeypatch.setattr(cli, "TASKS", tasks)
    monkeypatch.setattr(cli, "CONFIG", config)
    issues: list[str] = []
    cli.check_docs_links(issues)
    cli.check_task_docs(issues)
    assert issues == []


def test_docs_sync_generates_task_interfaces(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    docs = tmp_path / "docs"
    tasks = tmp_path / "tasks"
    write_task(tasks)
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "DOCS", docs)
    monkeypatch.setattr(cli, "TASKS", tasks)
    monkeypatch.setattr(cli, "CONFIG", config)

    cli.cmd_docs_sync(SimpleNamespace(check=False))

    assert "Generated by" in (docs / "index.md").read_text(encoding="utf-8")
    assert "| [Demo](task/demo.md) | `demo` | `score`, maximize | active |" in (docs / "index.md").read_text(encoding="utf-8")
    assert "No experiment code" in (docs / "task" / "demo.md").read_text(encoding="utf-8")
    assert "No promoted insights yet." in (docs / "task" / "demo.md").read_text(encoding="utf-8")
    assert "Experiment products are local logs" in (tasks / "demo" / "README.md").read_text(encoding="utf-8")
    assert "`memory/`: tracked curated run memory" in (tasks / "demo" / "README.md").read_text(encoding="utf-8")


def test_docs_sync_check_detects_drift(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    docs = tmp_path / "docs"
    tasks = tmp_path / "tasks"
    write_task(tasks)
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "DOCS", docs)
    monkeypatch.setattr(cli, "TASKS", tasks)
    monkeypatch.setattr(cli, "CONFIG", config)

    cli.cmd_docs_sync(SimpleNamespace(check=False))
    cli.cmd_docs_sync(SimpleNamespace(check=True))
    (docs / "index.md").write_text("# stale\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        cli.cmd_docs_sync(SimpleNamespace(check=True))


def test_task_docs_do_not_require_ignored_reports(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cli = load_cli()
    docs = tmp_path / "docs"
    tasks = tmp_path / "tasks"
    task = write_task(tasks)
    for path in (task / "reports").glob("*"):
        path.unlink()
    (docs / "task").mkdir(parents=True)
    (docs / "task" / "demo.md").write_text("# Demo\n", encoding="utf-8")
    config = tmp_path / "lab.yaml"
    write_lab_config(config)
    monkeypatch.setattr(cli, "DOCS", docs)
    monkeypatch.setattr(cli, "TASKS", tasks)
    monkeypatch.setattr(cli, "CONFIG", config)

    issues: list[str] = []
    cli.check_task_docs(issues)
    assert issues == []


def test_task_experiment_paths_are_ignored_except_placeholders() -> None:
    ignored_paths = ["tasks/demo/code/output.py", "tasks/demo/results/result.json", "tasks/demo/runs/run/events.jsonl"]
    ignored_results = [
        subprocess.run(["git", "check-ignore", "-q", path], cwd=ROOT, check=False).returncode
        for path in ignored_paths
    ]
    keep = subprocess.run(
        ["git", "check-ignore", "-q", "tasks/demo/code/.gitkeep"],
        cwd=ROOT,
        check=False,
    )
    assert ignored_results == [0, 0, 0]
    assert keep.returncode == 1


def test_codex_lab_wrapper_uses_exec_for_noninteractive_synthesis() -> None:
    text = (ROOT / "bin" / "codex-lab").read_text(encoding="utf-8")
    assert "codex --cd \"$HOME\" --ask-for-approval never" in text
    assert "codex exec -c approval_policy='never'" in text


def test_btc_extended_launcher_writes_task_local_launcher_log() -> None:
    text = (ROOT / "tasks" / "btc_benchmark" / "bin" / "run-btc-extended").read_text(encoding="utf-8")
    assert 'launcher_log="${run_dir}/launcher.log"' in text
    assert "logs/extended" not in text
