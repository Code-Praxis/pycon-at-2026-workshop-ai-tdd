# Vibe Coding with Guard Rails Workshop

Welcome to the workshop! This project demonstrates how to practice "vibe coding" (high-velocity, LLM-assisted development) while maintaining high quality through rigorous automated guard rails.

## Guard Rails in this Project

We use a combination of **TDD (Test-Driven Development)**, **ATDD (Acceptance Test-Driven Development)**, and static analysis to ensure our code remains correct even as we move fast.

### 1. Acceptance Testing
- **Tool**: `pytest`
- **Location**: `tests/features/`
- **Workflow**: Define behavioral requirements in high-level `pytest` tests before writing any code.

### 2. Static Analysis & Linting
- **Ruff**: Fast Python linter and formatter.
- **ty**: Static type checker to catch type errors before they happen.

---

## Getting Started

### Installation

We use `uv` for lightning-fast package management.

```bash
uv sync
```

### Running Tests

Run all tests:

```bash
uv run pytest
```

### Running Guard Rails

Check for linting and type errors:

```bash
# Linting
uv run ruff check src

# Type checking
uv run ty check
```

## Workshop Workflow

1. **Vibe**: Describe the feature in a test in `tests/features/`.
2. **Fail**: Run `uv run pytest` and see the test fail.
3. **Vibe**: Let the LLM generate the code.
4. **Pass**: Run `uv run pytest` until everything is green.
5. **Enforce**: Run `uv run ruff` and `uv run ty` to ensure the "vibe" didn't introduce messy code or type bugs.

## AI-Augmented Development with NWAVE

This project is configured to work with **NWAVE**, a specialized AI-augmented SDLC toolset that runs inside **Claude Code**. NWAVE structures development into several "waves" to ensure high-quality output.

### Using NWAVE Commands

If you have NWAVE installed in your Claude Code environment, you can use the following commands to guide your development:

- `/nw-buddy`: Ask for contextual advice on your next steps.
- `/nw-discuss "feature description"`: Define requirements and acceptance criteria.
- `/nw-design`: Explore and document architecture decisions.
- `/nw-distill`: Generate high-level acceptance tests (ATDD).
- `/nw-deliver`: Implement the feature using TDD.

### Workflow with NWAVE

1. **Initialize**: Run `/nw-buddy` to get an overview of the project.
2. **Requirement Analysis**: Use `/nw-discuss` to clarify what you want to build.
3. **Design**: Use `/nw-design` to plan the implementation.
4. **Testing**: Use `/nw-distill` to create tests in `tests/features/`.
5. **Implementation**: Use `/nw-deliver` to generate the code that passes the tests.
