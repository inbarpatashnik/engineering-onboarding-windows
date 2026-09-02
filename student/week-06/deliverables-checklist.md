# Week 6 deliverables checklist

- [ ] Core-source notes answer the weekly prompts
- [ ] Kafka startup was successful or the 30-minute fallback and diagnostic evidence are documented
- [ ] Partition, ordering, group, commit, restart, and replay evidence is included
- [ ] Producer checks delivery outcomes and uses intentional keys
- [ ] Consumer commit placement is explicit and defended
- [ ] Side effects are idempotent under duplicate delivery
- [ ] Poison/unknown-version events cannot block the partition indefinitely
- [ ] Unit tests do not require Kafka; a small integration suite uses Kafka when available
- [ ] Logs and metrics support diagnosis without exposing sensitive payloads
- [ ] Client responsibilities are separated from broker/provider responsibilities
- [ ] Runbook, decisions, evidence, and Thursday demo are complete
