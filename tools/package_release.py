"""Purpose: Build the deterministic Oracle AI Lab release package.

The helper packages only managed repository DB source files into db/dist and
generates release metadata without Docker, Oracle, DB connections, DDL, or DML.
It provides a reproducible package artifact from tracked source files while the
release remains explicitly not approved until review evidence allows approval.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RELEASE_NAME = "release_001"
DIST_ROOT = REPO_ROOT / "db" / "dist"
RELEASE_ROOT = DIST_ROOT / RELEASE_NAME
REVIEW_REPORT = REPO_ROOT / "db" / "review" / "review-report.md"
EMPTY_FOLDER_MARKER = "README.md"

OBJECT_TYPE_DIRS = (
    "tables",
    "constraints",
    "indexes",
    "views",
    "packages",
    "triggers",
    "seed",
)

SECRET_FILENAME_PATTERNS = (
    re.compile(r"(^|/)\.env(\..*)?$"),
    re.compile(r"(?i)(secret|token|password|passwd|private[_-]?key|id_rsa|\.pem$|\.p12$|\.pfx$)"),
)

SECRET_CONTENT_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)\b(api[_-]?key|token|secret|password|passwd)\s*=\s*[^;\s]+"),
)


def relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def fail(message: str) -> None:
    raise RuntimeError(message)


def require_repository_root() -> None:
    required = ["AGENTS.md", "db/install/install.sql", "scripts/package-release.sh"]
    for path in required:
        if not (REPO_ROOT / path).is_file():
            fail(f"Missing required repository file: {path}")


def tracked_files() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def ensure_tracked(path: Path, tracked: set[str]) -> None:
    rel_path = relative(path)
    if rel_path not in tracked:
        fail(f"Required package source is not tracked by Git: {rel_path}")


def assert_safe_release_root() -> None:
    dist_root = DIST_ROOT.resolve()
    release_root = RELEASE_ROOT.resolve()
    if release_root.parent != dist_root or release_root.name != RELEASE_NAME:
        fail("Release output path is outside the approved db/dist release directory.")


def prepare_release_tree() -> None:
    assert_safe_release_root()
    if RELEASE_ROOT.exists():
        shutil.rmtree(RELEASE_ROOT)

    for folder in OBJECT_TYPE_DIRS:
        (RELEASE_ROOT / "src" / folder).mkdir(parents=True, exist_ok=True)


def path_looks_secret(rel_path: str) -> bool:
    return any(pattern.search(rel_path) for pattern in SECRET_FILENAME_PATTERNS)


def content_looks_secret(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    return any(pattern.search(text) for pattern in SECRET_CONTENT_PATTERNS)


def managed_source_files(tracked: set[str]) -> list[tuple[str, str]]:
    package_files: list[tuple[str, str]] = []

    for folder in OBJECT_TYPE_DIRS:
        source_dir = REPO_ROOT / "db" / "src" / folder
        if not source_dir.is_dir():
            fail(f"Missing managed DB source folder: {relative(source_dir)}")

        for path in sorted(source_dir.rglob("*.sql")):
            rel_path = relative(path)
            ensure_tracked(path, tracked)
            if path_looks_secret(rel_path) or content_looks_secret(path):
                fail(f"Refusing to package possible secret-bearing file: {rel_path}")

            package_rel = (Path("src") / folder / path.relative_to(source_dir)).as_posix()
            package_files.append((rel_path, package_rel))

    return package_files


def copy_managed_sources(package_files: list[tuple[str, str]]) -> None:
    for source_rel, package_rel in package_files:
        destination = RELEASE_ROOT / package_rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / source_rel, destination)


def render_empty_folder_marker(folder: str) -> str:
    return f"""# Purpose

This marker keeps the `src/{folder}/` release package folder represented in Git.
Git does not track empty directories, and no managed SQL files exist for this
object type in this generated release package.

# Package Folder Status

