# Exercise 4: ownership and dependency models across document and graph databases

**Time:** 16 hours across Tuesday and Wednesday

## Goal

Model the same service-ownership and dependency domain as documents and as a labeled property graph. Neo4j is the learning implementation; ArangoDB is the transfer target. You are not expected to learn Neo4j administration.

## Required access patterns

1. Find the direct owner of a service.
2. Find every team affected by a dependency outage up to a bounded depth.
3. Detect a cycle and return the path that proves it.
4. Find services with no active owner.
5. Change an owner without leaving stale reverse relationships.

## Work

1. Write the five queries/questions before choosing a schema.
2. Build a document model and a property-graph model with the same synthetic data.
3. Complete the selected Neo4j GraphAcademy modules and implement at least three queries in Cypher.
4. Translate two traversals into AQL using ArangoDB's vertex/document and edge-collection model.
5. Create a cycle, a missing owner, and a high-fan-out dependency. Bound every traversal.
6. Compare correctness, query clarity, update complexity, indexing, and operational cost.
7. Recommend relational, document, graph, or ArangoDB multi-model storage for this domain. A mixed answer is allowed when boundaries are explicit.

## Transfer table

Include a table covering: Neo4j term, ArangoDB term, transferable idea, syntax/product difference, and operational question still unanswered. At minimum cover node/vertex document, relationship/edge document, properties, direction, path, traversal depth, cycle handling, and indexes.

## Done when

Another engineer can run the examples, see the same results in both models, understand why the chosen model fits the access patterns, and distinguish general graph reasoning from Neo4j- or ArangoDB-specific behavior.
