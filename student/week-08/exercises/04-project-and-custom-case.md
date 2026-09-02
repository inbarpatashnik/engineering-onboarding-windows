# Exercise 4: instrument and investigate one request path

**Time:** 15 hours across Tuesday and Wednesday

Instrument a small request path from an earlier week using OpenTelemetry. Reuse an HTTP client, database/cache interaction, or Kafka consumer rather than creating a new business system.

## Acceptance criteria

1. Propagate context across every boundary you control.
2. Emit structured logs correlated with trace/span IDs.
3. Measure request rate, errors, and duration with bounded-cardinality dimensions.
4. Represent dependency work as child spans with semantic conventions where available.
5. Preserve errors and useful span events without recording secrets or full sensitive payloads.
6. Create one latency or failure case and diagnose it using the Quest World investigation method.
7. Demonstrate that disabling or losing one signal does not silently change application correctness.

## Required comparison

Explain the difference between instrumentation and observability backend, correlation and coincidence, symptom and cause, logs and span events, metrics and traces, and request identifiers versus trace context.

## Done when

Another student can trigger the case, start from a user-visible symptom, use telemetry to narrow the cause, and point from each conclusion to evidence.
