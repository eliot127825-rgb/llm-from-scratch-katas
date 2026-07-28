"""Report whether a beginner can start the Trial Edition course."""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from pathlib import Path

from kata_status import (
    collect_katas,
    find_project_root,
    load_learner_profile,
    read_edition,
    recommend,
)


REQUIRED_PACKAGES = ("numpy", "pytest")


def package_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def inspect_environment(explicit_root: str | None = None) -> dict[str, object]:
    checks: list[dict[str, object]] = []

    python_ok = sys.version_info >= (3, 10)
    checks.append(
        {
            "name": "python",
            "ok": python_ok,
            "detail": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        }
    )

    checks.append(
        {
            "name": "virtual_environment",
            "ok": sys.prefix != sys.base_prefix,
            "detail": sys.executable,
            "required": False,
        }
    )

    checks.append(
        {
            "name": "git",
            "ok": shutil.which("git") is not None,
            "detail": shutil.which("git") or "not found",
            "required": False,
        }
    )

    missing_packages: list[str] = []
    for package in REQUIRED_PACKAGES:
        available = package_available(package)
        if not available:
            missing_packages.append(package)
        checks.append(
            {
                "name": f"package:{package}",
                "ok": available,
                "detail": "available" if available else "missing",
            }
        )

    root: Path | None
    try:
        root = find_project_root(explicit_root)
    except FileNotFoundError:
        root = None

    if root is None:
        checks.append(
            {
                "name": "course",
                "ok": False,
                "detail": "Trial Edition checkout not found",
            }
        )
        edition: dict[str, object] | None = None
        rows: list[dict[str, str]] = []
        next_kata: dict[str, str] | None = None
    else:
        edition = read_edition(root)
        edition_ok = edition.get("edition") == "trial"
        checks.append(
            {
                "name": "course",
                "ok": edition_ok,
                "detail": f"{edition.get('display_name')} at {root}",
            }
        )
        rows = collect_katas(root)
        profile = load_learner_profile(root)
        next_kata = recommend(rows, profile)

    blocking = [
        check["name"]
        for check in checks
        if not check["ok"] and check.get("required", True)
    ]

    if root is None:
        next_action = "Initialize or locate the Trial Edition course checkout."
    elif not python_ok:
        next_action = "Use Python 3.10 or newer."
    elif missing_packages:
        next_action = (
            "Install the missing packages in a project-local environment: "
            + ", ".join(missing_packages)
        )
    elif next_kata:
        next_action = f"Start: {next_kata['path']}"
    else:
        next_action = "All discovered kata implementations have been started."

    return {
        "ready": not blocking,
        "python_executable": sys.executable,
        "course_root": str(root) if root else None,
        "edition": edition,
        "kata_count": len(rows),
        "recommended": next_kata,
        "learner_profile": profile if root else None,
        "diagnostic_recommended": bool(root and profile is None),
        "checks": checks,
        "blocking": blocking,
        "next_action": next_action,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check whether the learner can start the Trial Edition"
    )
    parser.add_argument("--root", help="Path to the Trial Edition course")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    report = inspect_environment(args.root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("ML Katas beginner check")
        for check in report["checks"]:
            marker = "OK" if check["ok"] else (
                "INFO" if not check.get("required", True) else "ACTION"
            )
            print(f"[{marker}] {check['name']}: {check['detail']}")
        print(f"Next: {report['next_action']}")

    return 0 if report["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
