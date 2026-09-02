# Week 6: Kafka Client Engineering

## Outcome

Build a producer and consumer that behave safely under acknowledgement failure, duplicates, poison messages, rebalancing, restart, and replay. Docker is used to supply Kafka; broker administration is explicitly out of scope.

## Weekly rhythm — approximately 40 hours

| Day | Focus | Hours |
|---|---|---:|
| Sunday | Sources, client guarantees, start the disposable broker | 8 |
| Monday | Producer/consumer experiments and offset evidence | 8 |
| Tuesday | Implement a reliable client vertical slice | 8 |
| Wednesday | Duplicate, poison, restart, replay, and recovery cases | 8 |
| Thursday | Reproduce, document, demonstrate, mentor challenge | 8 |

## Boundaries

- **Learn deeply:** keys and partition ordering, acknowledgements, serialization, consumer groups, offset commits, retries, idempotency, poison-message handling, graceful shutdown, lag and client observability.
- **Understand at awareness level:** brokers, replication, leaders, retention, and why these affect client guarantees.
- **Do not spend the week on:** Kafka installation, KRaft configuration, broker tuning, storage sizing, cluster upgrades, ACL administration, or provider consoles.

## Start here

1. Complete [the source guide](source-guide.md) and [source notes](exercises/01-source-notes.md).
2. Follow the [Kafka client lab](../../training-platform/week-06/README.md).
3. Complete [small practice](exercises/02-small-practice.md), [the main project](exercises/04-project-and-custom-case.md), and [weekly synthesis](exercises/05-weekly-synthesis.md).

## Local-environment timebox

Allow at most **30 minutes** for the first Kafka start, including image download. Run the supplied readiness check; do not improvise broker configuration. If the second clean attempt fails, save the diagnostic bundle and continue with the supplied in-memory client lab and unit tests. Ask for focused help asynchronously. When Kafka becomes available, run the integration checks later; do not lose a learning day to infrastructure.

## Deliverables

- Producer and consumer source with dependency file
- Unit tests using a broker-independent client boundary
- Kafka integration tests, or documented diagnostic evidence if the timeboxed fallback was used
- Evidence for partitions, ordering, group behavior, commits, restart, and replay
- Duplicate and poison-message cases with safe behavior
- Client metrics/log design that omits message secrets
- `DECISIONS.md`, `RUNBOOK.md`, and `EVIDENCE.md`

## Definition of done

You can explain when a record may be lost or repeated, place offset commits relative to side effects, recover after interruption, and separate application responsibilities from broker/provider responsibilities.
