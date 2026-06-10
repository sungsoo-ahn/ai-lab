Use the account AI Lab setup from ~/AGENTS.md.

Synthesize the completed fixed-runner cycle for task `btc` and scientist `btc_autoresearch_v1`.

Read the scientist guide, scientist report, source map, run spec, and the current run directory passed in the invocation. Update local AI Lab artifacts only:

- scientist `report.md`
- relevant work-unit reports if the cycle changed their evidence
- run summary under the current `runs/<run_id>/`
- source map or memory only when there is durable, non-sensitive information

Preserve failed trials, generated artifact pointers, package/runtime exceptions, exact commands, and safety status. Do not use sealed holdout, live trading, private API keys, connector writes, external submissions, or evaluation-rule changes.
