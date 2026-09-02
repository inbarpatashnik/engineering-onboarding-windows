# Exercise 2: Kafka client practice

## 1. Keys, partitions, and ordering — 2 hours

Publish an interleaved sequence for three entity IDs to a three-partition topic. Predict and then record partitions and offsets. Explain why order exists within a partition but not globally, and choose an application key.

## 2. Groups, commits, restart, and replay — 3 hours

Run two consumers with the same group ID, then two different group IDs. Record assignments. Process a bounded batch, commit, restart, and show the resume point. Use a new group or explicit seek to replay. Explain when replay is safe.

## 3. Duplicate and poison events — 3 hours

Feed the same event ID twice and prove the side effect occurs once. Feed malformed JSON, a missing required field, and an unknown schema version. Reject or quarantine them without blocking the partition forever or committing unrelated work incorrectly.

## Evidence format

For each experiment record prediction, client configuration, input IDs/keys, partition and offset, processing result, commit position, restart/replay result, and conclusion. Never include credentials or sensitive payloads.
