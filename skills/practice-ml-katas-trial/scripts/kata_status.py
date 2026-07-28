"""Inspect kata implementation status and recommend the next exercise."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


MARKERS = (
    "EDITION.json",
    "CATALOG.md",
    "PROGRESS.md",
    "ENVIRONMENT.md",
    "katas",
)
CATALOG_ROW = re.compile(
    r"\|\s*\d+\s*\|\s*\[[^\]]+\]\((katas/[^)]+/README\.md)\)"
    r"\s*\|\s*(Beginner|Easy|Medium|Hard)\s*\|"
)


def is_project_root(path: Path) -> bool:
    return all((path / marker).exists() for marker in MARKERS)


def find_project_root(explicit: str | None = None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())

    configured_home = os.environ.get("ML_KATAS_HOME")
    if configured_home:
        candidates.append(Path(configured_home).expanduser())

    current = Path.cwd().resolve()
    candidates.extend((current, *current.parents))

    skill_file = Path(__file__).resolve()
    candidates.extend(skill_file.parents)
    candidates.extend(
        (
            Path.home() / "ml-katas-trial",
            Path.home() / "llm-from-scratch-katas_V1",
        )
    )

    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if is_project_root(resolved):
            return resolved

    raise FileNotFoundError(
        "Could not find the Trial Edition course. Pass --root, set "
        "ML_KATAS_HOME, or initialize a checkout with bootstrap_course.py."
    )


def implementation_status(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    if "raise NotImplementedError" in source:
        return "not_started"
    return "started"


def read_edition(root: Path) -> dict[str, object]:
    edition_path = root / "EDITION.json"
    with edition_path.open(encoding="utf-8") as file:
        return json.load(file)


def read_difficulties(root: Path) -> dict[str, str]:
    catalog = (root / "CATALOG.md").read_text(encoding="utf-8")
    difficulties: dict[str, str] = {}
    for match in CATALOG_ROW.finditer(catalog):
        kata_path = Path(match.group(1)).parent
        difficulties[str(kata_path)] = match.group(2)
    return difficulties


def load_learner_profile(root: Path) -> dict[str, object] | None:
    source = root / ".local" / "learner_profile.json"
    if not source.is_file():
        return None
    try:
        profile = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    if profile.get("schema_version") != 1:
        return None
    return profile


def collect_katas(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    difficulties = read_difficulties(root)
    for module in sorted((root / "katas").iterdir()):
        if not module.is_dir():
            continue
        for kata in sorted(module.iterdir()):
            implementation = kata / "implementation.py"
            if not kata.is_dir() or not implementation.is_file():
                continue
            rows.append(
                {
                    "module": module.name,
                    "kata": kata.name,
                    "status": implementation_status(implementation),
                    "path": str(kata.relative_to(root)),
                    "difficulty": difficulties.get(
                        str(kata.relative_to(root)),
                        "Unknown",
                    ),
                }
            )
    return rows


def recommend(
    rows: list[dict[str, str]],
    profile: dict[str, object] | None = None,
) -> dict[str, str] | None:
    for row in rows:
        if row["status"] == "started":
            return row

    if profile:
        preferred = profile.get("preferred_difficulties", [])
        if isinstance(preferred, list):
            for difficulty in preferred:
                for row in rows:
                    if (
                        row["status"] == "not_started"
                        and row["difficulty"] == difficulty
                    ):
                        return row

    for row in rows:
        if row["status"] == "not_started":
            return row
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", help="Path to the kata repository")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    try:
        root = find_project_root(args.root)
    except FileNotFoundError as error:
        parser.error(str(error))

    rows = collect_katas(root)
    profile = load_learner_profile(root)
    recommendation = recommend(rows, profile)
    edition = read_edition(root)

    if args.json:
        print(
            json.dumps(
                {
                    "root": str(root),
                    "edition": edition,
                    "learner_profile": profile,
                    "diagnostic_recommended": profile is None,
                    "katas": rows,
                    "recommended": recommendation,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    print(f"Project: {root}")
    print(
        f"Edition: {edition['display_name']} "
        f"({edition['edition']}, {edition['distribution']})"
    )
    if profile:
        print(
            f"Learner level: {profile['label']} "
            f"({profile['score']}/{profile['max_score']})"
        )
    else:
        print("Learner level: not assessed")
    for row in rows:
        marker = "*" if row is recommendation else " "
        print(
            f"{marker} {row['module']}/{row['kata']}: "
            f"{row['status']} ({row['difficulty']})"
        )
    if recommendation:
        print(f"Recommended: {recommendation['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
