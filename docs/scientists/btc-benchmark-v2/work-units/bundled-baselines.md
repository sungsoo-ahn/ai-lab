# Work Unit: BTC Benchmark Bundled Baselines

<div class="run-metadata">
<p><strong>Work Unit ID:</strong> bundled_baselines</p>
<p><strong>Scientist:</strong> btc_benchmark_v2</p>
<p><strong>Status:</strong> complete</p>
<p><strong>Date:</strong> 2026-06-10 KST</p>
</div>

## Purpose

Score the participant repository's bundled examples to establish baseline behavior and environment gaps.

## Results

| Strategy | Outcome |
| --- | --- |
| `EmaTrend` | Gates passed, but dev net was `-81.7%`, below buy-and-hold. |
| `XgbMomentum` | Gates passed after Homebrew `libomp` and a transient `uv --with scikit-learn` overlay; dev net was `+53.3%`, below buy-and-hold. |

## Runtime Decision

The XGBoost failure motivated a system update: approved long runs may now use the `xgboost-macos` runtime profile to install Homebrew `libomp` from the lab `Brewfile` and verify `import xgboost`. Python extras such as `scikit-learn` should be supplied through local `uv` workflows and recorded in the run report.

## Safety Checklist

- Referee rules changed: no
- Runtime profile satisfied: yes
- Failed baseline preserved: yes
- Live trading/API keys used: no

## Implementation References

- Work-unit report: `tasks/active/btc_benchmark/scientists/btc_benchmark_v2/work_units/bundled_baselines/report.md`
- Runtime policy: `policies/scientist-runtime-policy.md`
