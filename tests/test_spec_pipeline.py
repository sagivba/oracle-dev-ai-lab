# Purpose: unittest coverage for the release-management specification pipeline placeholder.

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = ROOT / "specs" / "001-release-management"
SPEC_HTML = SPEC_DIR / "spec.html"
SPEC_JSON = SPEC_DIR / "spec.json"
SPEC_TODO = SPEC_DIR / "TODO.md"
TRACEABILITY = SPEC_DIR / "traceability-matrix.md"
TASK_PLACEHOLDER = SPEC_DIR / "tasks" / "T001-spec-pipeline-placeholder.md"


class TestSpecPipeline(unittest.TestCase):
    """Validate the release-management specification pipeline placeholder.

    The checks stay local and avoid external services.
    """

    def run_tool(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_required_spec_files_exist(self) -> None:
        for path in [
            SPEC_HTML,
            SPEC_JSON,
            SPEC_TODO,
            TRACEABILITY,
            TASK_PLACEHOLDER,
        ]:
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_semantic_sections_and_stable_ids_exist(self) -> None:
        html = SPEC_HTML.read_text(encoding="utf-8")

        for section_id in [
            "business-goal",
            "scope",
            "out-of-scope",
            "entities",
            "plsql-api",
            "acceptance-criteria",
        ]:
            with self.subTest(section=section_id):
                self.assertIn(f'id="{section_id}"', html)

        for stable_id in ["REQ-001", "REQ-002", "REQ-003", "REQ-004"]:
            with self.subTest(requirement=stable_id):
                self.assertIn(stable_id, html)

        for stable_id in ["AC-001", "AC-002", "AC-003", "AC-004"]:
            with self.subTest(acceptance=stable_id):
                self.assertIn(stable_id, html)

    def test_plsql_api_section_is_optional_for_infrastructure_mvp(self) -> None:
        payload = json.loads(SPEC_JSON.read_text(encoding="utf-8"))
        section_map = {section["id"]: section for section in payload["sections"]}

        self.assertFalse(section_map["plsql-api"]["required"])
        self.assertEqual(section_map["plsql-api"]["optional_for"], "Goal 012 placeholder")

    def test_tools_support_help(self) -> None:
        for tool in [
            "tools/extract_spec.py",
            "tools/validate_spec.py",
            "tools/generate_todo.py",
            "tools/generate_tasks.py",
        ]:
            with self.subTest(tool=tool):
                result = self.run_tool(tool, "--help")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("usage:", result.stdout)

    def test_generated_outputs_are_current(self) -> None:
        commands = [
            ("tools/extract_spec.py", "--check"),
            ("tools/validate_spec.py",),
            ("tools/generate_todo.py", "--check"),
            ("tools/generate_tasks.py", "--check"),
        ]

        for command in commands:
            with self.subTest(command=command):
                result = self.run_tool(*command)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_extract_spec_output_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            first = Path(tmp_dir) / "first.json"
            second = Path(tmp_dir) / "second.json"

            first_result = self.run_tool("tools/extract_spec.py", "--output", str(first))
            second_result = self.run_tool("tools/extract_spec.py", "--output", str(second))

            self.assertEqual(first_result.returncode, 0, first_result.stderr)
            self.assertEqual(second_result.returncode, 0, second_result.stderr)
            self.assertEqual(first.read_text(encoding="utf-8"), second.read_text(encoding="utf-8"))

    def test_goal_012_documents_candidate_entities_as_future_scope_only(self) -> None:
        html = SPEC_HTML.read_text(encoding="utf-8")
        candidate_entities = [
            "RELEASE_REQUESTS",
            "RELEASE_ITEMS",
            "RELEASE_ENVIRONMENTS",
            "RELEASE_STATUSES",
            "RELEASE_APPROVALS",
            "RELEASE_EXECUTION_LOG",
        ]

        self.assertIn("planning candidates only", html)
        self.assertIn("must not be created", html)

        for token in candidate_entities:
            with self.subTest(token=token):
                self.assertIn(token, html)

    def test_candidate_entities_are_not_implemented_as_db_sources(self) -> None:
        checked_paths = [
            ROOT / "db" / "src" / "tables",
            ROOT / "db" / "src" / "constraints",
            ROOT / "db" / "src" / "indexes",
            ROOT / "db" / "src" / "views",
            ROOT / "db" / "src" / "packages",
            ROOT / "db" / "src" / "triggers",
            ROOT / "db" / "src" / "seed",
        ]
        candidate_entities = [
            "RELEASE_REQUESTS",
            "RELEASE_ITEMS",
            "RELEASE_ENVIRONMENTS",
            "RELEASE_STATUSES",
            "RELEASE_APPROVALS",
            "RELEASE_EXECUTION_LOG",
        ]

        for directory in checked_paths:
            for path in directory.rglob("*"):
                if not path.is_file():
                    continue
                content = path.read_text(encoding="utf-8")
                for token in candidate_entities:
                    with self.subTest(path=path, token=token):
                        self.assertNotIn(token, content)


if __name__ == "__main__":
    unittest.main()
