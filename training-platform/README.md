# Training platform

The platform exposes a deterministic simulator on port 8080. Week profiles optionally add PostgreSQL, Redis, or Redpanda while preserving one consistent student API. Docker Compose profiles are selected by the PowerShell scripts; students do not need to memorize Compose flags.

## Commands

```powershell
.\scripts\setup.ps1
.\scripts\start-week.ps1 -Week 6
.\scripts\seed-data.ps1 -Week 6
.\scripts\smoke-test.ps1 -Week 6
.\scripts\stop-week.ps1 -Week 6
```

The simulator endpoints are `/health`, `/api/resources`, `/api/dependency`, `/api/state`, and mentor-only `/admin/*`. Admin requests require the local training token from `.env`; the scripts supply it automatically. This is a learning environment, not a production security design.

## Week services

- Weeks 1–2: simulator only
- Weeks 3 and 7: PostgreSQL
- Weeks 4, 5, 8, 9, 10, 11: PostgreSQL and Redis as relevant
- Weeks 6, 12, 13: PostgreSQL, Redis, and Redpanda

Named volumes retain data between stop/start. `reset-week.ps1` deletes only Compose resources for this project and then reseeds synthetic data.
