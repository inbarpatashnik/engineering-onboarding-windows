# Mentor guide — Week 11: Performance, Capacity, and Resilience

> Restricted review guidance.

Assess whether resilience mechanisms control load and failure amplification under measurement. Do not accept patterns implemented without evidence.

## Challenge sequence

Begin healthy, add latency, then partial failures. Increase offered load, recover the dependency, and ask the student to explain useful work, retries, queues, percentiles, saturation, circuit state, and recovery surge.

## Pass evidence

Require a reproducible workload, correct percentile interpretation, one profiled bottleneck, end-to-end deadline, bounded retries with jitter, controlled concurrency/backpressure, safe recovery, retry-amplification measurements, maintained correctness, and honest before/after tradeoffs.

## Red flags

Averages without percentiles, coordinated-omission blindness, unlimited queues, retries at multiple layers, timeouts longer than the caller's budget, synchronized retries, circuit breakers without recovery design, throughput that counts failed/retried work as success, or optimization that changes correctness.
