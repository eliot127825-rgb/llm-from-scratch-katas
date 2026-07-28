"""Validate kata structure and Python syntax without solving the exercises."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = {
    "README.md",
    "implementation.py",
    "test_implementation.py",
    "mistakes.md",
}
REQUIRED_ROOT_FILES = {
    "README.md",
    "EDITION.json",
    "EDITIONS.md",
    "CATALOG.md",
    "ROADMAP.md",
    "PROGRESS.md",
    "ENVIRONMENT.md",
    "requirements.txt",
}
MODULE_PATTERN = re.compile(r"^(\d{2})_[a-z0-9_]+$")
KATA_PATTERN = re.compile(r"^(\d{3})_[a-z0-9_]+$")


def validate_python(path: Path) -> list[str]:
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError, UnicodeError) as error:
        return [f"{path}: {error}"]
    return []


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    katas_root = root / "katas"

    if not katas_root.is_dir():
        return [f"Missing kata root: {katas_root}"]

    missing_root_files = REQUIRED_ROOT_FILES.difference(
        path.name for path in root.iterdir() if path.is_file()
    )
    if missing_root_files:
        errors.append(
            f"{root}: missing {', '.join(sorted(missing_root_files))}"
        )

    kata_count = 0
    module_numbers: list[int] = []
    for module in sorted(path for path in katas_root.iterdir() if path.is_dir()):
        module_match = MODULE_PATTERN.fullmatch(module.name)
        if not module_match:
            errors.append(f"Invalid module directory name: {module}")
            continue

        module_numbers.append(int(module_match.group(1)))
        if not (module / "README.md").is_file():
            errors.append(f"{module}: missing module README.md")

        numbers: list[int] = []
        for kata in sorted(path for path in module.iterdir() if path.is_dir()):
            match = KATA_PATTERN.fullmatch(kata.name)
            if not match:
                errors.append(f"Invalid kata directory name: {kata}")
                continue

            kata_count += 1
            numbers.append(int(match.group(1)))
            missing = REQUIRED_FILES.difference(
                path.name for path in kata.iterdir() if path.is_file()
            )
            if missing:
                errors.append(
                    f"{kata}: missing {', '.join(sorted(missing))}"
                )

            for python_file in sorted(kata.glob("*.py")):
                errors.extend(validate_python(python_file))

        if numbers and numbers != list(range(1, len(numbers) + 1)):
            errors.append(
                f"{module}: kata numbers must be consecutive from 001; got {numbers}"
            )

    if module_numbers != list(range(1, len(module_numbers) + 1)):
        errors.append(
            "Module numbers must be unique and consecutive from 01; "
            f"got {module_numbers}"
        )

    if kata_count == 0:
        errors.append("No kata directories found")

    edition_path = root / "EDITION.json"
    if edition_path.is_file():
        try:
            edition = json.loads(edition_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            errors.append(f"{edition_path}: {error}")
        else:
            if edition.get("schema_version") != 1:
                errors.append(f"{edition_path}: schema_version must be 1")
            if edition.get("edition") not in {"trial", "complete"}:
                errors.append(
                    f"{edition_path}: edition must be 'trial' or 'complete'"
                )
            if edition.get("distribution") not in {"public", "private"}:
                errors.append(
                    f"{edition_path}: distribution must be 'public' or 'private'"
                )
            if edition.get("kata_count") != kata_count:
                errors.append(
                    f"{edition_path}: kata_count is {edition.get('kata_count')}, "
                    f"but found {kata_count}"
                )

    for python_file in sorted((root / "templates").rglob("*.py")):
        errors.extend(validate_python(python_file))

    for python_file in sorted((root / "skills").rglob("*.py")):
        errors.extend(validate_python(python_file))

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    kata_count = sum(
        1
        for path in (root / "katas").glob("*/*")
        if path.is_dir() and KATA_PATTERN.fullmatch(path.name)
    )
    print(f"Repository validation passed: {kata_count} katas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
