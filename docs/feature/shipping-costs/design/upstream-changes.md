# Upstream Changes
## Feature: shipping-costs — DESIGN wave findings
**Date**: 2026-04-17

## Changed Assumptions

### Calculation Error 1 — user-stories.md: `(10.0, Zone.A)` expected value

**Original** (`docs/feature/shipping-costs/discuss/user-stories.md`, US-01 Acceptance Criteria):
> `calculate_delivery_fee(10.0, Zone.A)` returns `18.75` (crosses tier-1/tier-2 boundary)

**Correct value**: `17.50`

**Derivation**:
- `calculate_weight_cost(10.0)` = 5×€1.00 + 5×€1.50 = 5.00 + 7.50 = **12.50**
- `fee` = (BASE_RATE 5.00 + 12.50) × Zone.A(1.0) = **17.50**

**Why**: The original value 18.75 appears to be the Zone B result for a different formula, or a transcription error. The source code in `src/shipping_costs/__init__.py` is authoritative.

---

### Calculation Error 2 — journey-calculate-shipping-fee.feature: `(10.0, Zone.B)` expected value

**Original** (`docs/feature/shipping-costs/discuss/journey-calculate-shipping-fee.feature`):
> `Then the fee is 18.75 EUR` (for 10.0 kg, Zone B, standard)

**Correct value**: `26.25`

**Derivation**:
- `calculate_weight_cost(10.0)` = 12.50
- `fee` = (5.00 + 12.50) × Zone.B(1.5) = 17.50 × 1.5 = **26.25**

**Why**: Transcription error in DISCUSS phase. Feature file comment even shows the correct formula `(5.00 + 12.50) × 1.5 = 26.25` but the `Then` line states 18.75.

---

**Action for product owner**: The test files created in DESIGN use the **correct values** (17.50 and 26.25). The DISCUSS artifacts contain the errors listed above. Please update `user-stories.md` slice-01 AC and `journey-calculate-shipping-fee.feature` scenario 2 to reflect the correct values.

DISCUSS documents are NOT modified by DESIGN (back-propagation rule preserved).
