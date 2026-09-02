# Week 6 learning guide: Kafka Client Engineering

## Sunday — build the model

Read the core sources, draw producer → topic-partition → consumer group → side effect → offset commit, and predict three failure windows. Start Kafka only through the supplied script and honor the 30-minute setup timebox.

## Monday — observe the protocol from the client side

Produce keyed and unkeyed records, compare ordering, use two consumers in one group and consumers in different groups, restart a consumer, and replay. Record offsets and assignments rather than studying broker internals.

## Tuesday — build the client

Create a small producer and consumer behind narrow interfaces. Validate before publish, wait for delivery acknowledgement, use explicit keys, deserialize defensively, and keep side effects idempotent.

## Wednesday — failure cases

Test duplicates, malformed/unknown versions, transient processing failure, interruption before and after commit, rebalance/shutdown, and replay. Use fakes for fast deterministic unit tests and Kafka only for a small integration layer.

## Thursday — defend the guarantees

Reproduce from a fresh session, demonstrate one failure window, explain delivery semantics without saying “exactly once” loosely, and show which telemetry would detect lag, retries, rejects, and processing failure.
