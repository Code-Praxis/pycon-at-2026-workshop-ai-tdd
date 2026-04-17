# Outcome KPIs
## Feature: shipping-costs
**Date**: 2026-04-17

| # | KPI | Target | Measurement Method | Owner |
|---|-----|--------|-------------------|-------|
| K1 | Acceptance test pass rate | 100% | `pytest tests/acceptance/` — all Gherkin-derived scenarios green | CI pipeline |
| K2 | Unit test pass rate | 100% | `pytest tests/unit/` — all slice ACs covered | CI pipeline |
| K3 | Type checker errors | 0 | `ty check src` | CI pipeline |
| K4 | Linter violations | 0 | `ruff check .` | CI pipeline |
| K5 | Test coverage of `calculate_delivery_fee` | ≥95% | `pytest --cov=shipping_costs` | CI pipeline |
| K6 | Workshop attendees complete full RED→GREEN→ENFORCE loop | ≥80% of attendees | Workshop facilitator end-of-session check | Workshop facilitator |
| K7 | Time to first green test from `git clone` | ≤5 minutes | Facilitator stopwatch on 3 representative setups pre-workshop | Workshop facilitator |

## Notes
- K1–K5 are automated and must be green before any slice is marked done.
- K6–K7 are workshop-outcome KPIs that confirm the shipping costs function serves its teaching purpose (JOB-01, JOB-02).
- K7 addresses assumption A4 (environment setup) from `docs/feature/pycon-austria-2026-workshop/discover/problem-validation.md`.
