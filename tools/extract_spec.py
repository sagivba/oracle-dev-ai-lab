"""Purpose: Extract Goal 009 semantic HTML specs into deterministic JSON."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

DEFAULT_SPEC = Path("specs/001-release-management/spec.html")
DEFAULT_OUTPUT = Path("specs/001-release-management/spec.json")
ID_PATTERN = re.compile(r"^(REQ|AC)-\d{3}$")
REQUIRED_SECTION_IDS = (
    "business-goal",
    "scope",
    "out-of-scope",
    "entities",
    "acceptance-criteria",
)


def _clean_text(parts: list[str]) -> str:
    return " ".join(" ".join(parts).split())


class SpecHTMLParser(HTMLParser):
    """Collect the intentionally small semantic subset used by Goal 009."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.article: dict[str, str] = {}
        self.sections: list[dict[str, Any]] = []
        self._current_section: dict[str, Any] | None = None
        self._current_item: dict[str, Any] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {name: value or "" for name, value in attrs}

        if tag == "article" and attr_map.get("id") == "spec":
            self.article = attr_map
            return

        if tag == "section":
            self._current_section = {
                "id": attr_map.get("id", ""),
                "title": attr_map.get("data-title", ""),
                "required": attr_map.get("data-required", "false").lower() == "true",
                "optional_for": attr_map.get("data-optional-for", ""),
                "text_parts": [],
                "requirements": [],
                "acceptance_criteria": [],
            }
            self.sections.append(self._current_section)
            return

        if tag == "li" and self._current_section is not None:
            if "data-requirement-id" in attr_map and "data-acceptance-id" not in attr_map:
                self._current_item = {
                    "kind": "requirement",
                    "id": attr_map["data-requirement-id"],
                    "section": self._current_section["id"],
                    "text_parts": [],
                }
            elif "data-acceptance-id" in attr_map:
                self._current_item = {
                    "kind": "acceptance",
                    "id": attr_map["data-acceptance-id"],
                    "requirement_id": attr_map.get("data-requirement-id", ""),
                    "section": self._current_section["id"],
                    "text_parts": [],
                }

    def handle_data(self, data: str) -> None:
        if self._current_item is not None:
            self._current_item["text_parts"].append(data)
        elif self._current_section is not None:
            self._current_section["text_parts"].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "li" and self._current_item is not None and self._current_section is not None:
            item = {
                key: value
                for key, value in self._current_item.items()
                if key not in {"kind", "text_parts"}
            }
            item["text"] = _clean_text(self._current_item["text_parts"])

            if self._current_item["kind"] == "requirement":
                self._current_section["requirements"].append(item)
            else:
                self._current_section["acceptance_criteria"].append(item)

            self._current_item = None
            return

        if tag == "section" and self._current_section is not None:
            self._current_section["summary"] = _clean_text(self._current_section["text_parts"])
            self._current_section.pop("text_parts", None)
            self._current_section = None


def extract_spec(spec_path: Path = DEFAULT_SPEC) -> dict[str, Any]:
    parser = SpecHTMLParser()
    parser.feed(spec_path.read_text(encoding="utf-8"))

    requirements = [
        requirement
        for section in parser.sections
        for requirement in section["requirements"]
    ]
    acceptance_criteria = [
        criterion
        for section in parser.sections
        for criterion in section["acceptance_criteria"]
    ]

    return {
        "_purpose": "Goal 009 deterministic spec extraction output.",
        "generated_by": "tools/extract_spec.py",
        "schema_version": "0.1.0",
        "source": spec_path.as_posix(),
        "spec": {
            "id": parser.article.get("data-spec-id", ""),
            "version": parser.article.get("data-version", ""),
            "goal_id": parser.article.get("data-goal-id", ""),
        },
        "sections": parser.sections,
        "requirements": requirements,
        "acceptance_criteria": acceptance_criteria,
    }


def validate_spec_payload(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    section_map = {section["id"]: section for section in payload.get("sections", [])}

    if not payload.get("spec", {}).get("id"):
        errors.append("missing spec id")

    for section_id in REQUIRED_SECTION_IDS:
        section = section_map.get(section_id)
        if section is None:
            errors.append(f"missing required section: {section_id}")
        elif not section.get("required"):
            errors.append(f"section must be marked required: {section_id}")

    plsql_section = section_map.get("plsql-api")
    if plsql_section is None:
        errors.append("missing optional PL/SQL API section")
    elif plsql_section.get("required"):
        errors.append("PL/SQL API section must be optional for the Infrastructure MVP")

    requirement_ids = [item["id"] for item in payload.get("requirements", [])]
    acceptance_ids = [item["id"] for item in payload.get("acceptance_criteria", [])]

    if not requirement_ids:
        errors.append("no requirement ids found")
    if not acceptance_ids:
        errors.append("no acceptance criteria ids found")

    for item_id in requirement_ids + acceptance_ids:
        if not ID_PATTERN.match(item_id):
            errors.append(f"invalid stable id format: {item_id}")

    if len(requirement_ids) != len(set(requirement_ids)):
        errors.append("duplicate requirement ids found")
    if len(acceptance_ids) != len(set(acceptance_ids)):
        errors.append("duplicate acceptance criteria ids found")

    known_requirements = set(requirement_ids)
    for criterion in payload.get("acceptance_criteria", []):
        requirement_id = criterion.get("requirement_id", "")
        if requirement_id and requirement_id not in known_requirements:
            errors.append(f"acceptance criterion references missing requirement: {requirement_id}")

    return errors


def write_json(payload: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract the Goal 009 semantic HTML spec into deterministic JSON."
    )
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC, help="Path to spec.html.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Path for spec.json.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate only; do not write output.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    payload = extract_spec(args.spec)
    errors = validate_spec_payload(payload)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    if not args.check:
        write_json(payload, args.output)
        print(f"Wrote {args.output.as_posix()}")
    else:
        print(f"Validated {args.spec.as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
