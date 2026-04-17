# Prioritization
## Feature: shipping-costs
**Date**: 2026-04-17

## Execution Order and Rationale

| Order | Slice | Rationale |
|-------|-------|-----------|
| 1 | slice-04-input-validation | Highest uncertainty about boundary edge cases. A wrong guard (e.g., `<` vs `<=` on MAX_WEIGHT) corrupts all subsequent slices silently. Fail early. |
| 2 | slice-01-flat-rate-calculation | The weight-cost tiers are the core logic. Zone multipliers and express surcharge both compose on top — they are meaningless if the base calculation is wrong. |
| 3 | slice-02-zone-pricing | Low uncertainty (simple dict lookup), but must be verified after base calculation is proven. Confirms that multiplier application order is correct. |
| 4 | slice-03-express-surcharge | Lowest risk: a single additive constant applied after all other math. If this fails in isolation, the fix is trivially obvious. Ship last. |

## Dependency Chain

```
slice-04 (validate)
    └─► slice-01 (weight cost)
            └─► slice-02 (zone multiplier)
                    └─► slice-03 (express surcharge)
```

## Dogfood Cadence

Each slice produces a passing pytest run on the same day it is dispatched. The acceptance test in `tests/acceptance/` remains green across all four slices — it is the invariant the workshop attendee writes first.

## Learning Hypotheses per Slice (Prioritization View)

| Slice | Hypothesis | Value if Confirmed | Cost if Disproved |
|-------|-----------|-------------------|------------------|
| slice-04 | Boundary guards are correctly placed (`< 0`, `> 100.0`) | All inputs to downstream math are safe | Cheap fix before any math is written |
| slice-01 | Weight tier boundaries and rates produce correct subtotals | Zone math can be layered confidently | Misaligned tiers affect every downstream scenario |
| slice-02 | Zone multiplier applies to (BASE_RATE + weight_cost), not just weight_cost | Zone C scenarios are correct | Re-work of all zone-specific tests |
| slice-03 | Express surcharge adds after zone multiplication, not before | Final fee formula is correct | One-line fix with no downstream impact |
