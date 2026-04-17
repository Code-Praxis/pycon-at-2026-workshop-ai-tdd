---
slice: 03
name: express-surcharge
feature: shipping-costs
effort: ≤1h
---

# Slice-03: Express Surcharge

**Goal**: Verify that `express=True` adds exactly €15.00 after zone-adjusted cost, and `express=False` adds nothing.

## IN Scope
- `express=True` adds `EXPRESS_SURCHARGE = €15.00` after zone multiplication
- `express=False` (default) leaves fee unchanged
- Surcharge is flat — not multiplied by zone

## OUT Scope
- Zone multiplier correctness (slice-02)
- Input validation (slice-04)

## Learning Hypothesis
Disproves "express surcharge applies after zone multiplication (not before)" if the surcharge is accidentally included inside the zone-multiplied subtotal. Confirms ordering is correct when zone C with express matches the expected formula `(BASE + weight) × zone + 15.00`.

## Acceptance Criteria
- `calculate_delivery_fee(3.0, Zone.A, express=True)` returns `23.00`  *(5+3)×1.0 + 15 = 23.00*
- `calculate_delivery_fee(3.0, Zone.A, express=False)` returns `8.00`  (unchanged from slice-01)
- `calculate_delivery_fee(3.0, Zone.C, express=True)` returns `35.00`  *(5+3)×2.5 + 15 = 35.00*
- Default value of `express` is `False`

## Dependencies
- Slice-01 and slice-02 passing

## Reference Class
Single additive constant applied conditionally. Zero risk of cascading failure.

## Pre-slice SPIKE
None.
