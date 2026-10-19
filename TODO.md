# TODO - DEVELOPMENT in Oracle using AI Lab

## Purpose

This file is the live repository status and next-action ledger for `oracle-dev-ai-lab`.

It records the current project state, the active readiness gaps, and the next recommended work before starting the first functional Oracle database iteration.

This file is documentation only. It does not implement Docker, Oracle schemas, install scripts, review scripts, package scripts, or functional database objects.

## Current status

The Infrastructure MVP is complete and merged to `main`.

The repository now provides a controlled Oracle AI Lab baseline where Git is the source of truth and the local Oracle Docker database is disposable runtime state.

Current baseline includes:

- isolated Oracle Docker lab skeleton
- controlled DB install workflow
- SQL smoke test workflow
- static review workflow
- deterministic release package workflow
- specification pipeline skeleton
- functional iteration readiness checklist
- local Oracle runtime validation record
- normalized live-file documentation
- completed T015 handoff documentation and explicit Flask/CI boundaries

T015 handoff documentation is complete and merged in [PR #24](https://github.com/sagivba/oracle-dev-ai-lab/pull/24) on 2026-05-22. The first functional Oracle DB iteration has not started and remains subject to the readiness gate.

## Status legend

- [DONE] Completed and merged.
- [TODO] Not yet done.
- [PARTIAL] Exists but needs clarification or follow-up.
- [BLOCKED] Cannot proceed until a decision or dependency is resolved.
- [DEFERRED] Intentionally postponed; not required before the next functional iteration.

## Completed infrastructure baseline

- [DONE] Project intake and repository alignment completed.
  - The repository is aligned to `oracle-dev-ai-lab`.
  - The project display name is `DEVELOPMENT in Oracle using AI Lab`.
  - The project is no longer treated as a generic Python/Flask template.

- [DONE] Governance and safety documentation completed.
  - `AGENTS.md` defines AI/Codex working rules.
  - Project safety rules prohibit organizational DB access, secrets, and ad-hoc DDL/DML.
  - Git remains the source of truth.

- [DONE] Oracle lab repository structure completed.
  - `db/`, `scripts/`, `tools/`, `tests/`, `specs/`, and supporting directories exist.
  - DB source files are organized by object type under `db/src/`.

- [DONE] Docker lab skeleton completed.
  - The Oracle database service uses the fixed lab container, volume, network, and PDB names.
  - Local secrets are represented only as placeholders in `.env.example`.

- [DONE] Lab lifecycle scripts completed.
  - Start, stop, reset, backup, and restore scripts exist for the local disposable lab.

- [DONE] Managed DB install workflow completed.
  - `scripts/install-db.sh` runs the official install entry point.
  - DB changes must be represented as versioned SQL files.

- [DONE] SQL smoke object and smoke tests completed.
  - `LAB_SMOKE_TEST` exists as infrastructure-only DB source.
  - SQL smoke tests check connectivity, object inventory, and invalid objects.

- [DONE] Specification pipeline skeleton completed.
  - Semantic HTML spec extraction, validation, TODO generation, task generation, and traceability generation exist.
  - The current release-management spec is a placeholder for future functional work.

- [DONE] Review workflow skeleton completed.
  - Static repository review script and report template exist.

- [DONE] Release packaging workflow skeleton completed.
  - The deterministic release package workflow creates `db/dist/release_001/`.
  - Generated package output is explicitly not approved unless review evidence supports approval.

- [DONE] Functional iteration readiness checklist completed.
  - Functional DB work is gated by `docs/functional-readiness-checklist.md`.

- [DONE] Local Oracle runtime validation recorded.
  - The infrastructure baseline has a recorded local runtime validation result.

- [DONE] Live-file documentation normalized.
  - Live source, script, SQL, tool, and generated package documentation now describe stable file purpose rather than historical Goal/Stage creation context.

- [DONE] T015 - Improve Repository Handoff Documentation Before First Functional Iteration.
  - Merged in [PR #24](https://github.com/sagivba/oracle-dev-ai-lab/pull/24) on 2026-05-22.
  - `docs/README.md` is the documentation navigation entry point.
  - `docs/stages/README.md` identifies stage reports as historical records.
  - Flask is retained-but-frozen; the Compose `app` service is explicitly outside Oracle DB iteration scope.
  - CI validates Python tests/contracts and lint, not live Oracle runtime.

## Validation evidence and remaining readiness work

- [DONE] Historical local Dev validation was recorded by Goal 014 in [PR #22](https://github.com/sagivba/oracle-dev-ai-lab/pull/22), merged on 2026-05-22.
  - The recorded baseline is `v0.1.0` (`1c6b46797766656e5db537047d8e91b61853e71d`).
  - It covers Oracle readiness, clean install after reset, SQL smoke tests, static review, and package generation.
  - See `docs/infrastructure-mvp-closure.md` and `docs/stages/stage-014-local-oracle-lab-runtime-validation.html` for scope and limitations.
  - Goal 014 did not validate repeated install on an installed lab, QA worktree behavior, or portability to other developers. Earlier QA results are a separate historical record in the closure document.

- [TODO] Satisfy `docs/functional-readiness-checklist.md` for the separate first functional goal.
  - Revalidate missing or stale evidence in the local disposable lab before functional work.
  - This documentation reconciliation did not start Docker, connect to Oracle, run install/SQL smoke tests, or exercise backup/restore.
  - Existing scripts, old PASS records, and green Python CI do not guarantee a fresh runtime succeeds.
  - Package generation is a skeleton workflow; generated entry points do not deploy objects and do not grant release approval.

## Recommended next task

Define a separate first functional Oracle DB goal with approved requirements,
acceptance criteria, traceability, and current readiness evidence. Do not rerun
T015 or create business objects as part of this documentation correction.

## First functional Oracle DB iteration - not started yet

- [TODO] Define the first functional iteration from the release-management specification.
  - Confirm the starting requirement set.
  - Confirm entity boundaries.
  - Confirm whether the first iteration should create tables only, or tables plus constraints/indexes/tests.
  - Prefer a small vertical slice.

- [TODO] Create versioned SQL files for the first functional objects.
  - Expected locations:
    - `db/src/tables/`
    - `db/src/constraints/`
    - `db/src/indexes/`
    - `db/src/views/` if needed
    - `db/src/packages/` only if explicitly justified

- [TODO] Extend the managed install workflow.
  - Functional DB objects must install only through official scripts.

- [TODO] Add SQL and/or future utPLSQL tests.
  - Tests must be traceable to requirements and acceptance criteria.

- [TODO] Update review and packaging evidence after functional changes.
  - Release package approval must remain blocked if review evidence is incomplete or BLOCKER findings exist.

## Deferred improvements

- [DEFERRED] Decide whether to separate Flask compose files from Oracle lab compose files.
  - Useful, but not required before the first functional DB iteration.

- [DEFERRED] Decide long-term policy for committed generated artifacts.
  - Current approach keeps deterministic generated artifacts in Git.
  - A later architecture decision may revisit this.

- [DEFERRED] Add Oracle container healthcheck.
  - Useful for improving `lab-up.sh`, but not required before first functional DB work.

- [DEFERRED] Add SQL error log parser for AI self-correction.
  - Potentially valuable after functional SQL work begins.

- [DEFERRED] Enforce release approval semantics more strictly in packaging scripts.
  - Current package output remains explicitly not approved unless review evidence supports approval.
  - A future release governance task can make this rule more machine-enforced.

## Open decisions

- [TODO] Confirm whether the next functional iteration should start with table-only implementation or a complete narrow vertical slice.
  - Recommended: narrow vertical slice if the requirements are stable enough; otherwise table-only plus tests.

## Standard validation commands

For repository-only checks:

```bash
PATH=.venv/bin:$PATH scripts/test.sh quick
PATH=.venv/bin:$PATH scripts/lint.sh
scripts/review-db-code.sh
git diff --check | cat
```

For local Oracle lab validation when DB runtime is in scope:

```bash
scripts/lab-up.sh
scripts/install-db.sh
scripts/run-db-tests.sh
```

For release package regeneration when packaging is in scope:

```bash
PATH=.venv/bin:$PATH scripts/package-release.sh
```

## Current next action

Define the separate first functional goal, resolve its scope, and satisfy the readiness checklist before implementing any business DB objects. T015 is already complete.
