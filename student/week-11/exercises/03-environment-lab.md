# Exercise 3: load, amplification, and recovery lab

**Time:** 6 hours

Create a repeatable staged workload. Record request rate, throughput, error rate, latency percentiles, concurrency, queue depth where available, dependency calls, retries, and recovery time.

Run controlled cases in this order:

1. Healthy baseline.
2. Increased latency without retries.
3. Partial failure with immediate retries.
4. Same failure with a total deadline, bounded attempts, exponential backoff, and jitter.
5. Add a concurrency limit or bounded queue and define overload behavior.
6. Open and recover a circuit breaker; observe the recovery surge.

Change one mechanism at a time. Plot or tabulate offered load versus completed useful work. Explain when an apparently lower error rate hides worse latency or resource use.
