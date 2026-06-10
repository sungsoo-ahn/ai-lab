# Work Unit Guide: ema_regime_robustness

Date: 2026-06-10
Status: active

## Purpose

This work unit tests whether `BestEmaRegimeV1` is a robust strategy family member.

## Method

Keep the frozen referee unchanged. Use gates-disabled screening only to rank nearby variants, then rerun top candidates with gates enabled. Preserve all screened rows and label non-gated evidence clearly.

## Expected Output

A small robustness table showing whether nearby fast/slow/band/min-hold choices remain strong, plus a recommendation to keep, adjust, or reject the current best.

## Safety Notes

- Do not use sealed holdout.
- Do not change referee scoring, costs, splits, gates, or accounting.
- Do not treat a screened-only result as submission-ready.
