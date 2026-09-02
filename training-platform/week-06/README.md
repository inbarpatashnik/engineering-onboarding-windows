# Week 6 local Kafka client lab

This lab uses the official Apache Kafka Docker image as a disposable dependency. The broker exists only so you can observe application-client behavior. Do not tune or administer it.

## Timebox

Allow at most 30 minutes for the first image pull and startup and at most two controlled attempts. If readiness still fails, run `diagnose.ps1`, save its output, and continue with `fallback-client-lab.py`. Return to the small Kafka integration suite later when a broker is available.

## Start and verify

```powershell
.\training-platform\scripts\start-week.ps1 -Week 6
.\training-platform\week-06\check-kafka.ps1
```

The check creates `ownership-events` with three partitions, publishes a short keyed batch, consumes it, and prints record metadata. It may recreate only this training topic.

## Client experiments

Use `localhost:19092` as the bootstrap address. Prefer your project's normal Kafka client library. Keep broker-dependent tests tagged as integration tests; client decision logic must remain testable with a fake.

For CLI-based observation without installing another desktop tool:

```powershell
.\training-platform\week-06\produce-samples.ps1
.\training-platform\week-06\consume-samples.ps1 -Group student-week06 -MaxMessages 6
```

Run a second consumer with the same group, then a different group. Restart, inspect committed offsets, and replay using a new group. The scripts are scaffolding: your submitted producer and consumer must expose delivery, validation, idempotency, commit, and shutdown behavior in application code.

## Fallback when Kafka is unavailable

```powershell
.\training-platform\week-06\diagnose.ps1
.\.venv\Scripts\python.exe .\training-platform\week-06\fallback-client-lab.py
```

The fallback exercises partition ordering, polling, commits, restart, replay, duplicates, and poison events in memory. It is not Kafka integration evidence. Record that limitation and continue building unit-testable client behavior.

## Stop

```powershell
.\training-platform\scripts\stop-week.ps1 -Week 6
```
