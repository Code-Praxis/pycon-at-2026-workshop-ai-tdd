# DESIGN Decisions — shipping-costs

## Key Decisions
- [D1] Application scope only: pure Python module with no infrastructure — system and domain scopes not applicable (see: brief.md)
- [D2] Guide interaction mode: instructor confirmed quality attribute ranking and paradigm choice interactively
- [D3] No ports-and-adapters: pure function has no I/O boundary to invert — ceremony without testability benefit in workshop context (see: brief.md, adr-002)
- [D4] FP paradigm: existing code is already functional; formalised in CLAUDE.md (see: adr-002-functional-paradigm.md)
- [D5] Acceptance/unit split: separate directories enforce the ATDD/unit distinction the workshop teaches (see: adr-001-test-structure.md)

## Architecture Summary
- Pattern: Pure-core module, flat structure, separated test layers
- Paradigm: Functional Python
- Key components: `calculate_delivery_fee` (canonical), `calculate_weight_cost` (unit-testable helper), `calculate_shipping_costs` (teaching foil, no tests)

## Reuse Analysis
| Existing Component | File | Overlap | Decision | Justification |
|---|---|---|---|---|
| `calculate_delivery_fee` | `src/shipping_costs/__init__.py` | Canonical fee function | EXTEND (tests) | Complete; DESIGN adds coverage only |
| `calculate_weight_cost` | `src/shipping_costs/__init__.py` | Weight tier helper | EXTEND (unit tests) | Is the unit under test |
| `calculate_shipping_costs` | `src/shipping_costs/__init__.py` | Alternative impl | NO ACTION | Teaching foil per A5 |
| `Zone` enum | `src/shipping_costs/__init__.py` | Type-safe zone param | REUSE as-is | Correct and complete |

## Technology Stack
- Python 3.11: existing constraint (pyproject.toml)
- pytest: test runner
- ruff: linting + formatting
- ty: type checking
- uv: package management

## Constraints Established
- Acceptance tests import only `calculate_delivery_fee` and `Zone` — never internal helpers
- Unit tests may import `calculate_weight_cost` directly
- All functions must be pure (no side effects, no I/O)
- Type annotations required on all public functions

## Upstream Changes
- Two calculation errors found in DISCUSS artifacts — see `design/upstream-changes.md`
