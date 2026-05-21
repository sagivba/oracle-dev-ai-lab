# Purpose: Repository contract tests for Goal 005 and Goal 007 of oracle-dev-ai-lab.

import re
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
            "docs/install-workflow.md",
            "scripts/test.sh",
            "scripts/lint.sh",
            "scripts/install-db.sh",
            "docker-compose.yml",
            "docs/docker-lab-design.md",
            "db/install/install.sql",
            "db/install/00_create_lab_users.sql",
            "db/install/01_create_schema.sql",
            "db/rollback/rollback.sql",
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

    def test_goal_007_install_sql_references_managed_files(self) -> None:
        install_sql = (ROOT / "db/install/install.sql").read_text(encoding="utf-8")

        self.assertIn("@@00_create_lab_users.sql", install_sql)
        self.assertIn("@@01_create_schema.sql", install_sql)
        self.assertNotIn("LAB_SMOKE_TEST", install_sql)

    def test_goal_007_install_script_targets_local_lab_only(self) -> None:
        install_script = (ROOT / "scripts/install-db.sh").read_text(encoding="utf-8")

        self.assertIn("db/install", install_script)
        self.assertIn("install.sql", install_script)
        self.assertIn("oracle-dev-ai-lab-db", install_script)
        self.assertIn("FREEPDB1", install_script)
        self.assertNotIn("LAB_SMOKE_TEST", install_script)

    def test_goal_007_files_do_not_contain_obvious_example_secrets(self) -> None:
        checked_files = [
            "db/install/install.sql",
            "db/install/00_create_lab_users.sql",
            "db/install/01_create_schema.sql",
            "db/rollback/rollback.sql",
            "scripts/install-db.sh",
            "docs/install-workflow.md",
        ]
        obvious_secret_pattern = re.compile(r"(?i)(oracle|welcome|passw(?:or)?d)[0-9]+")

        for relative_path in checked_files:
            content = (ROOT / relative_path).read_text(encoding="utf-8")
            with self.subTest(path=relative_path):
                self.assertIsNone(obvious_secret_pattern.search(content))

    def test_goal_005_does_not_require_later_goal_artifacts(self) -> None:
        optional_paths = [
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
