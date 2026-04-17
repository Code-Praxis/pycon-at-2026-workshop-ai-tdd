---
slice: 01
name: flat-rate-calculation
feature: shipping-costs
effort: ≤2h
---

# Slice-01: Flat-Rate Calculation

**Goal**: Verify that `calculate_delivery_fee` returns the correct fee for Zone A standard delivery using tiered weight pricing and BASE_RATE.

## IN Scope
- `calculate_delivery_fee(weight_kg, Zone.A, express=False)`
- Tiered weight cost: 0–5 kg @ €1.00, 5–20 kg @ €1.50, >20 kg @ €2.00
- BASE_RATE = €5.00
- Zone A multiplier = 1.0 (identity — no scaling)
- Return value rounded to 2dp

## OUT Scope
- Zone B and C multipliers (slice-02)
- Express surcharge (slice-03)
- Input validation errors (slice-04)

## Learning Hypothesis
Disproves "tier boundary calculations are correct" if the fee for a weight straddling a boundary (e.g., 10 kg) is wrong. Confirms "the tiered formula produces deterministic results" if all boundary cases pass.

## Acceptance Criteria
- `calculate_delivery_fee(3.0, Zone.A)` returns `8.00`
- `calculate_delivery_fee(5.0, Zone.A)` returns `10.00`
- `calculate_delivery_fee(10.0, Zone.A)` returns `18.75`  *(5×1.00 + 5×1.50 + BASE=5) × 1.0*
- `calculate_delivery_fee(20.0, Zone.A)` returns `32.50`
- `calculate_delivery_fee(25.0, Zone.A)` returns `42.50`
- Return type is `float`

## Dependencies
- `Zone` enum available from `shipping_costs`
- `BASE_RATE` constant = 5.00

## Reference Class
Pure function with tiered arithmetic — comparable to tax bracket calculations. No I/O, no state.

## Pre-slice SPIKE
None required. Logic is fully deterministic and the formula is explicit in the existing code.
