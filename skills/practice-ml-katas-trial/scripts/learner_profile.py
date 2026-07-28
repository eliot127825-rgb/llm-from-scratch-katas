"""Create and inspect a private local learner profile from diagnostic scores."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from kata_status import find_project_root


DIMENSIONS = (
    "python_basics",
    "debugging",
    "shape_reasoning",
    "ml_concepts",
    "algorithm_expression",
)


def level_for_score(score: int) -> dict[str, object]:
    if score <= 2:
        return {
            "level": "starter",
            "label": "Starter",
            "preferred_difficulties": ["Beginner"],
            "teaching_mode": "maximum_scaffolding",
        }
    if score <= 5:
        return {
            "level": "foundation",
            "label": "Foundation",
            "preferred_difficulties": ["Beginner", "Easy"],
            "teaching_mode": "detailed_guidance",
        }
    if score <= 8:
        return {
            "level": "guided",
            "label": "Guided",
            "preferred_difficulties": ["Easy", "Medium"],
            "teaching_mode": "guided_problem_solving",
        }
    return {
        "level": "independent",
        "label": "Independent",
        "preferred_difficulties": ["Medium"],
        "teaching_mode": "concise_challenge",
    }


def profile_path(root: Path) -> Path:
    return root / ".local" / "learner_profile.json"


def build_profile(
    scores: dict[str, int],
    strengths: list[str],
    support_needs: list[str],
) -> dict[str, object]:
    for dimension in DIMENSIONS:
        value = scores.get(dimension)
        if not isinstance(value, int) or not 0 <= value <= 2:
            raise ValueError(f"{dimension} must be an integer from 0 to 2")

    total = sum(scores.values())
    level = level_for_score(total)
    return {
        "schema_version": 1,
        "assessment": "five_dimension_trial_diagnostic",
        "assessed_at": datetime.now(timezone.utc).isoformat(),
        "score": total,
        "max_score": 10,
        **level,
        "dimensions": scores,
        "strengths": strengths,
        "support_needs": support_needs,
        "raw_answers_stored": False,
    }


def save_profile(root: Path, profile: dict[str, object]) -> Path:
    destination = profile_path(root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return destination


def load_profile(root: Path) -> dict[str, object]:
    source = profile_path(root)
    if not source.is_file():
        raise FileNotFoundError(f"No learner profile found: {source}")
    return json.loads(source.read_text(encoding="utf-8"))


def add_score_arguments(parser: argparse.ArgumentParser) -> None:
    for dimension in DIMENSIONS:
        parser.add_argument(
            f"--{dimension.replace('_', '-')}",
            required=True,
            type=int,
            choices=(0, 1, 2),
        )
    parser.add_argument(
        "--strength",
        action="append",
        default=[],
        help="Short evidence-based strength; may be repeated",
    )
    parser.add_argument(
        "--support",
        action="append",
        default=[],
        help="Short evidence-based support need; may be repeated",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Manage the private local ML Katas learner profile"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    save_parser = subparsers.add_parser("save")
    save_parser.add_argument("--root", help="Path to the Trial Edition course")
    add_score_arguments(save_parser)

    show_parser = subparsers.add_parser("show")
    show_parser.add_argument("--root", help="Path to the Trial Edition course")

    args = parser.parse_args()
    try:
        root = find_project_root(args.root)
        if args.command == "save":
            scores = {
                dimension: getattr(args, dimension)
                for dimension in DIMENSIONS
            }
            profile = build_profile(scores, args.strength, args.support)
            destination = save_profile(root, profile)
            print(json.dumps(profile, ensure_ascii=False, indent=2))
            print(f"Saved locally: {destination}")
            return 0

        profile = load_profile(root)
        print(json.dumps(profile, ensure_ascii=False, indent=2))
        return 0
    except (FileNotFoundError, OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
        return 2


if __name__ == "__main__":
    sys.exit(main())
