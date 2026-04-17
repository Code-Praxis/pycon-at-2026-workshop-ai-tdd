# JTBD Job Stories
## Feature: PyCon Austria 2026 Workshop — Vibe Coding with Guard Rails
**Date**: 2026-04-17
**Grounded in**: `docs/feature/pycon-austria-2026-workshop/discover/problem-validation.md` (G1 PASSED)

---

## Context

The workshop product serves Python developers attending PyCon Austria 2026. The domain (shipping costs) is a teaching vehicle. The real deliverable is a reusable mental model: write tests → let AI generate → enforce quality gates → refactor safely.

Four jobs were identified from the discovery evidence. They are ranked by opportunity score (see `jtbd-opportunity-scores.md`).

---

## JOB-01 — Gain a Trusted, Repeatable AI-Assisted Workflow

**Job Story (primary)**

> When I am using an LLM to generate Python code for a real feature,
> I want to apply tests and quality gates before accepting the generated output,
> so I can ship fast without discovering broken behaviour two sprints later.

**Functional Dimension**
- Receive a step-by-step workflow that works with standard Python tooling (pytest, ruff, ty)
- Apply the workflow to a realistic, non-trivial problem (tiered pricing logic, conditional branches, edge cases)
- Verify that LLM-generated code passes all tests before committing

**Emotional Dimension**
- Feel in control when using the LLM — "the AI is my pair programmer, not my tech-debt dealer"
- Confidence that code quality will not silently degrade as velocity increases
- Satisfaction from seeing the full loop (RED → LLM → GREEN → ENFORCE) complete in one session

**Social Dimension**
- Have a reference workflow to show skeptical tech leads: "this is how we use LLMs responsibly"
- Be the person who brings a credible answer to the team's "how do we trust AI code?" question
- Leave PyCon with something demonstrable, not just a slide deck of principles

**JTBD-to-Story Bridge**
- US-01: Environment Setup — precondition for any job execution
- US-02: Write Failing Acceptance Test — establishes behavioral intent before LLM call
- US-03: LLM-Assisted Unit Test Generation — the velocity lever in the workflow
- US-04: LLM-Assisted Implementation Generation — the AI-generates step
- US-05: Quality Gate Enforcement — the trust layer (ruff, ty)
- US-06: Refactor with Confidence — the payoff: safe restructuring under test cover

---

## JOB-02 — Discover Why TDD Actually Helps on Real Code

**Job Story**

> When I have tried TDD tutorials before but found them unconvincing because examples were trivial,
> I want to see TDD applied to code with genuine edge cases and multiple code paths,
> so I can understand how test coverage changes my ability to refactor safely.

**Functional Dimension**
- Work through tiered pricing logic that has boundary conditions (weight tiers, zone multipliers, express surcharge)
- Write tests that fail in meaningful ways — not just "function exists" but "this specific edge case is wrong"
- Observe that the dual-implementation contrast reveals which implementation is correct through test execution

**Emotional Dimension**
- The "aha" moment: seeing a test catch a real discrepancy between the two implementations
- Frustration relief: "I finally see why people say tests make you faster, not slower"
- Intellectual engagement with a realistic domain problem rather than abstract counter examples

**Social Dimension**
- Return to their team with concrete evidence: "TDD made it safe to refactor this 50-line function"
- Be able to answer junior colleagues' question: "Is this function right? How do you know?"

**JTBD-to-Story Bridge**
- US-02: Write Failing Acceptance Test — makes the job visible
- US-03: LLM-Assisted Unit Test Generation — scales coverage without killing velocity
- US-06: Refactor with Confidence — the payoff scenario for this job

---

## JOB-03 — Get Environment Ready Without Losing 20 Minutes of Workshop Time

**Job Story**

> When I arrive at a hands-on workshop at a conference,
> I want to have a working Python environment with all dependencies already verified,
> so I can spend the 90 minutes learning the workflow instead of debugging installation issues.

**Functional Dimension**
- Clone repository and install dependencies with a single command (`uv pip install -e ".[dev]"`)
- Verify that pytest, ruff, and ty all run without errors before the workshop exercises begin
- Have a smoke test that confirms the environment is complete in under 2 minutes

**Emotional Dimension**
- Absence of the conference-workshop stress: "everyone else is coding, I'm still fixing pip"
- Quick confidence: first `pytest` run outputs something meaningful within 60 seconds of cloning

**Social Dimension**
- Not be the person blocking their table partner because of a broken environment

**JTBD-to-Story Bridge**
- US-01: Environment Setup + Pre-workshop Verification — directly serves this job

---

## JOB-04 — Understand the Line Between Acceptance Tests and Unit Tests

**Job Story**

> When I write tests for LLM-generated code and they break every time I refactor,
> I want to learn the distinction between acceptance tests (from outside, describe behaviour) and unit tests (isolated, describe implementation),
> so I can design test suites that survive internal refactoring.

**Functional Dimension**
- Write a high-level acceptance test that passes regardless of which of the two implementations is used
- Write unit tests that are coupled to implementation details (and understand why they break on refactor)
- Experience the difference directly: one suite stays green through refactor, the other goes red

**Emotional Dimension**
- The discomfort of watching unit tests fail during a "correct" refactor — then the relief of understanding why
- Curiosity: "wait, both implementations produce the same result for this input, but the test still passed?"

**Social Dimension**
- Be able to explain to a code reviewer why a test is written at the acceptance level vs. unit level

**JTBD-to-Story Bridge**
- US-02: Write Failing Acceptance Test — explicitly teaches the acceptance level
- US-03: LLM-Assisted Unit Test Generation — teaches the unit level by contrast
- US-06: Refactor with Confidence — the stress test where the distinction becomes tangible

---

## Personas

### Persona A: Karolina Nowak
**Role**: Mid-level Python developer, 4 years experience, Warsaw
**Context**: Uses GitHub Copilot daily, ships features fast, reviews AI-generated PRs with uncertainty
**Motivation**: Wants a workflow her team will actually adopt
**Anxiety**: "What if I follow this and my tech lead still rejects the AI-generated code?"
**Primary Jobs**: JOB-01, JOB-04

### Persona B: Tobias Gruber
**Role**: Senior Python developer, 8 years experience, Vienna
**Context**: Skeptical of LLMs, has been burned by AI-generated bugs in production
**Motivation**: Wants to understand LLM-assisted development well enough to evaluate it fairly
**Anxiety**: "I'm going to waste 90 minutes on something I don't believe in"
**Primary Jobs**: JOB-02, JOB-04

### Persona C: Ana Ferreira
**Role**: Junior developer, 1.5 years experience, Porto, attending first PyCon
**Context**: Knows pytest basics, has never done TDD deliberately, wants to level up
**Motivation**: Wants concrete practices she can bring back immediately
**Anxiety**: "Everyone else here knows more than me — I'll fall behind"
**Primary Jobs**: JOB-02, JOB-03
