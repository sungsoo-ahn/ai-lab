from __future__ import annotations

import importlib.util
import importlib.machinery
import subprocess
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
        "schema_version": "ai_lab_scientist_run_v1",
        "task_id": "demo",
        "scientist_id": "demo_scientist",
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
                    "argv": ["python", "-c", "print('{run_id}', '{cycle}')"],
                    "timeout_seconds": 30,
                    "artifacts": ["results/**"],
                }
            ],
            "synthesis": [{"id": "synthesis", "builtin": "synthesize", "timeout_seconds": 30}],
        },
    }


def test_run_spec_validation_accepts_valid_shape(tmp_path: Path) -> None:
    cli = load_cli()
    path = tmp_path / "tasks" / "active" / "demo" / "scientists" / "demo_scientist" / "run-spec.yaml"
    path.parent.mkdir(parents=True)
    assert cli.validate_run_spec(valid_spec(), path=path) == []


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
    path = tmp_path / "tasks" / "active" / "demo" / "scientists" / "demo_scientist" / "run-spec.yaml"
    path.parent.mkdir(parents=True)
    issues = cli.validate_run_spec(spec, path=path)
    assert any("exactly one of argv, script, or builtin" in issue for issue in issues)
    assert any("{unsupported}" in issue for issue in issues)


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
