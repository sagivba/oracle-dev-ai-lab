# /goal 011 - Add Release Packaging Workflow Skeleton

## Goal

Add a skeleton-only release packaging workflow that defines how Infrastructure MVP files will be gathered into a deterministic release package from versioned repository files.

## Prompt to use with Codex

```text
/goal
Add the release packaging workflow skeleton for oracle-dev-ai-lab.

Create or update only the files needed for a skeleton packaging workflow. Likely files include:
- scripts/package-release.sh
- tools/package_release.py
- db/dist/ release output structure documentation or placeholder
- docs/packaging-workflow.md
- tests/test_packaging_contract.py or equivalent unittest location
- docs/stages/stage-011-task-G011-release-packaging-workflow.html

The packaging skeleton should define or validate this release output contract:

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

Package content rules:
- Package output must be generated from managed, versioned repository files only.
- Package output must include a manifest.md contract.
- Package output must include an install.sql aggregation or package entry point skeleton.
- Package output must include a rollback.sql package reference.
- Package output must include a test-report.md placeholder or copied report contract.
- Package output must include the review-report.md inclusion contract.
- Package output must include deployment-notes.md.
- Package output must include only managed db/src files under the expected object-type folders.
- Package output must not include secrets.
- Package output must not include local .env or .env.* files.
- Package output must not include unmanaged database changes.
- Package output must not claim approval if review output contains BLOCKER findings.

Implementation rules:
- Keep this goal skeleton-only.
- Use Python unittest, not pytest.
- Keep dependencies minimal and prefer the Python standard library.
- Add a shell entry point only if it is safe by default and does not connect to Oracle.
- Add a Python packaging helper only if it is deterministic and repository-local.
- Add unittest coverage for the packaging contract.
- Add a standalone Hebrew HTML stage report under docs/stages/.
- Do not connect to organizational databases.
- Do not run ad-hoc DDL or DML.
- Do not add secrets, credentials, tokens, private keys, certificates, or real connection strings.

Out of scope:
- Goal 012.
- Real business release-management DB objects.
- Functional deployment logic.
- Organizational DB access.
- Secrets.
- Ad-hoc DDL or DML.
- Oracle runtime validation claims unless the relevant runtime scripts actually ran and passed.
- Oracle 19c compatibility claims unless explicitly tested later.
- APEX.
- ORDS.
- REST APIs.
- UI/frontend work.

Success criteria:
- Packaging skeleton files exist and are safe-by-default.
- Package contract is documented.
- Packaging contract unittest coverage exists and uses unittest.
- Packaging validation rejects or excludes secrets and local .env files.
- Packaging validation includes only managed DB source files.
- No functional release-management DB objects are created.
- Existing repository tests pass.

Run:
python -m unittest discover
scripts/test.sh quick
scripts/lint.sh
```

## Commit suggestion

```text
Add release packaging workflow skeleton
```
