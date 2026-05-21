# Purpose: Repository contract tests for Goal 005 of oracle-dev-ai-lab.

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestRepositoryContract(unittest.TestCase):
    """Validate the repository structure and core governance contracts."""

    def test_required_files_exist(self) -> None:
        required_files = [
            "AGENTS.md",
            "TODO.md",
            "docs/project-charter.md",
            "docs/safety-rules.md",
            "docs/decision-log.md",
            "docs/repository-structure.md",
            "docs/codex-workflow.md",
            "docs/testing-strategy.md",
            "scripts/test.sh",
            "scripts/lint.sh",
            "docker-compose.yml",
            "docs/docker-lab-design.md",
        ]

        for relative_path in required_files:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file(), relative_path)

    def test_required_directories_exist(self) -> None:
        required_directories = [
            "docs/stages",
            "db",
            "db/install",
            "db/src",
            "db/src/tables",
            "db/src/constraints",
            "db/src/indexes",
            "db/src/views",
            "db/src/packages",
            "db/src/triggers",
            "db/src/seed",
            "db/rollback",
            "db/tests",
            "db/tests/sql",
            "db/tests/utplsql",
            "db/review",
            "db/generated",
            "db/dist",
            "specs/001-release-management",
            "specs/001-release-management/tasks",
            "tools",
        ]

        for relative_path in required_directories:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_dir(), relative_path)

    def test_scripts_test_sh_supports_quick_and_full(self) -> None:
        test_script = (ROOT / "scripts/test.sh").read_text(encoding="utf-8")

        self.assertIn('MODE="${1:-quick}"', test_script)
        self.assertIn("quick)", test_script)
        self.assertIn("full)", test_script)
        self.assertIn('python -m unittest discover -s tests -p "test_*.py"', test_script)

    def test_python_testing_framework_is_unittest(self) -> None:
        test_script = (ROOT / "scripts/test.sh").read_text(encoding="utf-8")
        lint_script = (ROOT / "scripts/lint.sh").read_text(encoding="utf-8")

        self.assertNotIn("pytest", test_script)
        self.assertNotIn("pytest", lint_script)

        strategy_doc = (ROOT / "docs/testing-strategy.md").read_text(encoding="utf-8")
        self.assertIn("unittest", strategy_doc)
        self.assertIn("Do not require `pytest`.", strategy_doc)

    def test_goal_005_does_not_require_later_goal_artifacts(self) -> None:
        optional_paths = [
            "db/install/install.sql",
            "scripts/install-db.sh",
            "scripts/run-db-tests.sh",
            "scripts/review-db-code.sh",
            "scripts/package-release.sh",
        ]

        for relative_path in optional_paths:
            with self.subTest(path=relative_path):
                path = ROOT / relative_path
                self.assertTrue(
                    not path.exists() or path.is_file(),
                    relative_path,
                )
