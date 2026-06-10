# BTC Work Units

Work units are not the same as score trials. A work unit may produce a result bundle, an audit finding, a negative result, a synthesis report, or a proposal for the next scientist version.

| Work Unit | Status | Purpose | Current Read |
| --- | --- | --- | --- |
| [`baseline_reproduction`](baseline-reproduction.md) | complete | Reproduce the local baseline and readiness gate. | `t054` reproduced at +94.0% net with sealed holdout unused. |
| [`pipeline_audit`](pipeline-audit.md) | complete | Audit leakage, cost, holdout, and reproducibility risks. | No accounting/split/holdout blocker found; reporting hygiene remains. |
| [`horizon_h4_audit`](horizon-h4-audit.md) | complete | Investigate H=4 horizon-matched behavior. | H=4 default winners weaken sharply under horizon-matched holding. |
| [`regime_filter_probe`](regime-filter-probe.md) | complete | Audit the strongest H=1 candidate family. | `t094` is promising but needs lower concentration and better fold coverage. |
| [`report_synthesis`](report-synthesis.md) | complete | Summarize overnight results and next actions. | Continue with robustness work, not holdout promotion. |

## Why This Matters

A scientist can improve by learning what not to trust. The H=4 audit and pipeline audit are useful even though they do not directly maximize the score. They constrain future score search and prevent false progress.

## Source Files

The canonical work-unit files live under:

```text
tasks/active/btc/scientists/btc_autoresearch_v1/work_units/
```

The public site summarizes those reports; the repository files remain the source of truth.
