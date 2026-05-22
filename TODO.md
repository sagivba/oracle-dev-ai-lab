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
- cleaned Git branch state after merged work

The repository is mostly ready for the first functional Oracle DB iteration, but a small handoff documentation cleanup should be completed first.

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

- [DONE] Git branches cleaned after merged work.
  - Merged task branches were removed locally and remotely.
  - `main` is clean and synchronized.

## Active readiness gaps before first functional DB iteration

- [TODO] Add a documentation index under `docs/README.md`.
  - Purpose: explain which documents are live governance, live workflow/reference, historical stage records, planning sources, goal/task sources, and generated/spec artifacts.
  - Reason: reduce confusion for future AI agents and human reviewers.

- [TODO] Add `docs/stages/README.md`.
  - Purpose: mark `docs/stages/` as historical stage reports, not active implementation instructions.
  - Reason: prevent AI agents from treating completed stage reports as current task instructions.

- [TODO] Confirm and document Flask starter status.
  - Recommended decision: retained-but-frozen.
  - Meaning: the Flask starter app remains only as retained Python/test/CI starter surface and must not be extended during Oracle DB functional iterations.
  - Files likely affected: `README.md`, `docs/README.md`, and possibly `.github/CONTRIBUTING.md`.

- [TODO] Clarify `docker-compose.yml` service boundaries.
  - Add a short comment above the `app` service.
  - The comment should state that the `app` service is retained Flask starter infrastructure and is not part of the Oracle database lab runtime or functional DB iteration scope.

- [TODO] Clarify CI validation scope.
  - Document that CI validates Python contracts and lint only.
  - Local Oracle runtime validation remains a local lab responsibility unless a later decision adds DB integration CI.
  - This can be documented in `docs/README.md` or a dedicated `docs/ci-scope.md`.

## Recommended next task

- [TODO] Run a focused handoff documentation cleanup before functional DB work.

Suggested task title:

```text
T015 - Improve Repository Handoff Documentation Before First Functional Iteration
```

Suggested scope:

1. Update this `TODO.md` if needed.
2. Add `docs/README.md`.
3. Add `docs/stages/README.md`.
4. Document the Flask starter as retained-but-frozen.
5. Add a comment in `docker-compose.yml` above the `app` service.
6. Clarify CI scope in documentation.
7. Add a Hebrew standalone HTML stage report under `docs/stages/`.

Constraints:

- Do not add functional Oracle DB objects.
- Do not change SQL behavior.
- Do not change Docker behavior.
- Do not change CI behavior unless explicitly required.
- Do not remove Flask starter files in this task.
- Do not modify historical stage reports except adding `docs/stages/README.md`.

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

- [TODO] Confirm final status of the retained Flask starter.
  - Recommended: retained-but-frozen.

- [TODO] Confirm whether `docs/README.md` should become the primary human/AI navigation entry point for documentation.
  - Recommended: yes.

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

Complete the handoff documentation cleanup task, then start the first functional Oracle DB iteration.
