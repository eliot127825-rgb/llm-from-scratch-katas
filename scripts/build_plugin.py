"""Build a clean skills-only Codex plugin archive.

The training repository contains kata source files, while the installed plugin only
needs its manifest and bundled Skill. The Skill can discover an existing checkout or
initialize the public Trial Edition after the learner confirms a destination.
"""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
import zipfile
from pathlib import Path


PLUGIN_NAME = "llm-from-scratch-katas"
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def read_manifest(root: Path) -> dict[str, object]:
    manifest_path = root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"Missing plugin manifest: {manifest_path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid plugin manifest JSON: {error}") from error

    if manifest.get("name") != PLUGIN_NAME:
        raise ValueError(f"Plugin name must be {PLUGIN_NAME!r}")
    version = manifest.get("version")
    if not isinstance(version, str) or not version.strip():
        raise ValueError("Plugin version must be a non-empty string")
    if manifest.get("skills") != "./skills/":
        raise ValueError("Plugin skills path must be './skills/'")
    return manifest


def included_files(root: Path) -> list[Path]:
    sources = [root / ".codex-plugin", root / "skills"]
    files: list[Path] = []
    for source in sources:
        if not source.is_dir():
            raise ValueError(f"Missing plugin component: {source}")
        for path in source.rglob("*"):
            relative = path.relative_to(root)
            if (
                path.is_file()
                and not EXCLUDED_PARTS.intersection(relative.parts)
                and path.suffix not in EXCLUDED_SUFFIXES
            ):
                files.append(path)
    if not any(path.name == "SKILL.md" for path in files):
        raise ValueError("Plugin archive must contain at least one SKILL.md")
    return sorted(files, key=lambda path: path.as_posix())


def build_archive(root: Path, output: Path) -> Path:
    manifest = read_manifest(root)
    files = included_files(root)
    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="ml-katas-plugin-") as temporary:
        temporary_archive = Path(temporary) / output.name
        with zipfile.ZipFile(
            temporary_archive,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for path in files:
                archive.write(path, path.relative_to(root).as_posix())
        shutil.copyfile(temporary_archive, output)

    print(f"Plugin: {manifest['name']} {manifest['version']}")
    print(f"Files: {len(files)}")
    print(f"Archive: {output}")
    return output


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest = read_manifest(root)
    default_output = (
        root
        / "dist"
        / f"{PLUGIN_NAME}-plugin-{manifest['version']}.zip"
    )

    parser = argparse.ArgumentParser(
        description="Build the ML Katas skills-only Codex plugin ZIP"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=default_output,
        help=f"Output ZIP path (default: {default_output})",
    )
    args = parser.parse_args()

    try:
        build_archive(root, args.output)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
