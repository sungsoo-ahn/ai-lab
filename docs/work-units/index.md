# Work Unit Manuals

Work-unit manuals explain focused units of agent work. A work unit may produce a score trial, a result bundle, an audit finding, a negative result, a synthesis report, an infrastructure pass, or a proposal for the next scientist version.

Work units are not the same as score trials. Some work units directly optimize a metric; others make future optimization safer or more interpretable.

## BTC Work Units

| Work Unit | Status | Type | Current Read |
| --- | --- | --- | --- |
| [`baseline_reproduction`](btc/baseline-reproduction.md) | complete | observation / readiness | `t054` reproduced at +94.0% net with sealed holdout unused. |
| [`pipeline_audit`](btc/pipeline-audit.md) | complete | audit | No accounting/split/holdout blocker found; reporting hygiene remains. |
| [`horizon_h4_audit`](btc/horizon-h4-audit.md) | complete | audit | H=4 default winners weaken sharply under horizon-matched holding. |
| [`regime_filter_probe`](btc/regime-filter-probe.md) | complete | observation / robustness | `t094` is promising but needs lower concentration and better fold coverage. |
| [`report_synthesis`](btc/report-synthesis.md) | complete | synthesis | Continue with robustness work, not holdout promotion. |

## Why This Matters

A scientist can improve by learning what not to trust. The H=4 audit and pipeline audit are useful even though they do not directly maximize the score. They constrain future score search and prevent false progress.

## Work-Unit Manual Contract

Each work-unit manual must explain purpose, method, commands, artifacts, agent/tool roles, result, decision, safety checks, failure modes, and how to continue. Implementation paths may be listed for audit, but the manual text should be sufficient for understanding.
