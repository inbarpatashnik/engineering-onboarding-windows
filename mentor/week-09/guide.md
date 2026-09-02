# Mentor guide — Week 9: System Design and Safe Change

> Restricted review guidance.

Assess whether the student understands the existing system before changing it. Challenge contracts, boundaries, compatibility, sequencing, evidence, and reversibility rather than diagram aesthetics.

## Challenge questions

- Which statements are observed facts and which are assumptions?
- Who owns each API, dataset, event, and failure boundary?
- What happens with old writer/new reader and new writer/old reader?
- What data makes rollback unsafe after a partial rollout?
- Can every stage remain deployed for a day?
- What evidence allows progression or requires rollback?
- Which complexity is temporary migration scaffolding, and how is it removed?

## Pass evidence

Require current-state maps, contract characterization, a defensible ADR, compatibility matrix, staged rollout, mixed-version tests, rollback rehearsal, and explicit unknowns. Red flags include big-bang migration, destructive schema change, unowned dual writes, flags without cleanup, and confident architecture unsupported by evidence.
