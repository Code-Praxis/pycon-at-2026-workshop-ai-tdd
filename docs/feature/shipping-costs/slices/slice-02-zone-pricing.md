---
slice: 02
name: zone-pricing
feature: shipping-costs
effort: ≤1h
---

# Slice-02: Zone Pricing

**Goal**: Verify that the zone multiplier is applied to the full subtotal (BASE_RATE + weight_cost), and that all three zones produce correct fees.

## IN Scope
- Zone B (×1.5) and Zone C (×2.5) multipliers
- Multiplier applied to `(BASE_RATE + weight_cost)` — not just weight_cost
- Any weight value (exercises the interaction, not new tier logic)

## OUT Scope
- Express surcharge (slice-03)
- Input validation (slice-04)

## Learning Hypothesis
Disproves "zone multipliers interact correctly with BASE_RATE" if Zone B/C fees are calculated as `BASE_RATE + weight_cost × multiplier` instead of `(BASE_RATE + weight_cost) × multiplier`. This is the most common implementation mistake.

## Acceptance Criteria
- `calculate_delivery_fee(3.0, Zone.B)` returns `12.00`  *(5+3)×1.5 = 12.00*
- `calculate_delivery_fee(3.0, Zone.C)` returns `20.00`  *(5+3)×2.5 = 20.00*
- `calculate_delivery_fee(10.0, Zone.B)` returns `26.25`  *(5+12.5)×1.5*
- `calculate_delivery_fee(10.0, Zone.C)` returns `43.75`  *(5+12.5)×2.5*
- Zone A result unchanged from slice-01

## Dependencies
- Slice-01 passing (tiered weight cost proven correct)

## Reference Class
Dict-lookup multiplier pattern. No new abstraction required.

## Pre-slice SPIKE
None.
