# User Stories
## Feature: shipping-costs
**Date**: 2026-04-17
**JTBD Source**: `docs/feature/pycon-austria-2026-workshop/discuss/jtbd-job-stories.md`
**Journey Source**: `docs/feature/shipping-costs/discuss/journey-calculate-shipping-fee.yaml`

---

## US-01: Weight-Based Shipping Fee Calculation

**Story**

As a checkout service,  
when I call `calculate_delivery_fee(weight_kg, zone)` with a valid weight and zone,  
I want to receive the correct tiered weight cost plus BASE_RATE, multiplied by the zone factor,  
so that I can display the accurate shipping fee to the customer before payment.

**JTBD Traceability**: JOB-01 (Trusted AI Workflow), JOB-02 (TDD on Real Code)

### Elevator Pitch
Before: no programmatic way to get a deterministic, tested shipping fee — callers must hardcode or estimate.  
After: call `calculate_delivery_fee(3.0, Zone.A)` → returns `8.0` (€5 base + €3 weight × 1.0 zone multiplier).  
Decision enabled: checkout system presents the confirmed shipping cost to the customer before they confirm payment.

### Acceptance Criteria
- `calculate_delivery_fee(3.0, Zone.A)` returns `8.00`
- `calculate_delivery_fee(5.0, Zone.A)` returns `10.00` (at tier-1 boundary)
- `calculate_delivery_fee(10.0, Zone.A)` returns `18.75` (crosses tier-1/tier-2 boundary)
- `calculate_delivery_fee(20.0, Zone.A)` returns `32.50` (at tier-2 boundary)
- `calculate_delivery_fee(25.0, Zone.A)` returns `42.50` (in tier-3)
- Return type is `float`, rounded to 2 decimal places
- Zone A multiplier is 1.0 (identity — result equals BASE_RATE + weight_cost)

**Slice**: slice-01-flat-rate-calculation

---

## US-02: Zone-Adjusted Fee

**Story**

As a checkout service,  
when I provide a destination zone (A, B, or C),  
I want the entire subtotal (BASE_RATE + weight cost) multiplied by the zone factor,  
so that the fee correctly reflects the delivery distance to the customer's region.

**JTBD Traceability**: JOB-01 (Trusted AI Workflow), JOB-02 (TDD on Real Code)

### Elevator Pitch
Before: no way to verify whether zone multiplication applies to the whole subtotal or only the weight cost — the error is silent.  
After: call `calculate_delivery_fee(3.0, Zone.C)` → returns `20.00` (confirming `(5+3)×2.5`, not `5+(3×2.5)`).  
Decision enabled: logistics team can confidently configure zone multipliers knowing the formula is correct.

### Acceptance Criteria
- `calculate_delivery_fee(3.0, Zone.B)` returns `12.00`
- `calculate_delivery_fee(3.0, Zone.C)` returns `20.00`
- `calculate_delivery_fee(10.0, Zone.B)` returns `26.25`
- `calculate_delivery_fee(10.0, Zone.C)` returns `43.75`
- Zone multiplier applies to `(BASE_RATE + weight_cost)`, not just `weight_cost`
- All three zones (A, B, C) are supported via the `Zone` enum

**Slice**: slice-02-zone-pricing

---

## US-03: Express Delivery Surcharge

**Story**

As a checkout service,  
when I call `calculate_delivery_fee(weight_kg, zone, express=True)`,  
I want a flat €15.00 surcharge added after the zone-adjusted cost,  
so that express delivery is correctly priced as a premium option available in any zone.

**JTBD Traceability**: JOB-01 (Trusted AI Workflow)

### Elevator Pitch
Before: express pricing is undocumented and untested — callers hardcode €15 manually and drift from the source of truth.  
After: call `calculate_delivery_fee(3.0, Zone.A, express=True)` → returns `23.00` (8.00 + 15.00).  
Decision enabled: product team can change EXPRESS_SURCHARGE in one place and know all callers reflect the new value.

### Acceptance Criteria
- `calculate_delivery_fee(3.0, Zone.A, express=True)` returns `23.00`
- `calculate_delivery_fee(3.0, Zone.A, express=False)` returns `8.00` (unchanged)
- `calculate_delivery_fee(3.0, Zone.C, express=True)` returns `35.00`  (`(5+3)×2.5 + 15 = 35.00`)
- `express` defaults to `False`
- Express surcharge is applied after zone multiplication (not before)

**Slice**: slice-03-express-surcharge

---

## US-04: Input Validation

**Story**

As a backend service,  
when I call `calculate_delivery_fee` with a weight below zero or above 100 kg,  
I want a `ValueError` raised immediately with a descriptive message,  
so that invalid data never silently produces a wrong fee that reaches the customer.

**JTBD Traceability**: JOB-01 (Trusted AI Workflow), JOB-02 (TDD on Real Code — boundary edge cases)

### Elevator Pitch
Before: passing `weight_kg=-1.0` produces a negative fee with no error — silent corruption.  
After: call `calculate_delivery_fee(-1.0, Zone.A)` → raises `ValueError("Weight cannot be negative.")`.  
Decision enabled: integration layer can trust that any float returned by the function is a valid, non-negative fee.

### Acceptance Criteria
- `calculate_delivery_fee(-0.001, Zone.A)` raises `ValueError("Weight cannot be negative.")`
- `calculate_delivery_fee(-1.0, Zone.A)` raises `ValueError("Weight cannot be negative.")`
- `calculate_delivery_fee(100.001, Zone.A)` raises `ValueError("Weight exceeds maximum allowed (100.0 kg).")`
- `calculate_delivery_fee(0.0, Zone.A)` does NOT raise — returns a valid float
- `calculate_delivery_fee(100.0, Zone.A)` does NOT raise — returns a valid float
- Error message is exact (used by callers for error display)

**Slice**: slice-04-input-validation
