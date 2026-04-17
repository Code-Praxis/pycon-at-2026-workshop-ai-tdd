# Evolution: shipping-costs — 2026-04-17

## Feature Summary

Acceptance-tested implementation of `calculate_delivery_fee` for the PyCon Austria 2026 workshop.
The function was already implemented in `src/shipping_costs/__init__.py`; this delivery wave added
a full acceptance + unit test suite demonstrating ATDD/TDD practice with LLM assistance.

**Business context**: Workshop demonstration of Vibe Coding with Guard Rails — AI-assisted TDD for
a checkout service shipping fee calculation (weight tiers × zone multiplier + express surcharge).

## Steps Completed

| Step | Name | Result |
|------|------|--------|
| 01-01 | Implement input validation guards | PASS (GREEN + COMMIT) |
| 01-02 | Implement tiered weight cost calculation | PASS (GREEN + COMMIT) |
| 01-03 | Implement zone multiplier application | PASS (GREEN + COMMIT) |
| 01-04 | Implement express delivery surcharge | PASS (GREEN + COMMIT) |
| 01-05 | Fix Testing Theater in TestInputValidation | PASS (GREEN + COMMIT) |

All RED phases logged as NOT_APPLICABLE (brownfield — implementation pre-existed).

## Quality Gates

| Gate | Result |
|------|--------|
| Adversarial review (Phase 4) | PASS — Testing Theater detected and fixed (step 01-05) |
| Mutation testing (Phase 5) | PASS — 83% kill rate (39/47 testable mutants) |
| DES integrity verification (Phase 6) | PASS — all 5 steps traced |

## Key Decisions

From DISCUSS:
- **D2**: No walking skeleton — brownfield; implementation pre-existed
- **D5**: Slice order validation-first — guards ship before computation

From DESIGN:
- **D3**: No ports-and-adapters — pure function has no I/O boundary; ceremony without benefit
- **D4**: Functional Python paradigm — formalised in CLAUDE.md
- **D5**: Acceptance/unit test split — separate directories enforce the ATDD teaching point

## Issues Encountered

1. **DISCUSS calculation errors** — Two ACs in user-stories.md contained wrong expected values
   (`18.75` instead of `17.50` for 10 kg Zone A, and `18.75` instead of `26.25` for 10 kg Zone B).
   Documented in `design/upstream-changes.md`; tests were written with correct values. DISCUSS
   artifacts were NOT modified per back-propagation rules.

2. **Testing Theater** (adversarial review) — `TestInputValidation` had 4 theater patterns:
   - `isinstance(result, float)` — type-only assertion (no business value)
   - `round(result, 2) == result` — circular assertion (round of round is always equal)
   Removed 2 test methods, replaced 2 with exact value assertions (`== 5.00`, `== 192.50`).

3. **Teaching foil mutants** — `calculate_shipping_costs` has 29 "no tests" mutants. Intentional:
   the function is an alternative implementation shown to attendees as a refactoring exercise.
   Kill rate calculated on tested functions only: 83%.

## Lessons Learned

- Brownfield delivery can skip RED phases cleanly via `NOT_APPLICABLE` + approved prefix convention.
- Testing Theater is easier to catch in adversarial review than during initial writing — the 7-pattern
  checklist is a reliable guide.
- DES hook enforcement prevented direct file edits during the session, which correctly forced all
  test changes through the crafter agent pipeline.

## Migrated Artifacts

- `docs/ux/shipping-costs/journey-calculate-shipping-fee.yaml`
- `docs/ux/shipping-costs/journey-calculate-shipping-fee-visual.md`

## Source Artifacts (preserved in docs/feature/shipping-costs/)

- `discuss/` — user stories, story map, DOR validation, outcome KPIs
- `design/` — wave decisions, upstream changes
- `deliver/` — roadmap, execution log
