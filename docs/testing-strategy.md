# Purpose

This document defines the testing strategy for `oracle-dev-ai-lab` at Goal 005.
It establishes the current Python contract-test layer and separates it from
future Oracle database test layers.

## 1. Python `unittest` Repository Contract Tests

Repository contract tests are the current automated test layer for the project.
They use Python `unittest` and the standard library only.

These tests check repository structure, governance files, required scripts, and
placeholder directories that support later Oracle work.

Rules for this layer:

- Use `unittest`.
- Do not require `pytest`.
- Do not require Docker.
- Do not require Oracle DB access.
- Do not execute DDL or DML.
- Keep the tests fast, deterministic, and repository-only.

## 2. SQL Smoke Tests

SQL smoke tests are the Oracle-layer smoke test type introduced by Goal 008.
They cover:

- DB connectivity;
- install verification for the infrastructure smoke object;
- invalid objects;
- object inventory;
- `LAB_SMOKE_TEST` column checks.

These tests live under:

```text
db/tests/sql/
```

They are run by:

```text
scripts/run-db-tests.sh
```

They require the local Oracle lab container and local environment variables.
They are not part of `scripts/test.sh quick`.

## 3. Future utPLSQL Tests

utPLSQL will be used later for PL/SQL business unit tests in functional
iterations.

These tests are not implemented in Goal 005.
They belong to later Oracle functional work after Infrastructure MVP foundations
exist.

## 4. Test Entry Points

Current supported entry points are:

```text
scripts/test.sh quick
scripts/test.sh full
RUN_DB_TESTS=1 scripts/test.sh full
scripts/run-db-tests.sh
PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

If the environment requires the virtual environment on `PATH`, use:

```text
PATH=.venv/bin:$PATH scripts/test.sh quick
PATH=.venv/bin:$PATH scripts/test.sh full
PATH=.venv/bin:$PATH RUN_DB_TESTS=1 scripts/test.sh full
PATH=.venv/bin:$PATH PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

## 5. Safety Boundaries

Repository-only tests do not:

- start Docker;
- connect to Oracle;
- execute DDL;
- execute DML;
- claim Docker runtime compatibility;
- claim Oracle runtime compatibility.

SQL smoke tests may connect only to the local `oracle-dev-ai-lab-db` container
and may run SELECT/metadata checks for test verification. They must not connect
to organizational databases.
