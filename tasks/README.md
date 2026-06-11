# Tasks

Task workspaces define broad challenge or dataset families and own the runnable AI-scientist loop for that task.

Active task definitions live under `tasks/<task_id>/`.

Each task owns its goal, metric, constraints, loop spec, agent instructions, and maintained helper scripts. Experiment code, results, plots, reports, assets, and raw runs are local logs ignored by repo Git.
