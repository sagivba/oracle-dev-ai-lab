# Repository Structure

## Purpose

This document describes the current layout and file responsibilities in
`oracle-dev-ai-lab`. It reflects the merged Infrastructure MVP and T015 handoff
baseline, rather than the earlier Goal 004 folder-only snapshot.

## Current Oracle Lab Files

| Area | Paths | Responsibility |
| --- | --- | --- |
| Docker lab | `docker-compose.yml`, `.env.example`, `scripts/lab-up.sh`, `scripts/lab-down.sh`, `scripts/lab-reset.sh`, `scripts/lab-backup.sh`, `scripts/lab-restore.sh` | Isolated disposable Oracle service and lifecycle entry points. |
| Managed install | `db/install/install.sql`, `db/install/00_create_lab_users.sql`, `db/install/01_create_schema.sql`, `scripts/install-db.sh` | Versioned lab user/schema setup and smoke-object installation through official scripts. |
| DB source | `db/src/` | SQL grouped by tables, constraints, indexes, views, packages, triggers, and seed. Currently only `tables/lab_smoke_test.sql` is implemented SQL. |
| Rollback | `db/rollback/rollback.sql` | Conservative rollback skeleton; not a full functional rollback implementation. |
| SQL tests | `db/tests/sql/`, `scripts/run-db-tests.sh` | Connectivity, object inventory, and invalid-object smoke checks. |
| Future PL/SQL tests | `db/tests/utplsql/` | Placeholder for future business unit tests; no business utPLSQL tests implemented. |
| Static review | `db/review/review-report.md`, `scripts/review-db-code.sh` | Repository-only checks and review template; no live Oracle diagnostics or deployment approval. |
| Packaging | `tools/package_release.py`, `scripts/package-release.sh`, `db/dist/release_001/` | Deterministic package skeleton from tracked sources; generated entry points do not deploy objects. |
| Generated DB area | `db/generated/` | Reserved area; no functional SQL generation implementation. |
| Spec pipeline | `tools/extract_spec.py`, `tools/validate_spec.py`, `tools/generate_todo.py`, `tools/generate_tasks.py` | Semantic specification extraction, validation, and generated planning artifacts. |
| Functional specification | `specs/001-release-management/` | Placeholder `spec.html`, generated `spec.json`, TODO, tasks, and traceability matrix; no business DB implementation. |

## Documentation and Governance

- `AGENTS.md` and `.agents/oracle-ai-lab-codex-planner/` define mandatory AI work rules.
- Root `TODO.md` is the current status and next-action ledger.
- `docs/README.md` is the documentation navigation index.
- Governance and workflow references live under `docs/`.
- `docs/01_Setting-AI-oracle-lab.html` is the original planning source, not an implementation inventory.
- `docs/codex-goals/` contains staged task sources; completed goals are not automatically the next action.
- `docs/stages/` contains historical Hebrew stage reports; read `docs/stages/README.md` before using them.

## Retained Python Starter

`src/oracle_ai_lab/`, `templates/`, `static/`, `Dockerfile`, and the Compose `app`
service are retained-but-frozen starter tooling, separate from the Oracle `db`
service. `tests/`, `scripts/test.sh`, `scripts/lint.sh`, and
`.github/workflows/ci.yml` provide Python tests/contracts and lint. CI does not
start Oracle or execute SQL smoke tests.

## Validation Boundary and Remaining Work

File presence proves implementation exists, not that a fresh environment works.
Historical local clean-install and smoke-test evidence is recorded in
[infrastructure-mvp-closure.md](infrastructure-mvp-closure.md) and the Goal 014
stage report. This documentation reconciliation did not run Oracle runtime checks.

Functional release-management tables, constraints, indexes, seed data, views,
packages, triggers, business SQL/utPLSQL tests, and deployment logic remain future
work. Some object-type directories contain only README placeholders. Follow
[the readiness checklist](functional-readiness-checklist.md) and an explicitly
approved functional goal before adding objects.

## Structure Rules

- Preserve the current layout and retained starter unless an explicit task changes it.
- Keep every DB change in versioned SQL and execute it only through official scripts.
- Trace every change to a goal, task, requirement, or decision.
- Do not infer release approval or runtime compatibility from generated package files.
