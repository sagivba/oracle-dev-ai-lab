# Purpose

This document defines the Goal 011 release packaging workflow skeleton for
`oracle-dev-ai-lab`.

## Scope

Goal 011 is skeleton-only. It defines the deterministic release package contract
and creates the first package structure under:

```text
db/dist/release_001/
```

It does not add functional release-management DB objects, real deployment logic,
Oracle runtime validation, APEX, ORDS, REST APIs, or UI work.

## Package Structure

The packaging workflow creates or refreshes:

```text
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
```

## Managed Source Inclusion Rules

The Python helper includes only tracked `.sql` files from these managed folders:

```text
db/src/tables/
db/src/constraints/
db/src/indexes/
db/src/views/
db/src/packages/
db/src/triggers/
db/src/seed/
```

Files are processed in deterministic sorted order. Unmanaged files outside those
folders are not packaged.

When an expected package object-type folder has no managed SQL files, the helper
generates a deterministic `README.md` marker inside that package folder. The
marker exists only because Git does not track empty directories; it is packaging
structure metadata, not a DB source file.

## Excluded Files

The package must not include:

- `.env`;
- `.env.*`;
- secrets, tokens, private keys, or certificates;
- unmanaged database changes;
- files outside the approved `db/src/` object-type folders.

If a managed source file appears to contain secret-bearing material, the helper
refuses to create the package.

## Safety Boundaries

The packaging workflow:

- does not connect to Oracle;
- does not run Docker;
- does not access organizational databases;
- does not execute ad-hoc DDL or DML;
- does not claim Oracle runtime validation;
- uses only Python standard library code.

The generated `install.sql` and `rollback.sql` files are package entry point
skeletons. They document package scope only and intentionally do not perform
deployment work.

## Review Report and BLOCKER Rule

The package copies:

```text
db/review/review-report.md
```

to:

```text
db/dist/release_001/review-report.md
```

The release package remains explicitly not approved in Goal 011. A release package is not approved if any BLOCKER exists, and this skeleton does not grant release approval.

## How to Run

From the repository root:

```bash
scripts/package-release.sh
```

The script calls:

```bash
python tools/package_release.py
```

## Validation

Use the standard quick check:

```bash
PATH=.venv/bin:$PATH scripts/test.sh quick
```

If linting is relevant to the change, run:

```bash
PATH=.venv/bin:$PATH scripts/lint.sh
```

Oracle runtime validation is not required for this skeleton-only packaging goal.
