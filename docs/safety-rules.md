# Safety Rules

## Purpose

This document defines mandatory safety rules for `oracle-dev-ai-lab`. These rules
are not advisory.

## Repository Boundary

- Codex must work only inside this repository.
- Codex must not modify unrelated files.
- Codex must not invent missing requirements.
- If a required assumption is missing, Codex must stop and report it.

## Database Boundary

- Codex must not connect to organizational databases.
- Codex must not connect to production, development, test, staging, or shared
  organizational databases.
- Codex must connect only to the local Docker container named
  `oracle-dev-ai-lab-db` when database work is required and the lab exists.
- Codex must not connect to any database for documentation-only tasks.

## DDL and DML Rules

- Codex must not execute ad-hoc DDL.
- Codex must not execute ad-hoc DML.
- Every schema or database change must be represented as a versioned SQL file in
  the repository.
- Every schema or database change must run only through official repository
  scripts.
- No database change is valid unless it exists as a versioned SQL file and can be
  installed on a clean lab database by official scripts.

## SELECT Rules

SELECT statements are allowed only for:

- diagnostics;
- metadata inspection;
- compile checks;
- tests;
- review.

SELECT statements are allowed only against the local lab container when the lab
exists and the current task authorizes DB access.

## Secrets and Configuration

- No secrets may be committed.
- No passwords may be committed.
- No tokens may be committed.
- No private keys may be committed.
- No certificates may be committed.
- No real connection strings may be committed.
- Do not add `.env` or local secret-bearing files to Git.
- Only placeholder values may appear in tracked examples such as `.env.example`.

## Git State Wins

Git state wins over database state.

If database state conflicts with Git state, recreate the lab DB from repository
files. Do not patch the database manually.

## Compatibility Claims

Do not claim Docker, Oracle, DB, install, review, packaging, or release-package
compatibility unless the relevant checks actually ran and passed.

If a check was not run, state:

- which check was not run;
- why it was not run;
- whether that limits confidence in the change.

## Testing Rules

- Python tests must use `unittest`.
- Do not introduce `pytest`.
- Business PL/SQL unit tests will use utPLSQL only in future functional
  iterations.

## Documentation-Only Task Rule

For documentation and governance tasks, do not:

- connect to any database;
- run DDL;
- run DML;
- create Oracle Docker runtime infrastructure;
- create DB SQL files;
- create install, review, package, or spec pipeline implementation artifacts.
