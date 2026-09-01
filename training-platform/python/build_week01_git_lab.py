from argparse import ArgumentParser
from pathlib import Path
import json
import os
import subprocess

def run(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True)

def commit(repo: Path, message: str, minute: int) -> None:
    run(repo, "add", ".")
    env = os.environ.copy()
    stamp = f"2025-01-01T10:{minute:02d}:00Z"
    env["GIT_AUTHOR_DATE"] = stamp
    env["GIT_COMMITTER_DATE"] = stamp
    subprocess.run(["git", "commit", "-m", message], cwd=repo, check=True, env=env, capture_output=True, text=True)

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")

def main() -> None:
    parser = ArgumentParser(description="Create the disposable Week 1 advanced Git lab")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.output.resolve()
    if repo.exists():
        raise SystemExit(f"Refusing to overwrite existing lab: {repo}. Rename or remove it deliberately.")
    repo.mkdir(parents=True)
    run(repo, "init", "-b", "main")
    run(repo, "config", "user.name", "Training Student")
    run(repo, "config", "user.email", "student@example.invalid")

    write(repo / "config.json", json.dumps({"mode": "stable", "limit": 5}, indent=2) + "\n")
    write(repo / "verify.py", """from pathlib import Path\nimport json\ncfg=json.loads(Path('config.json').read_text())\nassert cfg['mode']=='stable', f\"regression: mode={cfg['mode']}\"\nassert cfg['limit']==5\nprint('verification passed')\n""")
    write(repo / "policy.json", json.dumps({"timeout": 5, "retries": 2}) + "\n")
    commit(repo, "Add deterministic verification baseline", 1)
    run(repo, "tag", "known-good")

    write(repo / "README.md", "# Disposable advanced Git lab\n\nUse evidence; do not inspect the fixture generator until the lab is complete.\n")
    commit(repo, "Document the verification contract", 2)
    write(repo / "config.json", json.dumps({"mode": "fast", "limit": 5}, indent=2) + "\n")
    commit(repo, "Optimize configuration loading", 3)
    write(repo / "notes.md", "The regression is intentionally followed by unrelated history.\n")
    commit(repo, "Add operational notes", 4)

    run(repo, "checkout", "-b", "conflict-left", "known-good")
    write(repo / "policy.json", json.dumps({"timeout": 3, "retries": 2}) + "\n")
    commit(repo, "Reduce request timeout", 10)
    run(repo, "checkout", "-b", "conflict-right", "known-good")
    write(repo / "policy.json", json.dumps({"timeout": 5, "retries": 4}) + "\n")
    commit(repo, "Increase retry allowance", 11)

    run(repo, "checkout", "-b", "messy-history", "known-good")
    write(repo / "feature.py", "def normalize(value):\n    return value.strip().lower()\n")
    commit(repo, "WIP", 20)
    write(repo / "test_feature.py", "from feature import normalize\nassert normalize(' READY ') == 'ready'\n")
    commit(repo, "fix stuff", 21)
    write(repo / "feature.py", "def normalize(value):\n    \"\"\"Normalize external state labels.\"\"\"\n    return value.strip().lower()\n")
    commit(repo, "oops docs", 22)
    run(repo, "checkout", "main")
    print(repo)

if __name__ == "__main__":
    main()
