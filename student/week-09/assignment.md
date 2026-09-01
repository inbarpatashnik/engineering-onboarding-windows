# Week 9: Reliability Patterns

## Outcome

Avoid retry storms and bound failure impact.

## Suggested 10-hour plan

| Work | Suggested time |
|---|---:|
| Required learning sources and notes | 1.5 hours |
| Start, inspect, and understand the week's environment | 0.5 hour |
| Three guided exercises | 2 hours |
| Main implementation | 3 hours |
| Create cases, test failures, and collect evidence | 1.5 hours |
| Runbook, decisions, and reflection | 1 hour |
| Buffer | 0.5 hour |
| **Total** | **10 hours** |

The times are guidance, not performance targets. If a source takes longer, record what was difficult instead of silently skipping it.

## Required learning sources

- [AWS Builders' Library: timeouts, retries and backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — suggested 60 min
- [Azure retry pattern](https://learn.microsoft.com/azure/architecture/patterns/retry) — suggested 30 min

While reading, answer: what problem does this solve, which assumption can fail, and which observable signal would reveal failure? Topics this week: timeouts, retries, backoff, circuit breakers, bulkheads.

## Own the environment — 30 minutes

From the repository root, independently run:

```powershell
.\training-platform\scripts\start-week.ps1 -Week 9
.\training-platform\scripts\smoke-test.ps1 -Week 9
```

Inspect `/health`, `/api/resources`, `/api/dependency`, `/api/state`, and the container logs. Explain which components and persistent volumes are active. You are expected to operate and reason about the environment; you are not assessed on PowerShell syntax or Windows administration.

## Guided exercises — 2 hours

1. **Measure a timeout budget across retries** — 40 minutes.
2. **Compare fixed delay with jittered backoff** — 40 minutes.
3. **Create a dependency recovery case and observe circuit state** — 40 minutes.

For the visible case for this week, run:

```powershell
.\training-platform\student\run-case.ps1 -Case week-09-practice
```

Reset visible cases with `.\training-platform\student\reset-case.ps1`.

## Main assignment — 3 hours

**Harden a flaky dependency integration.** Use the simulator at `http://localhost:8080`. Write acceptance criteria first, implement the smallest useful vertical slice, and preserve request IDs and other evidence. Use portable path APIs such as `pathlib.Path`; copying the supplied PowerShell commands is sufficient.

## Create your own case — 1.5 hours

Create a new deterministic case instead of changing mentor files:

```powershell
.\training-platform\student\new-case.ps1 -Name my-week-09-case -Mode delay -DelayMs 700
.\training-platform\student\run-case.ps1 -Case my-week-09-case
```

Describe the hypothesis, expected signal, safe recovery, and automated assertion. Add tests for the happy path and at least three failures, including your case.

## Before asking the mentor

1. Re-run the smoke test and copy the exact failing command.
2. Record expected versus actual behavior and the request ID/time.
3. Inspect `docker compose ps` and relevant logs.
4. Reset only the visible case; do not delete volumes unless data reset is the hypothesis.
5. Try one controlled experiment and record the result.
6. Ask a focused question containing evidence and what you already tried.

## Deliverables

- Working source and dependency lock/requirements file
- Automated tests and a one-command test instruction
- Your custom case JSON under `training-platform/student/cases/custom/`
- `DECISIONS.md` with assumptions and one rejected alternative
- `RUNBOOK.md` with start, verify, diagnose, stop, and recover steps
- `EVIDENCE.md` with sanitized results and conclusions

## Definition of done

- You independently started, inspected, exercised, and reset the environment.
- The smoke test passes before and after the work.
- Another engineer can reproduce the work using the supplied commands.
- Failure behavior is bounded and tested.
- No secrets, absolute user paths, or production data are committed.
- You can explain the implementation and the case you designed.

## Reflection

What did operating or changing the environment teach you about the subject? Which signal was most useful? What would you redesign with twice the time?
