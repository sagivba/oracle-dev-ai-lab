# Purpose

This document defines the controlled database install workflow for
`oracle-dev-ai-lab`, including the Goal 007 install skeleton and the Goal 008
smoke-object integration.

## Scope

The install workflow uses managed SQL files only. It does not validate Oracle
runtime behavior unless explicitly run against the local lab, and it does not
implement release-management functionality.

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
db/src/tables/lab_smoke_test.sql
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
`db/` SQL tree into the container, and invokes only:

```text
db/install/install.sql
```

It does not contain inline SQL DDL or DML.

## Relationship to Goal 008

Goal 008 adds the `LAB_SMOKE_TEST` infrastructure object and SQL smoke tests.
`LAB_SMOKE_TEST` is not a business feature and does not represent
release-management functionality.

## Still Intentionally Not Implemented by the Install Workflow

- release-management business tables;
- utPLSQL tests;
- review workflow;
- packaging workflow;
- spec pipeline tools;
- functional release-management logic.

## Validation Status

Goal 007 validation is repository-only and shell syntax only. Docker was not
started, Oracle was not started, no database connection was made, and no DDL or
DML was executed.
