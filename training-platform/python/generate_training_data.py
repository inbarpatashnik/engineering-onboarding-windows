from argparse import ArgumentParser
from pathlib import Path
import json, random

def main():
    parser = ArgumentParser(description="Generate deterministic synthetic onboarding data")
    parser.add_argument("--week", type=int, required=True, choices=range(1, 14))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(10_000 + args.week)
    teams = ["platform", "observability", "identity", "data"]
    resources = [{"id": f"res-{i:03d}", "name": f"week-{args.week:02d}-service-{i}", "owner": rng.choice(teams), "tier": rng.randint(1, 3)} for i in range(1, 9)]
    payload = {"seed": 10_000 + args.week, "week": args.week, "resources": resources}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8", newline="\n")
    print(args.output.resolve())

if __name__ == "__main__": main()
