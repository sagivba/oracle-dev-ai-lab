# /goal 007 - Add Database Install Workflow Skeleton

## Goal

Create controlled DB installation workflow and lab user SQL skeletons.

## Prompt to use with Codex

```text
/goal
Add the controlled database installation workflow for oracle-dev-ai-lab.

Create or update:
- db/install/install.sql
- db/install/00_create_lab_users.sql
- db/install/01_create_schema.sql
- db/rollback/rollback.sql
- scripts/install-db.sh
- docs/install-workflow.md

Lab users:
- AI_APP_OWNER
- AI_APP_RUNTIME
- AI_APP_READONLY
- AI_REVIEWER

Rules:
- Use placeholders for passwords or read them from environment variables; do not store real secrets.
- Codex must not execute ad-hoc DDL/DML.
- All install actions must be represented as versioned SQL files.
- install-db.sh must run official SQL files only.
- Do not implement business objects yet except if a placeholder comment is needed.
- Do not add release-management tables in this goal.

Success criteria:
- install.sql is the controlled entry point.
- User/schema creation files exist as skeletons with clear TODOs/placeholders.
- rollback.sql exists as a safe skeleton.
- scripts/install-db.sh is documented and safe.
- Existing Python unittest tests pass.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add controlled DB install workflow skeleton
```
