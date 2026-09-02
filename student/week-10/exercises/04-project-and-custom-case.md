# Exercise 4: secure a resource API

**Time:** 16 hours

## Goal

Protect a synthetic resource API using a local issuer and resource-server verifier. Use established libraries; do not implement cryptographic algorithms.

## Acceptance criteria

1. Document actors: user/service, client, authorization server, resource server, and resource owner.
2. Separate credentials, identity claims, and permissions.
3. Accept only configured algorithms and trusted issuer keys.
4. Validate token type, signature, issuer, audience, expiry, not-before, subject, and required claims.
5. Evaluate scopes/roles and resource ownership separately from token validity.
6. Support key IDs and an overlap window during public-key rotation.
7. Bound JWKS caching and define behavior when refresh fails.
8. Keep bearer tokens, private keys, secrets, and sensitive claims out of logs.
9. Return deliberately limited 401/403 responses and richer sanitized internal evidence.
10. Test replay, confused-audience, tampering, expiry, missing permission, and rotation.

## Design explanation

Explain session cookies, API keys, opaque tokens, JWT access tokens, access versus refresh versus ID tokens, OAuth client/authorization/resource-server roles, Authorization Code with PKCE, and Client Credentials. Mark which mechanisms are implemented and which are conceptual.

## Central question

For every request: who issued this credential, for whom, for which service, for which operation, until when, and why should this service trust it?
