# Week 10 deliverables checklist

- [ ] Threat model identifies assets, actors, trust boundaries, and prioritized abuse cases
- [ ] Authentication and authorization are implemented and explained separately
- [ ] Private/public key signing and verification are demonstrated with synthetic keys
- [ ] Token type, algorithm, signature, issuer, audience, time, subject, and required claims are validated
- [ ] Scope/role and resource-ownership authorization are tested separately
- [ ] Expiry, not-before, tampering, wrong audience/issuer, unknown key, and replay cases are covered
- [ ] Key rotation includes public-key overlap and bounded JWKS caching behavior
- [ ] Bearer tokens, private keys, secrets, and sensitive claims are absent from logs
- [ ] OAuth roles and common flows are explained without provider-specific administration
- [ ] 401/403 behavior and internal evidence are intentionally limited and tested
