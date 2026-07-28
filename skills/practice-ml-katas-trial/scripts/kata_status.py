"""Inspect kata implementation status and recommend the next exercise."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


MARKERS = (
    "EDITION.json",
    "CATALOG.md",
    "PROGRESS.md",
    "ENVIRONMENT.md",
    "katas",
)


def is_project_root(path: Path) -> bool:
    return all((path / marker).exists() for marker in MARKERS)


def find_project_root(explicit: str | None = None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())

    current = Path.cwd().resolve()
    candidates.extend((current, *current.parents))

    skill_file = Path(__file__).resolve()
    candidates.extend(skill_file.parents)

    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if is_project_root(resolved):
            return resolved

    raise FileNotFoundError(
        "Could not find a project containing CATALOG.md, PROGRESS.md, "
        "ENVIRONMENT.md, and katas/. Pass --root explicitly."
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


def collect_katas(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
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
                }
            )
    return rows


def recommend(rows: list[dict[str, str]]) -> dict[str, str] | None:
    for row in rows:
        if row["status"] == "started":
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
    recommendation = recommend(rows)
    edition = read_edition(root)

    if args.json:
        print(
            json.dumps(
                {
                    "root": str(root),
                    "edition": edition,
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
    for row in rows:
        marker = "*" if row is recommendation else " "
        print(
            f"{marker} {row['module']}/{row['kata']}: {row['status']}"
        )
    if recommendation:
        print(f"Recommended: {recommendation['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
