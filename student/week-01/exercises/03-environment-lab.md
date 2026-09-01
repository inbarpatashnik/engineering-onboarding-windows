# Exercise 3: advanced Git incident lab

**Time:** 5 hours across Sunday and Monday  
**Objective:** Diagnose and recover realistic repository failures without relying on a hosting provider.

## Create the disposable lab repository

```powershell
.\training-platform\student\setup-week01-git-lab.ps1
Set-Location .\student-work\week-01-git-lab
```

The script creates a local repository with a known-good tag, a later regression, conflicting branches, and deliberately messy history. Do not inspect the fixture generator until after completing the lab.

## Lab A — regression search

1. Run `python .\verify.py` and record the failure.
2. Inspect `git log --graph --decorate --oneline --all`.
3. Use `git bisect` between `known-good` and `main`.
4. Automate the search with `git bisect run python verify.py` once classification is stable.
5. Record the first bad commit and explain why the test proves causation.
6. Reset the bisect session without rewriting history.

## Lab B — recover apparently lost work

1. Create and commit a file on a temporary branch.
2. Record its commit ID, switch away, and delete the branch.
3. Recover the commit using `git reflog` and a new branch.
4. Explain the difference between an unreachable name and immediately destroyed content.
5. State when recovery would no longer be safe to assume.

## Lab C — conflict correctness

1. Inspect `conflict-left` and `conflict-right`.
2. Rebase one onto the other and resolve the conflict from the intended invariant—not by blindly selecting one side.
3. Run verification before continuing the rebase.
4. Draw the before/after graphs and explain the rewritten commit identities.

## Lab D — reviewable history

Inspect `messy-history`. On a copy, produce a coherent review sequence using interactive rebase or new commits. Preserve final behavior and compare review, revert, and bisect quality.

## Expected observations

- Bisect narrows deterministic history logarithmically.
- Reflog records local reference movement and can locate unnamed commits.
- Rebase creates new commit identities.
- Conflict resolution is a semantic decision validated by tests.
- History quality changes review, revert, and regression diagnosis.

## Done when

`EVIDENCE.md` contains commands, graphs, the first bad commit, recovery proof, conflict rationale, verification results, and the history comparison.
