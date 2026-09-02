# Mentor guide — Week 8: Observability

> Restricted review guidance.

Assess investigation quality and instrumentation choices, not Grafana navigation or Docker setup. Quest World is used to teach signal selection, correlation, and hypothesis revision while combining HTTP, data, messaging, testing, and reliability knowledge from earlier weeks.

## Review challenge

Give the student a symptom without naming the affected component. Ask them to begin with a broad, low-cardinality signal, define a hypothesis, narrow the time window, pivot across signals, and show the evidence that changes or confirms the hypothesis.

## Questions

- Which signal detected the problem, and which explained it?
- What evidence proves causation rather than temporal correlation?
- Where was context propagated or lost?
- Which attribute creates cardinality or privacy risk?
- How would sampling change the investigation?
- Which earlier resilience or test pattern would prevent recurrence?
- What client or business metric is missing from infrastructure telemetry?

## Pass evidence

Require a coherent investigation timeline, bounded queries, trace structure across boundaries, cross-signal correlation, safe attributes, RED-style signals, one deliberate failure, and explicit limitations. Do not penalize a documented switch to Killercoda after the setup timebox.

## Red flags

Random dashboard clicking, unbounded log searches, treating a correlation ID as full trace propagation, putting user IDs or request IDs into metric labels, logging payloads or credentials, declaring root cause from one graph, or spending hours repairing the lab stack.
