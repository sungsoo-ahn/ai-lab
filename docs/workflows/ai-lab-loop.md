# AI Lab Scientist Loop

The AI Lab loop is broader than a score search. A scientist may open work units that reproduce a baseline, audit leakage risks, run score-maximizing trials, test a negative finding, synthesize reports, or propose a next scientist version.

The current BTC scientist uses this loop for BTCUSDT short-horizon backtesting. The performance plot in the first tutorial shows score-search trials, while the work-unit index records audits and synthesis work that do not necessarily improve the target metric directly.

## Flowchart

```mermaid
flowchart LR
  S[Scientist State] -->|current_report.md| P[Work Unit Planner]
  P -->|work-unit.yaml| C[Source Checkout]
  C -->|immutable_git_ref| E[Experiment Evaluator]
  E -->|trial_ledger.csv and metrics| A[Critic And Auditor]
  A -->|critique.md and caveats| R[Report Synthesis]
  R -->|scientist_report.md| H[Human Gate]
  H -->|accept / reject / rerun| S
  A -->|proposal.md| V[Next Scientist Version Gate]
```

## One Loop

```mermaid
sequenceDiagram
  participant State as Scientist State
  participant Planner as Work Unit Planner
  participant Source as Source Checkout
  participant Eval as Experiment Evaluator
  participant Audit as Critic/Auditor
  participant Report as Report Synthesis
  participant Human as Human Reviewer

  State->>Planner: current goal, constraints, reports
  Planner->>Source: source_id and immutable git_ref
  Source->>Eval: reproducible code and static configs
  Eval->>Audit: metrics, trial ledger, artifacts
  Audit->>Report: caveats, negative findings, next actions
  Report->>Human: updated scientist report
  Human->>State: accept, reject, rerun, or propose next version
```

## BTC Example

The BTC scientist has five current work units:

- `baseline_reproduction`: reproduced `t054` and verified readiness.
- `pipeline_audit`: checked leakage, costs, timestamp alignment, and holdout protection.
- `horizon_h4_audit`: found that H=4 default candidates weaken under horizon-matched holding.
- `regime_filter_probe`: audited `t094` and kept it at needs-refinement status.
- `report_synthesis`: summarized the overnight run and next action.

The machine-readable example workflow is stored at [ai-lab-scientist-workflow.yaml](../assets/ai-lab-scientist-workflow.yaml).

The score-search plot is shown in [First BTC trial inspection](../tutorials/first-btc-trial.md).
