"""Run tests for exactly one kata from a safe working directory."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from kata_status import (
    collect_katas,
    find_project_root,
    load_learner_profile,
    recommend,
)


def choose_python(root: Path) -> Path:
    candidates = (
        root / ".venv" / "Scripts" / "python.exe",
        root / ".venv" / "bin" / "python",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return Path(sys.executable)


def resolve_kata(root: Path, requested: str | None) -> Path:
    katas_root = (root / "katas").resolve()

    if requested:
        relative = Path(requested)
        if relative.parts and relative.parts[0] == "katas":
            relative = Path(*relative.parts[1:])
        target = (katas_root / relative).resolve()
    else:
        selected = recommend(
            collect_katas(root),
            load_learner_profile(root),
        )
        if selected is None:
            raise ValueError("No unfinished or started kata was found")
        target = (root / selected["path"]).resolve()

    try:
        target.relative_to(katas_root)
    except ValueError as error:
        raise ValueError("The kata path must stay inside the course katas directory") from error

    required = ("README.md", "implementation.py", "test_implementation.py")
    if not target.is_dir() or not all((target / name).is_file() for name in required):
        raise ValueError(f"Not a valid kata directory: {target}")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run or collect tests for one Trial Edition kata"
    )
    parser.add_argument("--root", help="Path to the Trial Edition course")
    parser.add_argument(
        "--kata",
        help="Kata path relative to katas/, for example 01_python_dsa/001_count_labels",
    )
    parser.add_argument(
        "--collect-only",
        action="store_true",
        help="Collect tests without running the unfinished implementation",
    )
    args = parser.parse_args()

    try:
        root = find_project_root(args.root)
        target = resolve_kata(root, args.kata)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))

    python = choose_python(root)
    command = [str(python), "-m", "pytest", "-q", "-p", "no:cacheprovider"]
    if args.collect_only:
        command.append("--collect-only")
    command.append(".")

    print(f"Course: {root}", flush=True)
    print(f"Kata: {target.relative_to(root)}", flush=True)
    print(f"Python: {python}", flush=True)
    print(
        "Running only this kata; other exercises are not affected.",
        flush=True,
    )

    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        command,
        cwd=target,
        env=environment,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
