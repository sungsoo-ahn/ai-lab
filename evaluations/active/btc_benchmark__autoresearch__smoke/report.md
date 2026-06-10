# Evaluation Cell Report: btc_benchmark__autoresearch__smoke

Date: 2026-06-10
Status: complete

## Smoke Run: smoke-20260610

Status: passed
Run directory: `runs/smoke-20260610`

The fixed runner checked the registered `btc_benchmark` source and ran:

```sh
uv run python -m pytest tests/test_metrics.py -q
```

Result: `6 passed`. The benchmark checkout matched registered commit `166a99f0e915ba1aaaaa6da9451dfa90c49032a6`, had no tracked edits, and only had the allowed untracked `uv.lock`.
