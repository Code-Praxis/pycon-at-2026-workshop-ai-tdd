# JTBD Four Forces Analysis
## Feature: PyCon Austria 2026 Workshop — Vibe Coding with Guard Rails
**Date**: 2026-04-17

The Four Forces explain why someone "hires" a product (switch toward) or stays with the status quo (stay away). Applied here to model workshop attendance motivation and the risk of non-adoption or early dropout.

---

## Forces for JOB-01: Gain a Trusted, Repeatable AI-Assisted Workflow

### Push (Situation-based — what's frustrating the status quo)

| # | Push Force | Evidence |
|---|-----------|---------|
| P1 | LLM-generated code ships without tests → debugging takes 3–5x longer (P1 from problem-validation) | "I let the AI generate the whole thing and it looked fine, but then it broke something I didn't expect" |
| P2 | No team-level consensus on AI workflow → every developer invents their own | "My team is worried about quality. Nobody has shown us a workflow that actually works." |
| P3 | AI-generated code fails code review ("no tests, no merge") → slows velocity, defeats the purpose | Senior devs rejecting PRs, junior devs uncertain about trust |

### Pull (Attraction — what the new solution promises)

| # | Pull Force | What the Workshop Delivers |
|---|-----------|--------------------------|
| R1 | A concrete, reproducible loop: describe → test RED → LLM generate → GREEN → enforce | The 5-step workflow in the README, demonstrable in 90 minutes |
| R2 | Take-home artifact: the workflow is documented in code form in a repo they keep | Attendees clone and keep the repo |
| R3 | Reference to show the team: "we tried this at PyCon, here's the evidence it works" | Observable test output, ruff/ty passing |

### Anxiety (Demand-reducing — fears about adopting the new solution)

| # | Anxiety | Mitigation in Workshop Design |
|---|---------|-------------------------------|
| A1 | "What if this doesn't work for my domain? Shipping costs is too simple." | The dual-implementation contrast intentionally adds real complexity: zone multipliers, express surcharge, boundary weight tiers |
| A2 | "What if my LLM generates wrong tests and I don't notice?" | ATDD acceptance test is written by the human first — LLM only generates unit tests under that umbrella |
| A3 | "What if 90 minutes is not enough to internalize this?" (A3 from assumptions) | The loop is short-cycle by design; attendees complete it 2–3 times during the session |
| A4 | "What if my environment doesn't work?" (A4 from assumptions) | Pre-workshop setup guide + smoke test command = confidence before entering the loop |

### Habit (Inertia — what keeps attendees in the old workflow)

| # | Habit | Counter-Strategy |
|---|-------|-----------------|
| H1 | Writing tests after code ("I already see the function, I'll just test it now") | Workshop starts with acceptance test BEFORE any implementation is visible |
| H2 | Trusting LLM output without running static analysis | `ruff check` and `ty check` are the last gate before "done" — made explicit in the loop |
| H3 | Skipping unit tests when acceptance test is green | US-03 explicitly covers the unit test layer as a separate discipline |
| H4 | Using LLM interactively (paste function, fix inline) | Workshop uses the structured loop — LLM called at a specific step with a specific prompt |

---

## Forces for JOB-02: Discover Why TDD Actually Helps on Real Code

### Push
- Existing TDD resources use FizzBuzz/Stack/Calculator — not relatable to production code (P2)
- Attendees leave generic TDD workshops unable to apply the skill the following Monday

### Pull
- Shipping costs domain has real edge cases: tiered pricing breakpoints, zone multiplier interaction, express surcharge stacking
- The dual-implementation contrast creates a natural "which one is correct?" discovery moment that only tests can answer

### Anxiety
- "I'll fall behind the group because I'm not fast with pytest" — mitigated by scaffolded exercises
- "I'll be shown theory I already know" — mitigated by hands-on, code-from-scratch format

### Habit
- Reading through the code to judge correctness instead of running tests
- Manually running the demo script to spot-check instead of writing a structured test

---

## Forces for JOB-03: Get Environment Ready Without Losing Workshop Time

### Push
- Conference workshop time is scarce (90 minutes); losing even 15 minutes to setup failure is catastrophic for learning
- Python environment setup is notoriously fragile: Python version conflicts, missing system dependencies, pip vs. uv confusion

### Pull
- Single-command install: `uv pip install -e ".[dev]"` — no per-tool installation needed
- Pre-workshop setup guide distributed before the conference session

### Anxiety
- "I'm using Windows and things work differently" (uv handles this well, but anxiety remains)
- "I'm on my work machine and IT has restricted global installs" — mitigated by uv's isolated environments

### Habit
- Attendees arrive and wait to set up until they're in the room — instead of following the pre-conference guide

---

## Forces for JOB-04: Understand the Line Between Acceptance Tests and Unit Tests

### Push
- Test suites that break on every refactor create the belief that "tests slow you down" (P5)
- LLM-generated code changes internal structure; tests coupled to internals break silently

### Pull
- The dual-implementation contrast is the perfect teaching artifact: both implementations produce the same acceptance-test-visible behaviour, but different internal structures
- Attendees can run both implementations against the same acceptance test and see that both pass

### Anxiety
- "I don't know what 'outside-in' means well enough to write an acceptance test" — pre-scaffolded acceptance test structure provided
- "My unit tests will be too implementation-specific and I won't realize it until the refactor"

### Habit
- Writing tests after implementation (the test mirrors the code structure, not the behaviour)
- Treating all tests the same: one `tests/` folder, no distinction between acceptance and unit

---

## Four-Forces Summary Heat Map

| Job | Push Strength | Pull Strength | Anxiety Level | Habit Resistance | Net Switch Probability |
|-----|:---:|:---:|:---:|:---:|:---:|
| JOB-01: Trusted AI workflow | HIGH | HIGH | MEDIUM | MEDIUM | HIGH |
| JOB-02: TDD on real code | HIGH | HIGH | LOW | LOW | HIGH |
| JOB-03: Environment setup | MEDIUM | MEDIUM | HIGH | LOW | MEDIUM |
| JOB-04: ATDD/unit distinction | MEDIUM | HIGH | MEDIUM | HIGH | MEDIUM-HIGH |

**Implication**: JOB-01 and JOB-02 have the strongest switch probability — the workshop should maximize time on these. JOB-03 must be solved before the session starts (pre-workshop) to avoid it consuming force from JOB-01. JOB-04 is addressed structurally through the dual-implementation design.
