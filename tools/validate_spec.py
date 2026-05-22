"""Purpose: Validate semantic spec skeleton files without DB access."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from extract_spec import DEFAULT_OUTPUT, DEFAULT_SPEC, extract_spec, validate_spec_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate required sections and stable IDs in the semantic spec."
    )
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC, help="Path to spec.html.")
    parser.add_argument(
        "--json",
        dest="json_path",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Optional extracted spec.json to compare when it exists.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    extracted_payload = extract_spec(args.spec)
    errors = validate_spec_payload(extracted_payload)

    if args.json_path.exists():
        stored_payload = json.loads(args.json_path.read_text(encoding="utf-8"))
        if stored_payload != extracted_payload:
            errors.append(f"{args.json_path.as_posix()} is not in sync with {args.spec.as_posix()}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Spec validation passed: {args.spec.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
