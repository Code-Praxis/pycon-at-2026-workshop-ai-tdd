# ADR-002: Functional Programming Paradigm

**Date**: 2026-04-17
**Status**: Accepted
**Feature**: shipping-costs

## Context

Python is multi-paradigm. The existing `src/shipping_costs/__init__.py` is already written in a functional style: pure functions with no side effects, referential transparency, no mutable state. The question is whether to formalise this as a paradigm commitment or leave it implicit.

## Decision

Adopt functional programming as the project paradigm. Written to `CLAUDE.md`:

> This project follows the **functional programming** paradigm. Use @nw-functional-software-crafter for implementation.

Implementation guidelines:
- All domain logic as pure functions (same inputs → same outputs, no side effects)
- No classes that hold mutable state
- `Enum` and `dataclass` (immutable, frozen if needed) are acceptable FP-compatible constructs
- Business rules expressed as function composition, not inheritance hierarchies

## Alternatives Considered

1. **OOP** — would require wrapping pure functions in a class (`ShippingCalculator`), adding instantiation ceremony and `self` that adds no value for a stateless calculation. Rejected: adds boilerplate without improving testability or readability.
2. **Implicit (no declaration)** — leaves paradigm ambiguous; future contributors might introduce classes that break the pure-core invariant. Rejected: workshop needs a clear model to demonstrate.

## Consequences

- `@nw-functional-software-crafter` is the designated DELIVER agent
- New functions must be pure (no I/O, no global mutation)
- `calculate_shipping_costs` (teaching foil) remains as a `dataclass`-based alternative — acceptable because it is a teaching artifact, not production code
- Type annotations are required (enforced by `ty check`)
