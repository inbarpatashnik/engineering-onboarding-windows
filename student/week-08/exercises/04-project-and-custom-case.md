# Exercise 4: main project and custom case

**Time:** 16 hours across Tuesday and Wednesday  
**Project:** Instrument a request path  
**Exit capability:** Diagnose latency using correlated telemetry.

## Acceptance criteria

1. Define inputs, outputs, invariants, and explicit non-goals.
2. Implement a reviewable vertical slice before adding breadth.
3. Preserve correlation evidence and fail clearly on invalid inputs.
4. Test the happy path, three failures, restart/recovery where relevant, and the custom case.
5. Document one rejected alternative and its tradeoff.

## Custom-case design

Choose `delay`, `unavailable`, or `malformed` only as a starting mechanism. Make the case subject-specific through the hypothesis, workload, expected signal, client behavior, and assertion.

```powershell
.\training-platform\student\new-case.ps1 -Name my-week-08-case -Mode delay -DelayMs 700 -LearningGoal "Replace with the specific concept being tested"
.\training-platform\student\run-case.ps1 -Case my-week-08-case
```

Edit the generated JSON to make the learning goal and expected signal precise. Never edit mentor presets.

## Review checkpoints

- Tuesday midday: acceptance criteria and interface sketch
- Tuesday end: vertical slice and initial tests
- Wednesday midday: custom case and failure matrix
- Wednesday end: complete tests, runbook, evidence, and clean smoke test

## Hints

- Reduce scope before adding abstractions.
- Turn every surprising observation into a minimal reproduction.
- A case is valuable when it can disprove an assumption, not merely make the system fail.

## Done when

Another student can clone, run, test, exercise, recover, and explain the project from your artifacts without mentor operation.
