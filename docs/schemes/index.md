# Scientist Schemes

Scientist schemes are reusable orchestration patterns that can be applied to multiple tasks. They define how work is proposed, assigned, executed, criticized, summarized, and converted into next-step proposals.

Schemes should not contain task-specific claims. A scheme can say "run a bounded experiment loop" or "split work across independent roles." It should not say "funding improves BTC performance"; that belongs in the hypothesis catalog.

## Active Schemes

| Scheme | Status | Best fit | Main risk |
| --- | --- | --- | --- |
| [AutoResearch](autoresearch.md) | active | Tasks with a measurable target and fast experiment loop. | Metric chasing without enough critique or negative-result memory. |
| [AutoScientist](autoscientist.md) | active | Tasks that benefit from independent roles, critique, and synthesis. | Producing more text than evidence if work-unit boundaries are weak. |

## Choosing A Scheme

Use AutoResearch when:

- the target metric is clear;
- experiments are cheap enough to iterate;
- source gates and expected artifacts are stable;
- the main need is disciplined propose-execute-evaluate-synthesize flow.

Use AutoScientist when:

- the task has several plausible research directions;
- critique and independent work streams are valuable;
- one agent's local optimum is likely to be misleading;
- the output needs a synthesis across different kinds of evidence.

When in doubt, start with AutoResearch for a smoke cell and promote to AutoScientist only when the task needs parallel work units or stronger adversarial review.

## Scheme Evaluation

A scheme should be judged on more than the final task score:

- evidence quality;
- number and usefulness of falsified hypotheses;
- reproducibility of artifacts;
- quality of critique;
- clarity of proposals;
- ability to stop when exit criteria are met;
- amount of human intervention required.
