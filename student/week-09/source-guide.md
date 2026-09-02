# Week 9 source and workshop guide

## How to use sources

Do not read passively. For each source, capture five notes: the problem, the mechanism, one guarantee, one failure assumption, and one observable signal. Save notes in `EVIDENCE.md` with the source URL and relevant section title. Reading estimates are guidance.

## Core reading

- [Microsoft: API design and implementation](https://learn.microsoft.com/azure/architecture/best-practices/api-design) — suggested 45 min
- [Martin Fowler: Branch By Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html) — suggested 35 min
- [AWS Builders' Library: ensuring rollback safety](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/) — suggested 45 min

## Guided web workshops

- [Repository safe-change design lab](exercises/03-environment-lab.md) — 3 hours. **Evidence:** Map the supplied system, propose a change, and prove compatibility and rollback across staged mixed versions.

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
