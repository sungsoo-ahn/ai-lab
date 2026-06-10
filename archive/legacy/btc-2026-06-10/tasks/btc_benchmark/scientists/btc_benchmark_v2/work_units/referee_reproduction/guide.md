# Work Unit Guide: referee_reproduction

Date: 2026-06-10
Status: active

## Purpose

This work unit verifies that the benchmark referee can be installed, tested, and used to load data before any strategy optimization begins.

## Method

Use `uv` commands from the referee checkout. The first verified problem is structural: `btc_benchmark/data` is absent from the repository even though tests and bootstrap scripts import it. A repair should copy or adapt data modules from the stated `btc_autoresearch` lineage only for data download/imputation/validation support. Do not change `btc_benchmark/benchmark/runner.py`, `validity.py`, cost model behavior, or walk-forward scoring semantics as part of this work unit unless the change is a documented bug fix with tests.

## Expected Output

Passing referee tests and a loadable benchmark data bundle.

## Safety Notes

- This work unit must not touch the sealed holdout except through the referee's own dev split firewall.
- This work unit must not weaken scoring, causality gates, cost settings, or accounting.
