# Week 1: Advanced Git, Reproducible Verification, and CI Foundations

## Outcome

Recover repository state and explain why automated verification differs from a developer machine.

## Week learning pack

1. [Learning guide](learning-guide.md) — sequence and daily navigation
2. [Source guide](source-guide.md) — readings, workshops, and note prompts
3. [Exercise 1: source notes](exercises/01-source-notes.md)
4. [Exercise 2: small practice](exercises/02-small-practice.md)
5. [Exercise 3: environment lab](exercises/03-environment-lab.md)
6. [Exercise 4: project and custom case](exercises/04-project-and-custom-case.md)
7. [Exercise 5: weekly synthesis](exercises/05-weekly-synthesis.md)
8. [Deliverables checklist](deliverables-checklist.md)

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

## Required learning sources — Sunday, about 4 hours

- [Pro Git: Debugging with Git](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git) — suggested 40 min
- [Git bisect reference](https://git-scm.com/docs/git-bisect) — suggested 30 min
- [Pro Git: Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified) — suggested 45 min
- [Git reflog reference](https://git-scm.com/docs/git-reflog) — suggested 25 min
- [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) — suggested 45 min
- [Reproducible Builds documentation](https://reproducible-builds.org/docs/) — suggested 30 min

Follow relevant linked subsections and take working notes. Answer: what problem does this solve, which assumption can fail, and which observable signal would reveal failure? Topics this week: Git commit graphs, bisect, reflog recovery, conflict resolution, reviewable history, clean-room verification, CI stages and failure propagation.

## Sunday — foundations and first contact (8 hours)

- Weekly planning, prior-week follow-up, and acceptance criteria — 1 hour.
- Advanced Git and CI readings with concept notes — 3.5 hours.
- Provider-neutral interactive Git workshop — 1.5 hours.
- Create the disposable repository and map its graph — 1.5 hours.
- Predictions, questions, and end-of-day summary — 1.5 hours.

From the repository root, independently run:

```powershell
.\training-platform\student\setup-week01-git-lab.ps1
Set-Location .\student-work\week-01-git-lab
git log --graph --decorate --oneline --all
```

Identify the known-good tag, regression range, divergent branches, and messy-history branch without reading the fixture generator. Predict which evidence will support bisect, recovery, and conflict work.

## Monday — guided practice and visible case (8 hours)

1. **Use git bisect to identify the exact commit that introduced a regression** — suggested 1.5 hours.
2. **Recover deleted or rewritten work with reflog and explain which objects were still reachable** — suggested 1.5 hours.
3. **Resolve a conflicting rebase, then restructure a messy branch into reviewable commits without losing behavior** — suggested 1.5 hours.

Use roughly 1.5 hours for each remaining guided exercise, 2 hours for the prepared case, 1.5 hours for investigation/evidence, and 1.5 hours for review and refinement. Run:

```powershell
.\training-platform\student\setup-week01-git-lab.ps1
```

Use the disposable repository for bisect, reflog recovery, conflict resolution, and history-cleanup labs. Recreate it under a new output path when a clean baseline is needed; the setup script never overwrites work.

## Tuesday — design and main implementation (8 hours)

**Build a provider-neutral local verification pipeline and diagnose a regression.** Use the simulator at `http://localhost:8080`. Suggested allocation: design and interfaces 1.5 hours; first vertical slice 4.5 hours; initial automated tests and review 2 hours. Preserve request IDs and other evidence. Use portable path APIs such as `pathlib.Path`; copying supplied PowerShell commands is sufficient.

## Wednesday — implementation, cases, and failure testing (8 hours)

Suggested allocation: complete/refactor the implementation 3 hours; design and create a deterministic custom case 2 hours; failure and recovery tests 2 hours; evidence and code-quality pass 1 hour.

```powershell
.\scripts\verify.ps1
# Then repeat from a fresh clone or disposable copy
```

Reproduce at least three clean-runner failures: hidden/untracked input, order or state leakage, and an undeclared dependency or environment assumption. Document the hypothesis, signal, correction, exit code, cleanup, and regression test.

## Thursday — handoff, review, and remediation (8 hours)

- Fresh-session reproduction and full automated test run — 2 hours.
- Runbook, decisions, evidence, and reflection — 2 hours.
- Student-led demonstration and mentor challenge/review — 1.5 hours.
- Apply review feedback or complete a bounded remediation — 1.5 hours.
- Final cleanup, submission, and next-week preparation — 1 hour.

The student operates the environment during review. The mentor reviews evidence, challenges reasoning, and may introduce a hidden scenario; the mentor does not activate the normal exercise.

## Before asking the mentor for operational help

1. Re-run the failing verification or Git operation and copy the exact command.
2. Record expected versus actual graph, commit, file state, and exit code.
3. Inspect `git status`, `git log --graph --all`, `git diff`, and `git reflog` as relevant.
4. Recreate the disposable lab under a new path when a clean baseline is needed; never overwrite evidence.
5. Try one controlled experiment and record the result.
6. Ask a focused question containing evidence and what you already tried.

## Deliverables

- Working source and dependency lock/requirements file
- Automated tests and a one-command test instruction
- Git incident evidence: bisect result, reflog recovery, conflict rationale, and cleaned history
- Provider-neutral verification command and machine-readable result artifact
- `DECISIONS.md` with assumptions and one rejected alternative
- `RUNBOOK.md` with start, verify, diagnose, stop, and recover steps
- `EVIDENCE.md` with sanitized results and conclusions
- Thursday demonstration and review notes

## Definition of done

- You independently created, inspected, exercised, and recovered the Git lab.
- The provider-neutral verification command passes from a clean checkout.
- Another engineer can reproduce the work using the supplied commands.
- Failure behavior is bounded and tested.
- No secrets, absolute user paths, or production data are committed.
- You can explain the implementation and the case you designed.

## Reflection

What did operating or changing the environment teach you about the subject? Which signal was most useful? What would you redesign with more time?
