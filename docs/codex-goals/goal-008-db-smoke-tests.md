# /goal 008 - Add DB Smoke Object and SQL Smoke Tests

## Goal

Add minimal DB smoke object and SQL smoke tests to prove install/test/review/package flow without implementing a business feature.

## Prompt to use with Codex

```text
/goal
Add a minimal DB smoke object and SQL smoke tests for Infrastructure MVP.

Create or update:
- db/src/tables/lab_smoke_test.sql
- db/tests/sql/001_db_connectivity.sql
- db/tests/sql/002_object_inventory.sql
- db/tests/sql/003_no_invalid_objects.sql
- scripts/run-db-tests.sh
- docs/testing-strategy.md

Smoke object:
- LAB_SMOKE_TEST

Rules:
- LAB_SMOKE_TEST is not a business feature.
- It exists only to prove controlled install, SQL tests, review, and packaging.
- Do not create release-management business tables yet.
- SQL tests should fail clearly using raise_application_error or equivalent when expectations are not met.
- SELECT diagnostics are allowed only against the local lab container.

If Docker/Oracle is not available during implementation, scripts must be written safely and tests that require DB must be explicitly separated from Python repository tests.

Success criteria:
- Smoke SQL file exists under db/src/tables.
- SQL smoke tests exist under db/tests/sql.
- scripts/run-db-tests.sh has clear modes or usage.
- scripts/test.sh quick does not require Oracle unless explicitly configured.
- scripts/test.sh full may include DB smoke tests.
- Python unittest tests pass.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add DB smoke object and SQL smoke test structure
```
