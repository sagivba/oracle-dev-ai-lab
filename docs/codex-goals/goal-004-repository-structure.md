# /goal 004 - Create Oracle Lab Repository Structure

## Goal

Add the Oracle lab folder structure while preserving the useful Python template structure.

## Prompt to use with Codex

```text
/goal
Create the repository structure for oracle-dev-ai-lab.

Add these directories if missing:
- docs/
- specs/001-release-management/tasks/
- db/install/
- db/src/tables/
- db/src/constraints/
- db/src/indexes/
- db/src/views/
- db/src/packages/
- db/src/triggers/
- db/src/seed/
- db/rollback/
- db/tests/sql/
- db/tests/utplsql/
- db/review/
- db/generated/
- db/dist/
- scripts/
- tools/

If the Python template uses src/ and tests/, preserve them.
Do not move Python package files unless required by existing project configuration.
Do not create real Oracle implementation yet.
Use placeholder README.md files only where needed to keep empty directories in Git.

Create or update docs/repository-structure.md with the intended final structure and purpose of each folder.

Success criteria:
- Required Oracle lab folders exist.
- Empty folders intended for future use are tracked with README.md or .gitkeep.
- Existing Python tests still run.
- No DB implementation is added yet.

Run:
python -m unittest discover
```

## Commit suggestion

```text
Add Oracle lab repository structure
```
