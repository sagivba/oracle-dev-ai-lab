# Purpose

This document defines the Goal 007 controlled database install workflow skeleton
for `oracle-dev-ai-lab`.

## Scope

Goal 007 adds the managed install entry points only. It does not validate Oracle
runtime behavior and does not implement release-management functionality.

## Safety Boundaries

- The workflow targets only the local Docker container
  `oracle-dev-ai-lab-db`.
- The default PDB is `FREEPDB1`.
- Git is the source of truth for every database change.
- No ad-hoc DDL or DML is allowed.
- Database changes must live in versioned SQL files under `db/`.
- No real passwords or secrets may be committed.
- Runtime Oracle compatibility is not claimed until the workflow is actually run
  and validated against the disposable local lab.

## Required Local Environment Variables

Set these in an untracked local `.env` file or in the shell environment before
running `scripts/install-db.sh`:

```text
ORACLE_PWD
AI_APP_OWNER_PWD
AI_APP_RUNTIME_PWD
AI_APP_READONLY_PWD
AI_REVIEWER_PWD
```

Optional variable:

```text
ORACLE_PDB=FREEPDB1
```

Do not commit `.env` or real values.

## Managed SQL Files

The official SQL entry point is:

```text
db/install/install.sql
```

It runs managed install files in this deterministic order:

```text
db/install/00_create_lab_users.sql
db/install/01_create_schema.sql
```

Rollback is reserved in:

```text
db/rollback/rollback.sql
```

## Shell Entry Point

Run the workflow with:

```text
scripts/install-db.sh
```

The script resolves the repository root, loads local environment values if
`.env` exists, checks the expected local lab container name, copies the managed
install SQL directory into the container, and invokes only:

```text
db/install/install.sql
```

It does not contain inline SQL DDL or DML.

## Relationship to Goal 008

Goal 008 will add the `LAB_SMOKE_TEST` object and SQL smoke tests. Goal 007 does
not add that object and does not add SQL smoke test implementation.

## Intentionally Not Implemented in Goal 007

- release-management business tables;
- `LAB_SMOKE_TEST`;
- SQL smoke tests;
- utPLSQL tests;
- review workflow;
- packaging workflow;
- spec pipeline tools;
- functional release-management logic.

## Validation Status

Goal 007 validation is repository-only and shell syntax only. Docker was not
started, Oracle was not started, no database connection was made, and no DDL or
DML was executed.
