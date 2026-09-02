# Training platform

The platform exposes a deterministic simulator on port 8080. Week profiles optionally add PostgreSQL, Redis, or the official Apache Kafka image while preserving one consistent student workflow. Docker Compose profiles are selected by the PowerShell scripts; students do not need to memorize Compose flags.

## Commands

```powershell
.\scripts\setup.ps1
.\scripts\start-week.ps1 -Week 6
.\scripts\seed-data.ps1 -Week 6
.\scripts\smoke-test.ps1 -Week 6
.\scripts\stop-week.ps1 -Week 6
```

The simulator endpoints are `/health`, `/api/resources`, `/api/dependency`, `/api/state`, and mentor-only `/admin/*`. Admin requests require the local training token from `.env`; the scripts supply it automatically. This is a learning environment, not a production security design.

Students own routine operation. `student/run-case.ps1` applies a visible deterministic case, `student/new-case.ps1` creates a custom case, and `student/reset-case.ps1` restores normal dependency behavior. The wrappers use the local admin endpoint so students can focus on system behavior rather than PowerShell details. Mentor controls are only for hidden review scenarios.

## Week services

- Weeks 1–2: simulator only
- Weeks 3 and 7: PostgreSQL
- Weeks 4, 5, 8, 9, 10, 11: PostgreSQL and Redis as relevant
- Weeks 6, 12, 13: PostgreSQL, Redis, and Apache Kafka

Week 6 treats Kafka as a disposable dependency. Students learn producer and consumer behavior, not broker installation or cluster administration. See `week-06/README.md` for the setup timebox and fallback route.

Named volumes retain data between stop/start. `reset-week.ps1` deletes only Compose resources for this project and then reseeds synthetic data.
