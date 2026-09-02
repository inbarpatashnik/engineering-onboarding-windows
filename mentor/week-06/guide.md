# Mentor guide — Week 6: Kafka Client Engineering

> Restricted review guidance.

Assess the student as an application/client engineer, not a Kafka operator. A local Docker failure is not a learning failure when the student honors the timebox, captures useful diagnostics, continues with deterministic tests, and later identifies the missing integration evidence.

## Challenge questions

- What happens if publish times out after the broker accepted the record?
- Why does a key provide per-entity ordering but not global ordering?
- Where is the offset committed relative to the side effect?
- What happens after a crash in each gap?
- How does the idempotency record become atomic with the side effect?
- Can a poison record block the partition? How is it quarantined?
- What happens when consumers outnumber partitions?
- What does rebalance do to in-flight work and shutdown?
- Which claims belong to the client, Kafka protocol, broker configuration, or provider?

## Pass evidence

Require explicit delivery semantics, observable delivery acknowledgement, intentional keys, defensive deserialization/versioning, bounded retry, idempotent effects, justified commits, graceful close, restart/replay evidence, and tests that separate client logic from the broker integration.

## Red flags

Calling `produce` and assuming success, committing before an unsafe side effect, treating `auto.offset.reset` as normal resume behavior, claiming global ordering, endless poison-message retry, using payloads as log context, saying “exactly once” without naming the boundary, or spending hours tuning the training broker.