- Object type folder: `src/{folder}/`
- Managed SQL files: none
- Scope: release package folder contract metadata
"""


def write_empty_folder_markers(package_files: list[tuple[str, str]]) -> None:
    populated_folders = {Path(package_rel).parts[1] for _, package_rel in package_files}

    for folder in OBJECT_TYPE_DIRS:
        if folder in populated_folders:
            continue
        marker_path = RELEASE_ROOT / "src" / folder / EMPTY_FOLDER_MARKER
        write_text(marker_path, render_empty_folder_marker(folder))


def review_report_has_blocker_finding(text: str) -> bool:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- BLOCKER:") or stripped.startswith("BLOCKER:"):
            return True
        if stripped.startswith("Severity: BLOCKER"):
            return True
    return False


def validate_review_report(tracked: set[str]) -> tuple[str, bool]:
    if not REVIEW_REPORT.is_file():
        fail("Missing required review report: db/review/review-report.md")

    ensure_tracked(REVIEW_REPORT, tracked)
    text = REVIEW_REPORT.read_text(encoding="utf-8")
    if "A release package is not approved if any BLOCKER exists." not in text:
        fail("Review report is missing the required BLOCKER approval rule.")
    if "## Approval status" not in text:
        fail("Review report is missing the required approval status section.")

    shutil.copy2(REVIEW_REPORT, RELEASE_ROOT / "review-report.md")
    return text, review_report_has_blocker_finding(text)


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def grouped_package_files(package_files: list[tuple[str, str]]) -> dict[str, list[tuple[str, str]]]:
    grouped = {folder: [] for folder in OBJECT_TYPE_DIRS}
    for source_rel, package_rel in package_files:
        folder = Path(package_rel).parts[1]
        grouped[folder].append((source_rel, package_rel))
    return grouped


def render_manifest(package_files: list[tuple[str, str]], blocker_found: bool) -> str:
    lines = [
        "# Purpose",
        "",
        "This manifest is generated by the packaging workflow for `oracle-dev-ai-lab`.",
        "It records deterministic package contents and keeps the release explicitly",
        "not approved until concrete review evidence allows approval.",
        "",
        "# Release Manifest",
        "",
        f"- Release package: `{RELEASE_NAME}`",
        "- Approval status: NOT APPROVED - review approval not recorded",
        "- Review report: `review-report.md` copied from `db/review/review-report.md`",
        "- BLOCKER rule: a release package is not approved if any BLOCKER exists",
        f"- BLOCKER findings detected by packaging helper: {'YES' if blocker_found else 'NO'}",
        "- Oracle runtime validation: NOT RUN",
        "- Functional release-management DB objects: NOT INCLUDED",
        "",
        "## Package Files",
        "",
        "- `install.sql`",
        "- `rollback.sql`",
        "- `test-report.md`",
        "- `review-report.md`",
        "- `deployment-notes.md`",
        "",
        "## Managed DB Source Files",
        "",
    ]

    grouped = grouped_package_files(package_files)
    for folder in OBJECT_TYPE_DIRS:
        lines.append(f"### src/{folder}")
        entries = grouped[folder]
        if not entries:
            lines.append("")
            lines.append("- No managed SQL source files in this folder.")
        else:
            lines.append("")
            for source_rel, package_rel in entries:
                lines.append(f"- `{source_rel}` -> `{package_rel}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_install_sql(package_files: list[tuple[str, str]]) -> str:
    lines = [
        "-- Purpose: Generated release package install entry point.",
        "-- It documents package contents only and intentionally does not execute DDL",
        "-- or DML. Functional deployment logic belongs to later approved goals.",
        "",
        "prompt Oracle AI Lab release_001 install skeleton",
        "prompt This skeleton package is not approved for deployment.",
        "",
        "-- Managed source files included in deterministic order:",
    ]

    if not package_files:
        lines.append("-- No managed SQL source files are included yet.")
    else:
        for source_rel, package_rel in package_files:
            lines.append(f"-- {source_rel} -> {package_rel}")

    return "\n".join(lines) + "\n"


def render_rollback_sql(package_files: list[tuple[str, str]]) -> str:
    lines = [
        "-- Purpose: Generated release package rollback reference.",
        "-- It documents rollback scope only and intentionally does not execute DDL",
        "-- or DML. Functional rollback logic belongs to later approved goals.",
        "",
        "prompt Oracle AI Lab release_001 rollback skeleton",
        "prompt This skeleton package is not approved for deployment.",
        "",
        "-- Rollback must remain tied to managed repository files.",
    ]

    if package_files:
        lines.append("-- Packaged source files that future rollback planning must consider:")
        for source_rel, package_rel in package_files:
            lines.append(f"-- {source_rel} -> {package_rel}")
    else:
        lines.append("-- No managed SQL source files are included yet.")

    return "\n".join(lines) + "\n"


def render_test_report() -> str:
    return """# Purpose

This generated test report records the release package validation contract. It
does not claim Oracle runtime validation, Docker validation, install validation,
or functional release-management validation unless those checks are recorded by
the current release process.

# Test Report

Status: SKELETON

- Repository unittest and script checks must be recorded outside this generated
  placeholder by the current Codex task.
- Oracle runtime validation was not run by the packaging helper.
- The release package is not approved for deployment.
"""


def render_deployment_notes(blocker_found: bool) -> str:
    blocker_text = "yes" if blocker_found else "no"
    return f"""# Purpose

These deployment notes describe the release package boundaries for
`oracle-dev-ai-lab`. They are generated from repository files only and do not
contain functional deployment instructions.

# Deployment Notes

## Scope

- Skeleton-only release package contract.
- No functional release-management DB objects were added.
- No organizational database access is required or allowed.
- No secrets, `.env`, or `.env.*` files are packaged.

## Approval

- Approval status: NOT APPROVED - skeleton package only.
- Review BLOCKER findings detected by helper: {blocker_text}.
- A release package is not approved if any BLOCKER exists.

## Runtime Validation

Oracle runtime validation was not run by the packaging workflow and is not
claimed by this package.
"""


def write_generated_files(package_files: list[tuple[str, str]], blocker_found: bool) -> None:
    write_text(RELEASE_ROOT / "manifest.md", render_manifest(package_files, blocker_found))
    write_text(RELEASE_ROOT / "install.sql", render_install_sql(package_files))
    write_text(RELEASE_ROOT / "rollback.sql", render_rollback_sql(package_files))
    write_text(RELEASE_ROOT / "test-report.md", render_test_report())
    write_text(RELEASE_ROOT / "deployment-notes.md", render_deployment_notes(blocker_found))


def build_release_package() -> None:
    require_repository_root()
    tracked = tracked_files()
    prepare_release_tree()
    package_files = managed_source_files(tracked)
    copy_managed_sources(package_files)
    write_empty_folder_markers(package_files)
    _, blocker_found = validate_review_report(tracked)
    write_generated_files(package_files, blocker_found)


def main() -> int:
    try:
        build_release_package()
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1

    print(f"Release package skeleton written: {relative(RELEASE_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
