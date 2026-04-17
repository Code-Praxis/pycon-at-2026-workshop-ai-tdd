# ADR-001: Separate Acceptance and Unit Test Directories

**Date**: 2026-04-17
**Status**: Accepted
**Feature**: shipping-costs

## Context

The workshop teaches the distinction between acceptance tests (behavioral, survive refactor) and unit tests (implementation-coupled, break on refactor). The test directory structure must make this distinction physically visible and structurally enforced — not just conceptual.

The deleted test file was at `tests/features/test_shipping_costs.py` — a flat layout that blurs the distinction.

## Decision

Use two separate directories:

```
tests/
  acceptance/   ← behavioral tests only; import calculate_delivery_fee, never calculate_weight_cost
  unit/         ← unit tests only; import calculate_weight_cost directly
```

The import rule is the enforcement mechanism: acceptance tests that import `calculate_weight_cost` are violating the boundary and must be moved to `unit/`.

## Alternatives Considered

1. **Flat `tests/` with naming convention** (`test_acceptance_*.py`, `test_unit_*.py`) — rejected because the distinction is invisible at a glance; workshop attendees lose the visual signal
2. **Single `tests/` directory** (original layout) — rejected because it merges the two concepts the workshop is explicitly teaching
3. **pytest markers** (`@pytest.mark.acceptance`) — rejected because markers are invisible without reading the test body; directory structure is self-documenting

## Consequences

- `pytest` runs both suites with a single `pytest` command (configured via `testpaths = ["tests"]`)
- The refactor exercise is structurally supported: attendees can observe which directory's tests break
- `tests/unit/` tests are expected to break when `calculate_shipping_costs` is refactored — this is intended, not a bug
