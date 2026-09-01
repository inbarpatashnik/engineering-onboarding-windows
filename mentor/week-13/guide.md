# Mentor guide — Week 13: Capstone Incident

> Restricted: contains review guidance and hidden assessment details.

## Review intent

The student should demonstrate: lead a clear evidence-based incident review. Focus the review on triage order, hypothesis updates, mitigation safety, communication. Do not reward extra architecture that lacks evidence, and do not operate or repair the normal environment for the student.

## Suggested review sequence

1. Ask the student to state the acceptance criteria and current risk.
2. Ask the student to independently start and smoke-test the environment while narrating their model.
3. Review the student's visible practice case and custom case before offering help.
4. Ask for a five-minute implementation demo.
5. Optionally choose one hidden failure from the mentor controls and observe diagnosis.
6. Review tests and one design decision, then score with `curriculum\assessment_rubric.md`.

## Progressive hints

- **Hint 1:** Ask which boundary owns the observed behavior.
- **Hint 2:** Ask for a request ID and compare client/server timing.
- **Hint 3:** Ask what the student learned from `/api/state`, container status, and logs.
- **Hint 4:** Ask the student to reset the visible case, reproduce one variable at a time, and compare evidence.

## Hidden checks

- The student can start, inspect, exercise, and reset the environment without mentor action.
- A timeout or 503 does not trigger an unbounded retry loop.
- Duplicate requests/events do not corrupt state.
- Logs omit authorization values and secrets.
- The custom case is deterministic and teaches a subject-specific behavior.

## Red flags

Waiting for the mentor to operate scripts, global exception swallowing, sleeps used as synchronization, destructive recovery as the first option, tests coupled to execution order, or confident claims without measurements. Do not score PowerShell syntax or Windows administration.

## Optional hidden fault exercise

Only after the student independently passes the baseline, visible case, and custom-case work, optionally run:

```powershell
+.\training-platform\mentor\set-fault.ps1 -Preset week-13
+```

Expected injected behavior is recorded in `training-platform\mentor\incident-presets\week-13.json`. Ask the student to diagnose before revealing it. Finish with `.\training-platform\mentor\reset-faults.ps1`.

## Pass evidence

A pass requires independent environment operation, appropriate tests, a meaningful student-created case, bounded failure behavior, and a clear explanation of tradeoffs. Capture one observation and one next step in the review record.
