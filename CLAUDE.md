# CLAUDE.md

## Development Paradigm

This project follows the **functional programming** paradigm. Use @nw-functional-software-crafter for implementation.

## Project Context

PyCon Austria 2026 workshop — "Vibe Coding with Guard Rails". Demonstrates LLM-assisted development with TDD/ATDD quality gates.

## Quality Gates (run before marking any work done)

```bash
pytest                # all tests must pass
ruff check .          # zero linting violations
ruff format .         # code formatted
ty check src          # zero type errors
```
