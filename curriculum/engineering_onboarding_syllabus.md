# Engineering onboarding syllabus

## Learning model

Each week combines concepts, a constrained build, evidence collection, review, and reflection. Depth labels are **Deep** (implement and debug), **Working familiarity** (use safely and explain tradeoffs), and **Awareness** (recognize and know when to seek help).

## Week 1: Advanced Git, Reproducible Verification, and CI Foundations

- **Depth:** Deep
- **Subjects:** Git commit graphs, bisect, reflog recovery, conflict resolution, reviewable history, clean-room verification, CI stages and failure propagation.
- **Applied work:** Build a provider-neutral local verification pipeline and diagnose a regression.
- **Exit capability:** Recover repository state and explain why automated verification differs from a developer machine.

## Week 2: HTTP APIs and Contracts

- **Depth:** Deep
- **Subjects:** HTTP semantics, REST, validation, error models, retries.
- **Applied work:** Implement a resilient API client.
- **Exit capability:** Distinguish client, server, and transient failures.

## Week 3: Data Modeling and SQL

- **Depth:** Deep
- **Subjects:** relational modeling, indexes, transactions, query plans.
- **Applied work:** Design and query a resource catalog.
- **Exit capability:** Defend schema and index choices with measurements.

## Week 4: Document and Graph Data

- **Depth:** Working familiarity
- **Subjects:** document stores, graph traversal, denormalization tradeoffs.
- **Applied work:** Model ownership and dependency relationships.
- **Exit capability:** Choose a model based on access patterns.

## Week 5: Caching and Concurrency

- **Depth:** Deep
- **Subjects:** Redis patterns, race conditions, idempotency, locking.
- **Applied work:** Add safe caching to the catalog client.
- **Exit capability:** Demonstrate correctness under concurrent requests.

## Week 6: Events and Messaging

- **Depth:** Working familiarity
- **Subjects:** Kafka concepts, delivery semantics, schemas, consumers.
- **Applied work:** Build an idempotent event consumer.
- **Exit capability:** Recover from duplicates and poison messages.

## Week 7: Testing Strategy

- **Depth:** Deep
- **Subjects:** unit, integration, contract, property, and end-to-end testing.
- **Applied work:** Create a layered automated test suite.
- **Exit capability:** Explain what each test catches and misses.

## Week 8: Observability

- **Depth:** Deep
- **Subjects:** structured logs, metrics, traces, correlation, SLO signals.
- **Applied work:** Instrument a request path.
- **Exit capability:** Diagnose latency using correlated telemetry.

## Week 9: System Design and Safe Change

- **Depth:** Deep
- **Subjects:** system mapping, boundaries, compatibility, ADRs, staged change, mixed versions, rollback.
- **Applied work:** Design and stage a backward-compatible system change.
- **Exit capability:** Change an unfamiliar system without breaking its contracts.

## Week 10: Security, Authentication, and Authorization

- **Depth:** Working familiarity
- **Subjects:** threat modeling, authentication, authorization, asymmetric keys, tokens, OAuth roles, secrets, input safety.
- **Applied work:** Secure a resource API and verify signed access tokens.
- **Exit capability:** Identify trust boundaries and correctly validate identity and permissions.

## Week 11: Performance, Capacity, and Resilience

- **Depth:** Working familiarity
- **Subjects:** profiling, load testing, percentiles, saturation, queues, timeouts, retry budgets, jitter, backpressure, circuit breakers, recovery.
- **Applied work:** Keep a slow and partially failing workload stable under bounded load.
- **Exit capability:** Measure capacity and prevent failure amplification.

## Week 12: Delivery and Operations

- **Depth:** Working familiarity
- **Subjects:** CI/CD, containers, configuration, migrations, rollback.
- **Applied work:** Create a safe release runbook.
- **Exit capability:** Plan detection, rollback, and data compatibility.

## Week 13: Capstone Incident

- **Depth:** Deep
- **Subjects:** system synthesis, incident response, communication, remediation.
- **Applied work:** Diagnose and stabilize a multi-symptom incident.
- **Exit capability:** Lead a clear evidence-based incident review.
