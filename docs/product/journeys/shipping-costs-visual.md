# Journey: Calculate Shipping Fee (SSOT)
**Feature**: shipping-costs | **Type**: Backend | **Date**: 2026-04-17

## Entry Point
`calculate_delivery_fee(weight_kg: float, zone: Zone, express: bool = False) -> float`

## Summary
A checkout service provides package weight, destination zone, and delivery preference. The function validates inputs, computes a tiered weight cost, applies a zone multiplier to the full subtotal, optionally adds an express surcharge, and returns the fee in EUR rounded to 2 decimal places.

## Steps
1. **Caller assembles inputs** — weight_kg, zone (A/B/C), express (default False)
2. **Validate** — rejects negative weight or weight > 100 kg with ValueError
3. **Tiered weight cost** — 0–5 kg @ €1/kg, 5–20 kg @ €1.50/kg, >20 kg @ €2/kg; add BASE_RATE €5
4. **Zone multiplier** — multiply whole subtotal by A=1.0, B=1.5, C=2.5
5. **Express surcharge** — add €15 if express=True (flat, applied after zone)
6. **Return** — float rounded to 2dp

## Emotional Arc
Neutral → Confident. Caller receives a deterministic, reproducible number with no silent failure modes.

## Jobs Served
- JOB-01: Trusted AI-assisted workflow
- JOB-02: TDD on real code (tiered pricing is the realistic domain problem)
