# Mentor guide — Week 6: Events and Messaging

> Restricted: contains review guidance and intervention details.

## Review intent

The student should demonstrate: recover from duplicates and poison messages. Focus the review on consumer offsets, idempotency keys, schema evolution, dead letters. Do not reward extra architecture that lacks evidence.

## Suggested review sequence

1. Ask the student to state the acceptance criteria and current risk.
2. Run the baseline smoke test together.
3. Ask for a five-minute demo with no narration from notes.
4. Choose one failure condition from the mentor controls and observe diagnosis.
5. Review tests and one design decision.
6. Score with `curriculum\assessment_rubric.md` and agree remediation if needed.

## Progressive hints

- **Hint 1:** Ask which boundary owns the observed behavior.
- **Hint 2:** Ask for a request ID and compare client/server timing.
- **Hint 3:** Point to `/api/state` and the simulator logs.
- **Hint 4:** Reset the environment, reproduce one variable at a time, and compare evidence.

## Hidden checks

- Paths and commands work from a directory containing spaces.
- A timeout or 503 does not trigger an unbounded retry loop.
- Duplicate requests/events do not corrupt state.
- Logs omit authorization values and secrets.
- The runbook distinguishes stop, reset, and destructive cleanup.

## Red flags

Global exception swallowing, sleeps used as synchronization, hard-coded `C:\Users` paths, destructive recovery as the first option, tests coupled to execution order, or confident claims without measurements.

## Fault exercise

After baseline success, run:

```powershell
+.\training-platform\mentor\set-fault.ps1 -Preset week-06
+```

Expected injected behavior is recorded in `training-platform\mentor\incident-presets\week-06.json`. Ask the student to diagnose before revealing it. Finish with `.\training-platform\mentor\reset-faults.ps1`.

## Pass evidence

A pass requires reproducible Windows instructions, appropriate tests, bounded failure behavior, and a clear explanation of tradeoffs. Capture one quote-sized observation and one next step in the review record.
