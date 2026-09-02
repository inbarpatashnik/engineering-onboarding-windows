# Exercise 3: authentication and signed-token lab

**Time:** 5 hours

Follow `training-platform\week-10\README.md`. Generate a synthetic RSA key pair, issue tokens with the private key, publish the public key as JWKS, and verify tokens as a resource server.

## Required cases

Valid token, modified payload, expired token, not-yet-valid token, wrong issuer, wrong audience, missing scope, unknown key ID, disallowed algorithm, key rotation overlap, valid identity without resource permission, and a bearer token replay.

For every rejection, record which validation layer rejected it and whether the result is authentication failure, authorization denial, or malformed input. Never use real organizational credentials or keys.
