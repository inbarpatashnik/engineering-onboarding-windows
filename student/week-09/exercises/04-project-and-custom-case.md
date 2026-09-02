# Exercise 4: design and stage a backward-compatible change

**Time:** 16 hours

## Acceptance criteria

1. Start with a written problem, users, constraints, invariants, and non-goals.
2. Map existing ownership and contracts before choosing a solution.
3. Record at least two viable alternatives in an ADR and explain the tradeoff.
4. Preserve compatibility across APIs, stored data, and events.
5. Break implementation into independently deployable and observable stages.
6. Define mixed-version behavior and rollback at every irreversible boundary.
7. Attach tests and observable evidence to each rollout gate.
8. Identify security, operability, performance, and failure-mode consequences.

## Required stages

Characterize → introduce compatibility seam → dual-read or dual-write only when justified → migrate/backfill → switch behavior → remove legacy path after evidence. Do not use a flag as a substitute for compatibility analysis.

## Review scenario

The rollout is paused halfway through while old and new instances both serve traffic. Demonstrate correct behavior, detection of divergence, and a safe next action.
