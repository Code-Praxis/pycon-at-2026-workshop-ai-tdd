# DISCUSS Decisions — shipping-costs

## Key Decisions
- [D1] Feature type = Backend: shipping cost calculation is a pure function with no UI — all story ACs reference the Python call signature, not a UI action (see: user-stories.md)
- [D2] Walking skeleton = No: `calculate_delivery_fee` already exists in `src/shipping_costs/__init__.py`; this is brownfield — the function is implemented but untested (see: src/shipping_costs/__init__.py)
- [D3] UX research depth = Lightweight: a deterministic backend function has one actor (caller) and one observable output (float) — a comprehensive emotional arc is not warranted (see: journey-calculate-shipping-fee-visual.md)
- [D4] JTBD = Skipped: workshop-level JTBD is already complete in `docs/feature/pycon-austria-2026-workshop/discuss/jtbd-job-stories.md`; all 4 stories trace to jobs documented there
- [D5] Slice execution order = validation-first: slice-04 (input validation) ships before the computation slices because a wrong boundary guard corrupts all downstream scenarios silently (see: prioritization.md)

## Requirements Summary
- Primary jobs/user needs: Checkout service needs a deterministic, tested, type-safe function to compute shipping fees by weight, zone, and delivery type
- Walking skeleton scope: N/A (brownfield)
- Feature type: Backend

## Constraints Established
- `weight_kg` must satisfy `0.0 ≤ weight_kg ≤ 100.0` — enforced by ValueError guards
- Zone is type-safe via `Zone` enum — invalid zone is a static type error, not a runtime error
- Express surcharge (€15.00) applies after zone multiplication — not before
- Return value is always `float` rounded to 2 decimal places

## Upstream Changes
- No DISCOVER assumptions changed. The shipping costs function is described in `problem-validation.md` (A2: "Shipping costs is a relatable, non-trivial domain") — DISCUSS confirms this assumption holds. The dual-implementation in `src/shipping_costs/__init__.py` (`calculate_delivery_fee` and `calculate_shipping_costs`) is the intentional teaching contrast documented in A5.
