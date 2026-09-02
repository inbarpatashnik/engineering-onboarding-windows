# Exercise 3: disposable local Kafka lab

Follow `training-platform\week-06\README.md`. Docker Desktop and the official Apache Kafka image provide the broker; the provided PowerShell scripts start, verify, and stop it.

## Troubleshooting budget

Spend no more than 30 minutes on initial startup and no more than two controlled attempts. Capture the output from `diagnose.ps1`; then continue with `fallback-client-lab.py` if Kafka is unavailable. Broker configuration changes are not part of this exercise.

## Required observations

- Topic partition count and record metadata
- Same-key ordering and absence of global ordering
- Consumer assignment for same and different group IDs
- Committed position before and after restart
- Replay from an earlier position

The fallback proves client logic only. Mark integration evidence pending and return to it when a broker is available.
