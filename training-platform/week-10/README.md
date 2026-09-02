# Week 10 asymmetric-token lab

This local lab uses synthetic identities and keys. It demonstrates signing, public-key verification, claims, JWKS, rotation, and the boundary between authentication and authorization. Never copy real tokens, private keys, or company configuration into it.

## Install the isolated lab dependency

```powershell
.\training-platform\week-10\setup.ps1
```

If installation fails, preserve the error and continue with the reading/threat model while requesting focused help. Do not disable TLS verification or download random binaries.

## Create keys and issue a token

```powershell
.\.venv\Scripts\python.exe .\training-platform\week-10\auth-token-lab.py init --directory .\student-work\week-10-auth
.\.venv\Scripts\python.exe .\training-platform\week-10\auth-token-lab.py issue --directory .\student-work\week-10-auth --subject student-service --scope "resources:read resources:write" --output .\student-work\week-10-auth\access-token.txt
.\.venv\Scripts\python.exe .\training-platform\week-10\auth-token-lab.py verify --directory .\student-work\week-10-auth --token-file .\student-work\week-10-auth\access-token.txt --required-scope resources:write
```

The private key signs. `jwks.json` contains only public material used for verification. A signature protects integrity/authenticity; it does not hide the claims.

## Rotation and negative cases

```powershell
.\.venv\Scripts\python.exe .\training-platform\week-10\auth-token-lab.py rotate --directory .\student-work\week-10-auth
.\.venv\Scripts\python.exe .\training-platform\week-10\auth-token-lab.py self-test
```

Create and document expired, wrong-issuer, wrong-audience, unknown-key, modified-payload, missing-scope, and replay cases. Always verify with an allow-listed algorithm and expected issuer/audience. Token validity and resource authorization are separate decisions.
