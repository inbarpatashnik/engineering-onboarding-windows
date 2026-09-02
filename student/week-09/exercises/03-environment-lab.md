# Exercise 3: system map and safe-change design lab

**Time:** 5 hours

Start the Week 9 environment and treat it as an unfamiliar service. Do not propose changes until you can show its current contracts.

## Build the map

Identify entry points, callers, synchronous dependencies, asynchronous boundaries, persistent state, caches, ownership, trust boundaries, observable signals, and failure propagation. Mark facts, assumptions, and unknowns differently.

## Proposed change

Add an asynchronous ownership-change workflow while preserving the existing synchronous API and stored data. Your design must allow old and new producers, consumers, and API clients to overlap during rollout.

## Required experiments

1. Characterize the current API, data, and event contracts with executable checks.
2. Introduce an additive representation that old readers ignore safely.
3. Simulate old writer/new reader, new writer/old reader, and mixed event versions.
4. Show what happens when rollout stops after each stage.
5. Rehearse rollback without deleting or corrupting data written by the new version.

## Output

A system-context diagram, dependency/data-flow diagram, contract inventory, risk list, compatibility matrix, staged rollout, rollback plan, and evidence gates.
