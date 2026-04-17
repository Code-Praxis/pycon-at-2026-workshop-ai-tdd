# Journey: Calculate Shipping Fee
## Feature: shipping-costs
**Type**: Backend — API contract journey
**Date**: 2026-04-17
**Depth**: Lightweight
**Grounded in**: `docs/feature/pycon-austria-2026-workshop/discuss/jtbd-job-stories.md` (JOB-01, JOB-02)

---

## Mental Model

The caller (checkout service, order processor, or workshop attendee) thinks of shipping as: *"given a package and a destination zone, give me a number in euros."* They do not think in terms of internal tiers or multiplier tables. They expect:

- One function call
- One float back
- Errors for obviously bad inputs (negative weight, impossibly heavy package)

The vocabulary they use: **weight**, **zone**, **express**, **fee**. Not "multiplier", "surcharge object", or "pricing config".

---

## Journey Steps

```
Caller                          calculate_delivery_fee()
  │                                      │
  │── 1. Assemble inputs ──────────────►│
  │   weight_kg: float                   │
  │   zone: Zone (A | B | C)            │
  │   express: bool (default False)     │
  │                                      │
  │                        2. Validate inputs
  │                           weight_kg < 0  → ValueError ──► Caller handles error
  │                           weight_kg > 100 → ValueError ──► Caller handles error
  │                                      │
  │                        3. Calculate weight cost (tiered)
  │                           0–5 kg    @ €1.00/kg
  │                           5–20 kg   @ €1.50/kg
  │                           >20 kg    @ €2.00/kg
  │                           + BASE_RATE €5.00
  │                                      │
  │                        4. Apply zone multiplier
  │                           Zone A: × 1.0
  │                           Zone B: × 1.5
  │                           Zone C: × 2.5
  │                                      │
  │                        5. Add express surcharge
  │                           express=True: + €15.00
  │                           express=False: + €0.00
  │                                      │
  │                        6. Round to 2 decimal places
  │                                      │
  │◄── fee: float (EUR) ────────────────│
  │
  └── Caller uses fee (display, store, compare)
```

---

## Emotional Arc

| Step | Caller State | Note |
|------|-------------|------|
| 1. Assemble inputs | Neutral — has the data, needs a number | |
| 2. Validation | Confident — invalid inputs caught early, not silently wrong | |
| 3–5. Calculation | Not visible to caller | Pure internal state |
| 6. Receive fee | **Confident** — exact, reproducible, typed result | Goal achieved |
| Error path | Frustrated → quickly resolved | Clear ValueError message tells caller what went wrong |

Arc: **Neutral → Confident**. No anxiety about silent miscalculation — the function either returns a correct number or raises clearly.

---

## Shared Artifacts

| Artifact | Type | Source Step | Consumed By |
|----------|------|-------------|-------------|
| `weight_kg` | `float` | Caller (step 1) | Validation (step 2), Weight calculation (step 3) |
| `zone` | `Zone` (enum) | Caller (step 1) | Zone multiplier (step 4) |
| `express` | `bool` | Caller (step 1) | Express surcharge (step 5) |
| `fee` | `float` (EUR, 2dp) | Round step (step 6) | Caller (display / store) |

Single source of truth for each artifact: see `shared-artifacts-registry.md`.

---

## Error Paths

| Trigger | Behaviour | Recovery |
|---------|-----------|---------|
| `weight_kg < 0` | `ValueError("Weight cannot be negative.")` | Caller validates input before calling |
| `weight_kg > 100.0` | `ValueError("Weight exceeds maximum allowed (100.0 kg).")` | Caller rejects oversized shipments upstream |
| Invalid zone | `KeyError` from `_ZONE_MULTIPLIERS` lookup | Caller uses `Zone` enum — invalid zone is a type error caught at import time |
