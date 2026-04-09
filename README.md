# Vibe Coding with Guard Rails Workshop

Welcome to the workshop! This project demonstrates how to practice "vibe coding" (high-velocity, LLM-assisted development) while maintaining high quality through rigorous automated guard rails.

## Guard Rails in this Project

We use a combination of **TDD (Test-Driven Development)**, **ATDD (Acceptance Test-Driven Development)**, and static analysis to ensure our code remains correct even as we move fast.

### 1. ATDD (Acceptance Test-Driven Development)
- **Tool**: `pytest`
- **Location**: `tests/acceptance/`
- **Workflow**: Define behavioral requirements in high-level `pytest` tests before writing any code.

### 2. TDD (Test-Driven Development)
- **Tool**: `pytest`
- **Location**: `tests/unit/`
- **Workflow**: Write small, focused unit tests for individual functions and logic components.

### 3. Static Analysis & Linting
- **Ruff**: Fast Python linter and formatter.
- **Mypy**: Static type checker to catch type errors before they happen.

---

## Getting Started

### Installation

We use `uv` for lightning-fast package management.

```bash
uv pip install -e ".[dev]"
```

### Running Tests

Run all tests (Unit + Acceptance):

```bash
pytest
```

### Running Guard Rails

Check for linting and type errors:

```bash
# Linting
ruff check .

# Formatting
ruff format .

# Type checking
mypy src
```

## Workshop Workflow (The "Vibe")

1. **Vibe**: Describe the feature in an acceptance test in `tests/acceptance/`.
2. **Fail**: Run `pytest` and see the test fail.
3. **Vibe**: Let the LLM generate the unit tests and the implementation.
4. **Pass**: Run `pytest` until everything is green.
5. **Enforce**: Run `ruff` and `mypy` to ensure the "vibe" didn't introduce messy code or type bugs.
