# Week 9: Reliability Patterns

## Outcome

Avoid retry storms and bound failure impact.

## Timebox and prerequisites

Plan 8–10 hours. Complete the preceding week, run `..\..\training-platform\scripts\start-week.ps1 -Week 9`, then run the matching smoke test.

## Study prompts

Topics: timeouts, retries, backoff, circuit breakers, bulkheads. For each topic, write one paragraph answering: what problem does it solve, what assumption can fail, and what observable signal reveals failure? Prefer official documentation for language, protocol, database, and tool behavior.

## Assignment

**Harden a flaky dependency integration.** Use the simulator at `http://localhost:8080`. Begin by calling `/health`, `/api/resources`, and `/api/dependency`. Store paths with `pathlib.Path`; never concatenate Windows paths by hand. Commands shown in your runbook must be PowerShell commands.

## Required work

1. Write acceptance criteria before implementation.
2. Implement the smallest useful vertical slice.
3. Add automated tests for the happy path and at least three failures.
4. Capture structured evidence: request IDs, timings, test output, or query plans as appropriate.
5. Document one rejected alternative and why.
6. Demonstrate clean setup on a fresh PowerShell session.

## Investigation prompts

- Which behavior is guaranteed by your code, and which depends on the environment?
- What happens on timeout, duplicate input, malformed data, restart, and partial completion?
- How would an operator detect and safely recover from failure?
- What data must never appear in logs?

## Deliverables

- Working source and dependency lock/requirements file
- Automated tests and a one-command test instruction
- `DECISIONS.md` with assumptions and tradeoffs
- `RUNBOOK.md` with start, verify, diagnose, stop, and recover steps
- `EVIDENCE.md` with sanitized command output and conclusions

## Definition of done

- The environment smoke test passes before and after the demo.
- Another engineer can reproduce the work on Windows from the runbook.
- Failure behavior is bounded and tested.
- No secrets, absolute user paths, or production data are committed.
- You can explain the implementation without reading the code line by line.

## Reflection

What changed in your mental model? Which signal was most useful? What would you redesign with twice the time?
