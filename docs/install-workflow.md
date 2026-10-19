# Purpose

This document defines the controlled database install workflow for
`oracle-dev-ai-lab`, including the Goal 007 install skeleton and the Goal 008
smoke-object integration.

## Scope

The install workflow uses managed SQL files only. It creates or updates the
local lab users required by the infrastructure smoke object, but it does not
validate Oracle runtime behavior unless explicitly run against the local lab, and
it does not implement release-management functionality.

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

`db/install/00_create_lab_users.sql` creates or updates these local lab users:

```text
AI_APP_OWNER
AI_APP_RUNTIME
AI_APP_READONLY
AI_REVIEWER
```

The file uses only the password substitution variables supplied by
`db/install/install.sql` and `scripts/install-db.sh`. `AI_APP_OWNER` receives
the minimum privileges required to own `LAB_SMOKE_TEST`: `CREATE SESSION`,
`CREATE TABLE`, and quota on the local `USERS` tablespace. The other lab users
receive `CREATE SESSION` only in Goal 008.

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

It passes the copied container-side `db/` root to `db/install/install.sql` so
managed source files under `db/src/` are referenced by their explicit runtime
path inside the container. This keeps the `LAB_SMOKE_TEST` install independent
of SQLPlus' current working directory.

It does not contain inline SQL DDL or DML. The script captures SQLPlus output
and fails non-zero if SQLPlus exits non-zero or if the output contains `SP2-`,
`ORA-`, or `PLS-` error markers. The success message is printed by the shell
script only after those checks pass.

The SQL entry point ends with a managed SQLPlus `exit success` so the
`docker exec` install session terminates deterministically after the managed
install order completes.

## Relationship to Goal 008

Goal 008 adds the `LAB_SMOKE_TEST` infrastructure object and SQL smoke tests.
`LAB_SMOKE_TEST` is not a business feature and does not represent
release-management functionality.

## Related Workflows and Remaining Scope

Static review, packaging, and specification tooling exist as separate workflows;
they are not executed by the install script. See [the documentation index](README.md).
Release-management business objects, business utPLSQL tests, and functional
logic have not been implemented. `LAB_SMOKE_TEST` remains infrastructure-only.

## Validation Status

Goal 014 / [PR #22](https://github.com/sagivba/oracle-dev-ai-lab/pull/22) records a
successful local Dev clean install after reset and SQL smoke tests at `v0.1.0`
on 2026-05-22. See [the closure record](infrastructure-mvp-closure.md).
Repeated idempotent install on an already-installed lab was not validated.

No install or SQL smoke tests were run during this documentation reconciliation.
A new environment must validate its own clean install and smoke tests; existing
files, historical PASS results, and Python CI do not prove current Oracle runtime
compatibility.
