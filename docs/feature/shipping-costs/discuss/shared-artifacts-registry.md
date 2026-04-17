# Shared Artifacts Registry
## Feature: shipping-costs
**Date**: 2026-04-17

Each artifact has exactly one source of truth. Any step that reads the artifact must consume the canonical version, not a copy.

| Artifact | Type | Source | Consumed By | Notes |
|----------|------|--------|-------------|-------|
| `weight_kg` | `float` | Caller (S1) | Validation (S2), Weight calculation (S3) | Kilograms; must satisfy 0 ≤ weight_kg ≤ 100.0 |
| `zone` | `Zone` (enum) | Caller (S1) | Zone multiplier lookup (S4) | Values: A, B, C. Type-safe via enum — invalid zone is a static error |
| `express` | `bool` | Caller (S1) | Express surcharge (S5) | Default: False |
| `fee` | `float` | Return step (S6) | Caller (display / persist) | EUR, rounded to 2 decimal places; only value the caller observes |

## Constants (single source of truth: `src/shipping_costs/__init__.py`)

| Constant | Value | Used In |
|----------|-------|---------|
| `BASE_RATE` | €5.00 | Step S3 |
| `EXPRESS_SURCHARGE` | €15.00 | Step S5 |
| `MAX_WEIGHT` | 100.0 kg | Step S2 |
| `_ZONE_MULTIPLIERS` | {A:1.0, B:1.5, C:2.5} | Step S4 |
