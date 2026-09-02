# Exercise 4: resilient Kafka client

**Time:** 16 hours

Build a small event producer and consumer for synthetic resource-ownership changes.

## Acceptance criteria

1. Events have stable IDs, entity keys, timestamps, and explicit schema versions.
2. The producer validates before publish and observes delivery success/failure.
3. The consumer uses a stable group, bounded polling, graceful shutdown, and explicit commit behavior.
4. The side effect is idempotent by event ID.
5. Malformed and unsupported events are quarantined with a reason and safe metadata.
6. Transient processing failures retry with a strict bound; permanent failures do not block forever.
7. Tests cover failure before the side effect, after the side effect but before commit, and after commit.
8. Logs/metrics expose group, topic, partition, offset, lag, retry, reject, and processing outcome without leaking payloads.

## Required design statement

State the delivery behavior your client actually provides. Explain why broker claims alone cannot make an external side effect exactly once, and identify the transaction/idempotency boundary.

## Non-goals

Multi-broker deployment, replication tuning, provider selection, Kafka security administration, and production capacity planning.
