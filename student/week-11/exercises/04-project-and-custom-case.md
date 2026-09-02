# Exercise 4: keep a partially failing workload stable

**Time:** 15 hours

## Acceptance criteria

1. Define a representative workload, correctness invariant, service-level target, and resource budget.
2. Establish repeatable baseline percentiles and throughput before optimization.
3. Profile one demonstrated bottleneck; do not optimize by intuition alone.
4. Apply an end-to-end timeout budget and bounded retry policy with jitter.
5. Limit concurrency or queue growth and define admission/backpressure behavior.
6. Use circuit breaking only with explicit states, thresholds, probes, and recovery behavior.
7. Measure retry amplification and useful work during degradation and recovery.
8. Preserve correctness and idempotency while shedding or retrying work.
9. Show before/after evidence and identify the bottleneck or tradeoff that moved elsewhere.

## Scope control

Implement only the mechanisms required by measured evidence. Extensive profiler mechanics, multiple load tools, infrastructure autoscaling, and provider capacity configuration are optional.

## Final evidence

Workload definition, raw results, p50/p95/p99, throughput, errors, saturation, retry multiplier, recovery timeline, profiler evidence, chosen controls, rejected alternatives, and capacity estimate with assumptions.
