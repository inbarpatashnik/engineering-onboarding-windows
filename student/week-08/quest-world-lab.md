# Quest World observability investigation lab

Quest World is a text adventure instrumented with OpenTelemetry and backed by the Grafana LGTM stack. The game is the workload; your real task is to investigate it using metrics, logs, and traces.

## Choose one execution path

### Local Docker path

Use the official project: [grafana/adventure](https://github.com/grafana/adventure). Follow its current README using Docker Desktop and Docker Compose. Keep it in a separate short path such as `C:\training\quest-world`; do not copy its containers into this repository.

### Online fallback

Use the [Grafana Quest World Killercoda sandbox](https://killercoda.com/grafana-labs/course/workshops/adventure). It requires a free account but avoids local image and port troubleshooting.

## Setup timebox

Spend at most 45 minutes on the local path and make at most two controlled attempts. Before retrying, capture container status, the first relevant error, free disk/memory, and occupied ports. If it still fails, switch to Killercoda. Environment setup is not assessed.

## Investigation rules

1. Before opening detailed logs or traces, write a hypothesis from the user-visible symptom and a metric.
2. Pivot to logs using a bounded time window and stable attributes.
3. Follow one action as a trace and identify parent/child spans, service boundaries, duration, status, and relevant events.
4. Record every hypothesis change and the evidence that caused it.
5. Do not search by a known answer copied from the walkthrough until your own investigation is complete.

## Required evidence

- One metric that detects a trend but cannot explain its cause
- One log query narrowed by time and stable context
- One distributed trace across at least two boundaries
- One example of trace/log or metric/trace correlation
- One missing, misleading, high-cardinality, or sensitive attribute and a safer replacement
- A timeline: symptom → hypothesis → query → evidence → revised hypothesis → conclusion
- A small service/data-flow diagram showing application, Alloy/collector, and telemetry backends

## Connect prior weeks

Relate the investigation to HTTP request IDs and status semantics, database/cache or Kafka dependency behavior, testing, and reliability patterns. Explain which earlier control would prevent the fault and which telemetry would prove that control works.
