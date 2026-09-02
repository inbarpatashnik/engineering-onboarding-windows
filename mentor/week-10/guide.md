# Mentor guide — Week 10: Security, Authentication, and Authorization

> Restricted review guidance.

Assess mechanism understanding, validation completeness, key custody, authorization separation, and safe failure. Do not reward custom cryptography or identity-provider administration.

## Hidden checks

Modified payload, `alg` confusion/disallowed algorithm, wrong issuer, wrong audience, expired/not-yet-valid token, unknown `kid`, stale JWKS during rotation, missing scope, another owner's resource, token replay, and accidental credential logging.

## Questions

- What does the signature prove, and what does it not prove?
- Why is a signed JWT readable and not necessarily encrypted?
- Who holds the private key and who receives the public key?
- Why can a cryptographically valid token still be unauthorized?
- What is the difference between access, refresh, and ID tokens?
- What happens during key rotation and JWKS failure?
- Where can a bearer token leak or be replayed?

## Pass evidence

Require allow-listed algorithms, complete claim validation, separate resource authorization, safe key/token handling, rotation reasoning, bounded caching, clear 401/403 behavior, and tests. Reject solutions that decode without verifying, trust token claims blindly, log tokens, embed private keys, or confuse signing with encryption.
