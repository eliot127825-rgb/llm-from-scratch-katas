"""Safely initialize a local checkout of the public Trial Edition course."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_SOURCE = (
    "https://github.com/eliot127825-rgb/llm-from-scratch-katas_V1.git"
)
MARKERS = (
    "EDITION.json",
    "CATALOG.md",
    "PROGRESS.md",
    "ENVIRONMENT.md",
    "katas",
)


def is_project_root(path: Path) -> bool:
    return all((path / marker).exists() for marker in MARKERS)


def read_edition(root: Path) -> dict[str, object]:
    with (root / "EDITION.json").open(encoding="utf-8") as file:
        return json.load(file)


def validate_destination(destination: Path) -> None:
    if destination == Path(destination.anchor):
        raise ValueError("Refusing to use a filesystem root as the destination")

    if destination.exists():
        if not destination.is_dir():
            raise ValueError(f"Destination is not a directory: {destination}")
        if is_project_root(destination):
            return
        if any(destination.iterdir()):
            raise ValueError(
                "Destination already exists and is not an empty Trial Edition "
                f"directory: {destination}"
            )


def clone_course(source: str, destination: Path, dry_run: bool = False) -> str:
    destination = destination.expanduser().resolve()
    validate_destination(destination)

    if is_project_root(destination):
        edition = read_edition(destination)
        if edition.get("edition") != "trial":
            raise ValueError(
                f"Existing project is not the Trial Edition: {destination}"
            )
        return "reused"

    git = shutil.which("git")
    if git is None:
        raise RuntimeError(
            "Git is required to initialize the course. Install Git or clone "
            f"{DEFAULT_SOURCE} manually."
        )

    command = [git, "clone", "--depth", "1", source, str(destination)]
    if dry_run:
        print("Dry run; no files will be created.")
        print(f"Source: {source}")
        print(f"Destination: {destination}")
        print("Command: git clone --depth 1 <source> <destination>")
        return "planned"

    destination.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"Git clone failed: {detail}")

    if not is_project_root(destination):
        raise RuntimeError(
            "The cloned repository is missing required Trial Edition files"
        )

    edition = read_edition(destination)
    if edition.get("edition") != "trial":
        raise RuntimeError(
            "The cloned repository does not identify itself as the Trial Edition"
        )
    return "cloned"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Initialize the public ML Katas Trial Edition"
    )
    parser.add_argument(
        "--destination",
        required=True,
        help="Confirmed destination directory for the course checkout",
    )
    parser.add_argument(
        "--source",
        default=DEFAULT_SOURCE,
        help="Git source URL or local repository path",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and print the planned clone without writing files",
    )
    args = parser.parse_args()

    try:
        destination = Path(args.destination)
        result = clone_course(args.source, destination, args.dry_run)
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))

    print(f"Result: {result}")
    print(f"Course: {destination.expanduser().resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
