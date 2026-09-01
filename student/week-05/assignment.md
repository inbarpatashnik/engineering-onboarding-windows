# Week 5: Caching and Concurrency

## Outcome

Demonstrate correctness under concurrent requests.

## Weekly rhythm: Sunday–Thursday, approximately 40 hours

This plan assumes five ordinary eight-hour workdays. Adjust for holidays, organizational events, or approved leave; the mentor should reduce scope rather than expect hidden overtime. Breaks and normal team ceremonies are included within each day.

| Day | Focus | Suggested allocation |
|---|---|---:|
| Sunday | Sources, concept notes, environment orientation, first guided exercise | 8 hours |
| Monday | Remaining guided exercises, environment inspection, visible practice case | 8 hours |
| Tuesday | Design and main implementation | 8 hours |
| Wednesday | Complete implementation, custom cases, failure testing, refactoring | 8 hours |
| Thursday | Reproduction, documentation, mentor review, feedback and remediation | 8 hours |
| **Total** |  | **40 hours** |

The allocations below are guidance, not speed targets. Record blockers early. If the week is shortened, agree explicitly which stretch items or cases are removed.

## Required learning sources — Sunday, about 2 hours

- [Redis developer quick starts](https://redis.io/docs/latest/develop/get-started/) — suggested 40 min
- [Redis client-side caching](https://redis.io/docs/latest/develop/clients/client-side-caching/) — suggested 35 min

Follow relevant linked subsections and take working notes. Answer: what problem does this solve, which assumption can fail, and which observable signal would reveal failure? Topics this week: Redis patterns, race conditions, idempotency, locking.

## Sunday — foundations and first contact (8 hours)

- Weekly planning, prior-week follow-up, and acceptance criteria — 1 hour.
- Required sources and concept notes — 2 hours.
- Independently start, smoke-test, and map the environment — 2 hours.
- Guided exercise 1 — 1.5 hours.
- Evidence, questions, and end-of-day summary — 1.5 hours.

From the repository root, independently run:

```powershell
.\training-platform\scripts\start-week.ps1 -Week 5
.\training-platform\scripts\smoke-test.ps1 -Week 5
```

Inspect `/health`, `/api/resources`, `/api/dependency`, `/api/state`, active containers, logs, and persistent volumes. You are assessed on the system model and evidence—not PowerShell syntax or Windows administration.

## Monday — guided practice and visible case (8 hours)

1. **Measure cache hit and miss behavior** — suggested 1.5 hours.
2. **Create stale-data and stampede cases** — suggested 1.5 hours.
3. **Demonstrate an atomic update under concurrent requests** — suggested 1.5 hours.

Use roughly 1.5 hours for each remaining guided exercise, 2 hours for the prepared case, 1.5 hours for investigation/evidence, and 1.5 hours for review and refinement. Run:

```powershell
.\training-platform\student\run-case.ps1 -Case week-05-practice
```

State the expected behavior before running it. Collect signals, explain recovery, and reset with `.\training-platform\student\reset-case.ps1`.

## Tuesday — design and main implementation (8 hours)

**Add safe caching to the catalog client.** Use the simulator at `http://localhost:8080`. Suggested allocation: design and interfaces 1.5 hours; first vertical slice 4.5 hours; initial automated tests and review 2 hours. Preserve request IDs and other evidence. Use portable path APIs such as `pathlib.Path`; copying supplied PowerShell commands is sufficient.

## Wednesday — implementation, cases, and failure testing (8 hours)

Suggested allocation: complete/refactor the implementation 3 hours; design and create a deterministic custom case 2 hours; failure and recovery tests 2 hours; evidence and code-quality pass 1 hour.

```powershell
.\training-platform\student\new-case.ps1 -Name my-week-05-case -Mode delay -DelayMs 700
.\training-platform\student\run-case.ps1 -Case my-week-05-case
```

Describe the hypothesis, expected signal, safe recovery, and automated assertion. Test the happy path and at least three failures, including the custom case.

## Thursday — handoff, review, and remediation (8 hours)

- Fresh-session reproduction and full automated test run — 2 hours.
- Runbook, decisions, evidence, and reflection — 2 hours.
- Student-led demonstration and mentor challenge/review — 1.5 hours.
- Apply review feedback or complete a bounded remediation — 1.5 hours.
- Final cleanup, submission, and next-week preparation — 1 hour.

The student operates the environment during review. The mentor reviews evidence, challenges reasoning, and may introduce a hidden scenario; the mentor does not activate the normal exercise.

## Before asking the mentor for operational help

1. Re-run the smoke test and copy the exact failing command.
2. Record expected versus actual behavior and the request ID/time.
3. Inspect container status and relevant logs.
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
- Thursday demonstration and review notes

## Definition of done

- You independently started, inspected, exercised, and reset the environment.
- The smoke test passes before and after the work.
- Another engineer can reproduce the work using the supplied commands.
- Failure behavior is bounded and tested.
- No secrets, absolute user paths, or production data are committed.
- You can explain the implementation and the case you designed.

## Reflection

What did operating or changing the environment teach you about the subject? Which signal was most useful? What would you redesign with more time?
