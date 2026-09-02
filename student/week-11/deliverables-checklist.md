# Week 11 deliverables checklist

- [ ] Workload, correctness invariant, target, and resource budget are defined
- [ ] Healthy baseline is reproducible and reports p50/p95/p99, throughput, errors, and saturation
- [ ] One measured bottleneck is supported by profiler evidence
- [ ] Slow and partially failing dependency behavior is measured under load
- [ ] End-to-end deadline and retry budget are explicit
- [ ] Backoff includes jitter and retry amplification is measured
- [ ] Concurrency/queue limits and overload behavior are bounded
- [ ] Circuit opening, probing, closing, and recovery surge are demonstrated
- [ ] Correctness and idempotency survive retry and load shedding
- [ ] Before/after results disclose moved bottlenecks and tradeoffs
- [ ] Capacity estimate lists assumptions and uncertainty
