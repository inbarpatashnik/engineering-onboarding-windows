# Week 11 source and workshop guide

## How to use sources

Do not read passively. For each source, capture five notes: the problem, the mechanism, one guarantee, one failure assumption, and one observable signal. Save notes in `EVIDENCE.md` with the source URL and relevant section title. Reading estimates are guidance.

## Core reading

- [AWS Builders' Library: timeouts, retries and backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — suggested 60 min
- [Google SRE: handling overload](https://sre.google/sre-book/handling-overload/) — suggested 50 min
- [Grafana k6 running tests](https://grafana.com/docs/k6/latest/get-started/running-k6/) — suggested 40 min
- [Python profiling](https://docs.python.org/3/library/profile.html) — suggested 30 min

## Guided web workshops

- [Grafana k6 load-and-resilience lab](https://grafana.com/docs/k6/latest/get-started/running-k6/) — 2 hours. **Evidence:** Create repeatable load stages and thresholds, then measure how retries, limits, and recovery change percentiles and failure amplification.

External workshops may require a free account or create a separate practice repository. Never enter company secrets, production data, or internal source code. Use synthetic training data only.

## Reading questions

- Which statement is a protocol/tool guarantee, and which is a recommendation?
- Which default is safe for a tutorial but unsafe at production scale?
- What evidence would falsify your current understanding?
- Which concept will you demonstrate in the local training environment?

## Source completion evidence

- Links and sections completed
- Five-note record for every core source
- Workshop output, screenshot-free command evidence, or resulting repository URL
- Three unanswered questions ranked by importance
