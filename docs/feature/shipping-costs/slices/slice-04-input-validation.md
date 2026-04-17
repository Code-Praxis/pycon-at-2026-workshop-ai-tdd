---
slice: 04
name: input-validation
feature: shipping-costs
effort: ≤1h
---

# Slice-04: Input Validation

**Goal**: Verify that invalid weight inputs raise `ValueError` with exact messages before any cost calculation occurs.

## IN Scope
- `weight_kg < 0` raises `ValueError("Weight cannot be negative.")`
- `weight_kg > 100.0` raises `ValueError("Weight exceeds maximum allowed (100.0 kg).")`
- `weight_kg == 0` is accepted (zero-weight is valid)
- `weight_kg == 100.0` is accepted (at-maximum is valid)

## OUT Scope
- Cost calculation logic (slices 01–03)
- Zone or express parameter validation (type system / enum handles that)

## Learning Hypothesis
Disproves "boundary guards use correct operators" if `weight_kg == 0` raises an error (off-by-one: `<= 0` instead of `< 0`) or `weight_kg == 100.0` raises an error (off-by-one: `>= MAX_WEIGHT` instead of `> MAX_WEIGHT`). Boundary errors in validation corrupt every upstream caller silently.

## Acceptance Criteria
- `calculate_delivery_fee(-0.001, Zone.A)` raises `ValueError` with message `"Weight cannot be negative."`
- `calculate_delivery_fee(-1.0, Zone.A)` raises `ValueError` with message `"Weight cannot be negative."`
- `calculate_delivery_fee(100.001, Zone.A)` raises `ValueError` with message `"Weight exceeds maximum allowed (100.0 kg)."`
- `calculate_delivery_fee(0.0, Zone.A)` does NOT raise — returns a valid float
- `calculate_delivery_fee(100.0, Zone.A)` does NOT raise — returns a valid float
- Error is raised before any cost calculation (guards at top of function)

## Dependencies
- None — this slice can run independently of slices 01–03

## Reference Class
Guard-clause validation at function entry. No external dependencies.

## Pre-slice SPIKE
None. Boundary conditions are fully specified.
