# User Story Map
## Feature: shipping-costs
**Date**: 2026-04-17
**Walking Skeleton**: Not applicable (isolated backend function, Decision 2 = No)
**Slicing method**: Elephant Carpaccio (≤1 day per slice, each disproves a named hypothesis)

---

## Backbone (User Activities)

```
┌─────────────────────┬──────────────────────────┬──────────────────────────┬──────────────────────────┐
│   INPUT INTAKE      │   COST COMPUTATION       │   SURCHARGE APPLICATION  │   FEE DELIVERY           │
│                     │                          │                          │                          │
│ Caller provides     │ Calculate tiered weight  │ Add express surcharge    │ Return rounded float     │
│ weight, zone,       │ cost + apply zone        │ (optional)               │ to caller in EUR         │
│ express flag        │ multiplier               │                          │                          │
└─────────────────────┴──────────────────────────┴──────────────────────────┴──────────────────────────┘
```

---

## Story Map

```
ACTIVITY        │ Input Intake         │ Cost Computation          │ Surcharge            │ Fee Delivery
────────────────┼──────────────────────┼───────────────────────────┼──────────────────────┼──────────────────
                │                      │                           │                      │
SLICE-01        │ Accept weight_kg     │ Calculate tiered weight   │                      │ Return fee
flat-rate       │ (no zone, no         │ cost + BASE_RATE          │ —                    │ (float, 2dp)
                │ express)             │ Zone A only (×1.0)        │                      │
────────────────┼──────────────────────┼───────────────────────────┼──────────────────────┼──────────────────
SLICE-02        │ Accept zone param    │ Look up zone multiplier   │                      │ Return zone-
zone-pricing    │                      │ Apply to subtotal         │ —                    │ adjusted fee
────────────────┼──────────────────────┼───────────────────────────┼──────────────────────┼──────────────────
SLICE-03        │ Accept express flag  │                           │ Add €15.00 when      │ Return fee with
express-        │                      │ —                         │ express=True         │ surcharge
surcharge       │                      │                           │                      │
────────────────┼──────────────────────┼───────────────────────────┼──────────────────────┼──────────────────
SLICE-04        │ Validate weight_kg   │                           │                      │ Raise ValueError
input-          │ (negative, over-max) │ —                         │ —                    │ with message
validation      │                      │                           │                      │
```

---

## Carpaccio Taste Tests

| Test | Slice-01 | Slice-02 | Slice-03 | Slice-04 |
|------|:---:|:---:|:---:|:---:|
| Ships ≤4 new components? | ✓ (1 fn) | ✓ (1 lookup) | ✓ (1 branch) | ✓ (2 guards) |
| No slice depends on new abstraction? | ✓ | ✓ | ✓ | ✓ |
| Each disproves a named hypothesis? | ✓ | ✓ | ✓ | ✓ |
| Uses/targets production-data paths? | ✓ | ✓ | ✓ | ✓ |
| Dogfood moment same day? | ✓ | ✓ | ✓ | ✓ |
| Explicit IN/OUT scope? | ✓ | ✓ | ✓ | ✓ |

All taste tests pass.

---

## Slice Execution Order

1. **Slice-04** (input-validation) — highest learning leverage; a wrong validation guard corrupts all downstream slices
2. **Slice-01** (flat-rate-calculation) — foundation; all zone/express math builds on correct tiered pricing
3. **Slice-02** (zone-pricing) — extends slice-01; confirms multiplier interaction
4. **Slice-03** (express-surcharge) — final additive layer; lowest risk, isolated to one constant
