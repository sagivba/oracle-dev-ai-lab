# /goal 011 - Add Release Packaging Workflow Skeleton

## Goal

Add release packaging workflow that creates a deterministic release package from versioned files.

## Prompt to use with Codex

```text
/goal
Add the release packaging workflow skeleton for oracle-dev-ai-lab.

Create or update:
- scripts/package-release.sh
- tools/package_release.py
- db/dist/README.md
- docs/packaging-workflow.md
- tests/test_packaging_contract.py or equivalent unittest location

Package structure must target:

db/dist/release_001/
  manifest.md
  install.sql
  rollback.sql
  test-report.md
  review-report.md
  deployment-notes.md
  src/
    tables/
    constraints/
    indexes/
    views/
    packages/
    triggers/
    seed/

Rules:
- Package must be built from versioned repository files.
- Package must not include secrets.
- Package must include manifest, test report, review report, and deployment notes.
- Package must not be approved if review has BLOCKER findings.
- Do not create a functional release-management package yet.

Success criteria:
- Packaging script exists and supports a dry-run or help mode.
- Python unittest validates expected package contract or generated placeholder structure.
- Existing tests pass.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add release packaging workflow skeleton
```
