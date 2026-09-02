# Exercise 5: weekly synthesis

Trace one event through producer validation, serialization, key selection, delivery acknowledgement, partition/offset assignment, poll, validation, side effect, and commit.

Repeat the trace for:

1. producer timeout with unknown delivery outcome;
2. crash before the side effect;
3. crash after the side effect but before commit;
4. poison message;
5. rebalance during processing;
6. intentional replay.

For each, state likely duplicate/loss behavior, safe client response, evidence, and test. Finish with two columns: **client owns** and **broker/platform owns**.
