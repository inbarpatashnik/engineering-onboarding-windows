# Week 10 source and workshop guide

## How to use sources

Do not read passively. For each source, capture five notes: the problem, the mechanism, one guarantee, one failure assumption, and one observable signal. Save notes in `EVIDENCE.md` with the source URL and relevant section title. Reading estimates are guidance.

## Core reading

- [OWASP authentication cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — suggested 40 min
- [OWASP authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — suggested 40 min
- [RFC 6750: bearer token usage](https://www.rfc-editor.org/rfc/rfc6750.html) — suggested 35 min
- [RFC 8725: JWT best current practices](https://www.rfc-editor.org/rfc/rfc8725.html) — suggested 50 min
- [RFC 9700: OAuth 2.0 security best current practice](https://www.rfc-editor.org/rfc/rfc9700.html) — suggested 50 min

## Guided web workshops

- [Repository asymmetric-token lab](../../training-platform/week-10/README.md) — 3 hours. **Evidence:** Generate a local key pair, issue signed synthetic tokens, verify claims, exercise key rotation, and reject deliberately invalid credentials.

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
