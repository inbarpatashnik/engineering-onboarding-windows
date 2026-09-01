# Exercise 4: provider-neutral verification pipeline

**Time:** 15 hours across Tuesday and Wednesday  
**Objective:** Build one deterministic verification contract that behaves the same on a developer machine and a clean automated runner.

## Project

Create one documented entry point such as:

```powershell
.\scripts\verify.ps1
```

PowerShell should be only a thin launcher when portable project tooling can implement the checks. Do not write GitHub Actions, GitLab CI, Jenkins, or other provider configuration this week.

## Required stages

1. Validate tools and configuration without printing secrets.
2. Check formatting or inexpensive static rules.
3. Run unit tests.
4. Run integration or contract tests.
5. Start the training environment and perform a bounded smoke check.
6. Produce a small machine-readable summary artifact.
7. Return nonzero on every failed required stage.
8. Clean up resources it started, even after failure.

## Clean-runner cases

Reproduce and fix at least three causes of “local pass, clean runner fail”:

- An untracked or ignored file required by a test.
- Order-dependent tests or leaked process state.
- An undeclared dependency or environment variable.
- A case-sensitive path or working-directory assumption.
- A cached/generated artifact masking a missing build step.

Use a fresh clone or disposable copy to simulate the runner. The command must not depend on GitHub or GitLab.

## CI design record

Define stages, dependencies, fail-fast versus always-run behavior, artifacts, cache safety, timeout budget, secret boundary, and blocking checks. Explain how any CI provider can invoke the same contract without changing semantics.

## Tests

- Passing clean run
- Failing static/unit stage with correct exit code
- Integration timeout with cleanup proof
- Missing dependency/configuration with a clear message
- One hidden-state regression converted to a deterministic test

## Done when

Another engineer can run one command from a clean checkout, understand every stage, locate failure evidence, and connect the contract to any CI system.
