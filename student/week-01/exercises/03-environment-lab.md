# Exercise 3: environment lab and visible case

**Time:** 4 hours across Sunday and Monday  
**Objective:** Learn Git, Python project environments, evidence-driven debugging, independent learning habits by operating and observing the supplied environment.

## Baseline

```powershell
.\training-platform\scripts\start-week.ps1 -Week 1
.\training-platform\scripts\smoke-test.ps1 -Week 1
```

Map active services, ports, health checks, volumes, `/api/state`, and relevant logs. Draw a small request/data flow and identify where state persists.

## Prepared case

Read `training-platform/student/cases/week-01-practice.json`. Without running it, predict status, latency/parsing behavior, state, logs, and recovery. Then run:

```powershell
.\training-platform\student\run-case.ps1 -Case week-01-practice
```

Perform at least five repeated observations. Explain stable versus variable behavior. Reset the case and prove recovery:

```powershell
.\training-platform\student\reset-case.ps1
.\training-platform\scripts\smoke-test.ps1 -Week 1
```

## Expected observations

- Baseline health remains distinguishable from dependency behavior.
- Requests carry identifiers that connect client evidence and logs.
- The case creates the behavior described in its JSON without corrupting source files.
- Reset restores normal dependency behavior without deleting student work.

## Self-check and hints

- If evidence is inconsistent, check whether the case uses a failure rate and collect more samples.
- If the API is unreachable, inspect container status before changing code.
- If reset appears ineffective, query `/api/state` and repeat with a new request ID.

## Done when

`EVIDENCE.md` contains the system map, predictions, repeated observations, explanation, recovery proof, and one automated assertion.
