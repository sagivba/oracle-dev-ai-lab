# TODO - DEVELOPMENT in Oracle using AI Lab

## Purpose

This file is the Stage 0 intake baseline for `oracle-dev-ai-lab`. It records what the
project is supposed to contain according to `docs/01_Setting-AI-oracle-lab.html`, what
currently exists in the repository, what is missing, and what should happen next.

This baseline is documentation only. It does not implement Docker, Oracle schemas,
install scripts, review scripts, package scripts, or functional database objects.

## Status legend

- [DONE] The required item exists and is aligned enough to count as present.
- [TODO] The required item is missing.
- [PARTIAL] A generic/template version exists, but it is not yet aligned to Oracle AI Lab.
- [BLOCKED] The item cannot proceed until a required decision or source file is provided.
- [NOT_APPLICABLE_YET] The item depends on completion of earlier Infrastructure MVP work.

## Current repository baseline

- [DONE] Repository contains the required project planning document.
  - Evidence: `docs/01_Setting-AI-oracle-lab.html`
  - Source: Repository observation; required by this task.
  - Notes: This document is the current source for project stages, decisions, and expected structure.
- [DONE] Repository contains the Oracle AI Lab Codex Skill and project rules.
  - Evidence: `.agents/oracle-ai-lab-codex-planner/SKILL.md`; `.agents/oracle-ai-lab-codex-planner/references/project-rules.md`
  - Source: Repository observation; AGENTS.md project-specific instructions.
  - Notes: These files define fixed names, safety rules, branch rules, and stage report requirements.
- [PARTIAL] Repository contains a generic Python template application.
  - Evidence: `src/oracle_ai_lab/`, `tests/`, `templates/`, `static/`, `Dockerfile`, `docker-compose.yml`
  - Source: Repository observation.
  - Notes: Existing Flask health/welcome code is template infrastructure, not the Oracle DB lab infrastructure described in the planning document.
- [DONE] Root README identifies the Oracle AI Lab project.
  - Evidence: `README.md`
  - Source: Repository observation.
  - Notes: README now states that `oracle-dev-ai-lab` is not a generic Python/Flask template project and frames existing Flask/Docker files as retained starter infrastructure.
- [DONE] AGENTS.md exists and includes strict Oracle AI Lab project instructions.
  - Evidence: `AGENTS.md`
  - Source: Repository observation; task requirement.
  - Notes: AGENTS.md now includes governance reading, goal ordering, commit discipline, database safety, standard checks, and final response expectations.
- [DONE] Basic Python test script exists.
  - Evidence: `scripts/test.sh`
  - Source: Repository observation.
  - Notes: It runs unittest for the template app; it is not yet the full Oracle lab test workflow.
- [PARTIAL] Basic lint script exists.
  - Evidence: `scripts/lint.sh`
  - Source: Repository observation.
  - Notes: It checks Python template files only.
- [DONE] Required Stage 0 project documents exist.
  - Evidence: `docs/project-charter.md`, `docs/safety-rules.md`, `docs/decision-log.md`, and `docs/repository-structure.md`
  - Source: Planning document section 12; project rules required repository structure.
  - Notes: Governance documents now define scope, safety rules, stable decisions, and current vs target structure.
- [DONE] Required Oracle lab database directories exist.
  - Evidence: `db/install/`, `db/src/`, `db/src/tables/`, `db/src/constraints/`, `db/src/indexes/`, `db/src/views/`, `db/src/packages/`, `db/src/triggers/`, `db/src/seed/`, `db/rollback/`, `db/tests/sql/`, `db/tests/utplsql/`, `db/review/`, `db/generated/`, and `db/dist/`
  - Source: Planning document section 7; project rules required repository structure.
  - Notes: Goal 004 created the folder-only skeleton and placeholder READMEs; no SQL implementation was added.
- [DONE] Required spec directory exists.
  - Evidence: `specs/001-release-management/` and `specs/001-release-management/tasks/`
  - Source: Planning document sections 7, 9, 10, and 12.
  - Notes: Goal 004 created the folder-only skeleton and placeholder READMEs; functional spec work belongs to later goals.
- [DONE] Required tools directory exists.
  - Evidence: `tools/`
  - Source: Planning document section 7; project rules required repository structure.
  - Notes: Goal 004 created the folder-only skeleton and placeholder README; tool implementation belongs to later goals.

## Codex goals execution baseline

- [DONE] Goal 000 - Operating Rules for All Goals
  - Goal file: `docs/codex-goals/goal-000-operating-rules.md`
  - Purpose: Establish mandatory execution rules for all later Codex goals.
  - Evidence: Goal file exists; `.agents/oracle-ai-lab-codex-planner/SKILL.md`, `.agents/oracle-ai-lab-codex-planner/references/project-rules.md`, `AGENTS.md`, and `docs/01_Setting-AI-oracle-lab.html` contain the mandatory operating rules.
  - Notes: The goal states that no repository changes are required by Goal 000.
  - Recommended next action: Skip Goal 000 as already satisfied; continue with Goal 001.
- [DONE] Goal 001 - Align Template Identity
  - Goal file: `docs/codex-goals/goal-001-template-alignment.md`
  - Purpose: Align repository identity to `oracle-dev-ai-lab` without adding Oracle implementation.
  - Evidence: `README.md` identifies `oracle-dev-ai-lab`; `pyproject.toml` uses display name `DEVELOPMENT in Oracle using AI Lab`; package folder remains `src/oracle_ai_lab/`; `src/oracle_ai_lab/__init__.py` and `src/oracle_ai_lab/config.py` no longer use `*-template` naming; `docs/template-usage.md` is reframed as legacy notes.
  - Notes: Retained Flask/Python starter infrastructure remains intentionally; no Oracle implementation was added.
  - Recommended next action: Continue with Goal 002.
- [DONE] Goal 002 - Create Project Documentation Baseline
  - Goal file: `docs/codex-goals/goal-002-project-docs.md`
  - Purpose: Create mandatory project charter, safety rules, decision log, repository structure, and Codex workflow documentation.
  - Evidence: `docs/project-charter.md`, `docs/safety-rules.md`, `docs/decision-log.md`, `docs/repository-structure.md`, and `docs/codex-workflow.md`
  - Notes: Documentation distinguishes Infrastructure MVP, future functional iterations, and out-of-scope organizational integration. No implementation artifacts were added.
  - Recommended next action: Continue with Goal 004.
- [DONE] Goal 003 - Create Strict AGENTS.md
  - Goal file: `docs/codex-goals/goal-003-agents-md.md`
  - Purpose: Create strict Codex operating rules for repository work.
  - Evidence: `AGENTS.md`; `docs/project-charter.md`; `docs/safety-rules.md`; `docs/decision-log.md`; `docs/repository-structure.md`; `docs/codex-workflow.md`
  - Notes: AGENTS.md is aligned with the governance docs and includes strict safety rules, `unittest`, goal ordering, one-goal-per-commit discipline, combined-goal exception, standard checks, and final response requirements.
  - Recommended next action: Continue with Goal 004.
- [DONE] Goal 004 - Create Oracle Lab Repository Structure
  - Goal file: `docs/codex-goals/goal-004-repository-structure.md`
  - Purpose: Add the Oracle lab folder structure while preserving useful Python template structure.
  - Evidence: `docs/repository-structure.md`; `specs/001-release-management/`; `specs/001-release-management/tasks/`; `db/`; `db/install/`; `db/src/`; `db/src/tables/`; `db/src/constraints/`; `db/src/indexes/`; `db/src/views/`; `db/src/packages/`; `db/src/triggers/`; `db/src/seed/`; `db/rollback/`; `db/tests/`; `db/tests/sql/`; `db/tests/utplsql/`; `db/review/`; `db/generated/`; `db/dist/`; `tools/`
  - Notes: Goal 004 created the folder-only Oracle lab repository structure and placeholder READMEs. No Oracle SQL implementation was added.
  - Recommended next action: Continue with Goal 005.
- [DONE] Goal 005 - Add Testing Strategy and Baseline unittest Contracts
  - Goal file: `docs/codex-goals/goal-005-testing-strategy.md`
  - Purpose: Add testing strategy documentation and baseline repository contract tests using `unittest`.
  - Evidence: `docs/testing-strategy.md`; `tests/test_repo_contract.py`; `scripts/test.sh`; `scripts/lint.sh`
  - Notes: Goal 005 adds repository-contract tests with Python `unittest`, keeps `pytest` out of the test stack, preserves the existing quick local unittest entrypoint, and `scripts/test.sh quick` passes when `python` is available through `.venv/bin`.
  - Recommended next action: Continue with Goal 007.
- [DONE] Goal 006 - Add Oracle Docker Lab Skeleton
  - Goal file: `docs/codex-goals/goal-006-docker-lab-skeleton.md`
  - Purpose: Add Oracle AI Database 26ai Free Docker skeleton and lab lifecycle scripts.
  - Evidence: `docker-compose.yml`; `.env.example`; `scripts/lab-up.sh`; `scripts/lab-down.sh`; `scripts/lab-reset.sh`; `scripts/lab-backup.sh`; `scripts/lab-restore.sh`; `docs/docker-lab-design.md`
  - Notes: Skeleton is aligned to Sagiv Barhoom's Oracle 26ai Docker setup post using project names and placeholder-only secrets. Docker was not started, so runtime compatibility is not claimed.
  - Recommended next action: Continue with the first earlier incomplete goal in the sequence, Goal 004.
- [DONE] Goal 007 - Add Database Install Workflow Skeleton
  - Goal file: `docs/codex-goals/goal-007-install-workflow.md`
  - Purpose: Create controlled DB installation workflow and lab user SQL skeletons.
  - Evidence: `db/install/install.sql`, `db/install/00_create_lab_users.sql`, `db/install/01_create_schema.sql`, `db/rollback/rollback.sql`, `scripts/install-db.sh`, `docs/install-workflow.md`, and `tests/test_repo_contract.py`
  - Notes: Goal 007 added a managed install workflow skeleton and local-container-only shell entry point. Goal 008 now makes the install path internally consistent by creating or updating the local lab users needed for the smoke object. Runtime Oracle validation was not run or claimed.
  - Recommended next action: Run Goal 008 after Goal 007 creates the controlled install workflow.
- [DONE] Goal 008 - Add DB Smoke Object and SQL Smoke Tests
  - Goal file: `docs/codex-goals/goal-008-db-smoke-tests.md`
  - Purpose: Add minimal `LAB_SMOKE_TEST` object and SQL smoke tests for the Infrastructure MVP.
  - Evidence: `db/src/tables/lab_smoke_test.sql`, `db/tests/sql/001_db_connectivity.sql`, `db/tests/sql/002_object_inventory.sql`, `db/tests/sql/003_no_invalid_objects.sql`, `scripts/run-db-tests.sh`, and `tests/test_repo_contract.py`
  - Notes: Goal 008 adds `LAB_SMOKE_TEST` as an infrastructure-only object, integrates it through `db/install/install.sql`, updates local lab user setup so `AI_APP_OWNER` can own the object, and adds SQL smoke tests plus a local-container-only runner. Runtime Oracle validation was not run or claimed.
  - Recommended next action: Run Goal 009 after the DB smoke object and SQL smoke test structure exist.
- [DONE] Goal 009 - Add Specification Pipeline Skeleton
  - Goal file: `docs/codex-goals/goal-009-spec-pipeline-skeleton.md`
  - Purpose: Add HTML spec to JSON/TODO/tasks pipeline skeleton and deterministic tooling.
  - Evidence: `specs/001-release-management/spec.html`, `spec.json`, `TODO.md`, `traceability-matrix.md`, `specs/001-release-management/tasks/T001-spec-pipeline-placeholder.md`, `tools/extract_spec.py`, `tools/validate_spec.py`, `tools/generate_todo.py`, `tools/generate_tasks.py`, `tests/test_spec_pipeline.py`, and `docs/spec-pipeline.md`
  - Notes: Goal 009 adds deterministic standard-library skeleton tooling only. It does not generate functional release-management DB objects, review workflow files, or packaging workflow files.
  - Recommended next action: Run Goal 010 after the spec pipeline skeleton exists.
- [DONE] Goal 010 - Add Review Workflow Skeleton
  - Goal file: `docs/codex-goals/goal-010-review-workflow.md`
  - Purpose: Add DB code, repository contract, safety, and traceability review workflow.
  - Evidence: `scripts/review-db-code.sh`, `db/review/review-report.md`, `docs/review-workflow.md`, and `tests/test_review_contract.py`
  - Notes: Goal 010 adds a safe-by-default static review skeleton, required report sections, severity levels, BLOCKER approval rule, and repository-only contract tests. Runtime Oracle diagnostics were not run or claimed.
  - Recommended next action: Run Goal 011 after the review workflow skeleton exists.
- [DONE] Goal 011 - Add Release Packaging Workflow Skeleton
  - Goal file: `docs/codex-goals/goal-011-release-packaging-workflow.md`
  - Purpose: Add deterministic release packaging workflow and manifest structure.
  - Evidence: `scripts/package-release.sh`, `tools/package_release.py`, `db/dist/README.md`, `db/dist/release_001/`, `docs/packaging-workflow.md`, and `tests/test_packaging_contract.py`
  - Notes: Goal 011 remains skeleton-only. It packages managed, versioned repository DB source files into a deterministic `db/dist/release_001/` contract, copies the review report, keeps the package explicitly not approved, and does not add functional release-management DB objects.
  - Recommended next action: Keep Goal 012 blocked until the Infrastructure MVP skeleton is reviewed and accepted.
- [NOT_APPLICABLE_YET] Goal 012 - Add Release Management Functional Spec Placeholder
  - Goal file: `docs/codex-goals/goal-012-functional-spec-placeholder.md`
  - Purpose: Add only a placeholder spec for the future release-management use case.
  - Evidence: `specs/001-release-management/spec.html`, `specs/001-release-management/README.md`, and `docs/functional-iterations-plan.md` are missing; Infrastructure MVP foundations are also incomplete.
  - Notes: This goal is intentionally functional-scope preparation and should wait until earlier infrastructure goals are resolved.
  - Recommended next action: Do not run yet; revisit after Goals 001 through 011 are complete or intentionally skipped.
- [NOT_APPLICABLE_YET] Goal 013 - Add Functional Iteration Readiness Checklist
  - Goal file: `docs/codex-goals/goal-013-functional-iteration-readiness.md`
  - Purpose: Add checklist that blocks real functional development until Infrastructure MVP is complete.
  - Evidence: `docs/functional-readiness-checklist.md`, `docs/goals-plan.md`, and `specs/001-release-management/tasks/README.md` are missing; Infrastructure MVP is not complete.
  - Notes: Functional readiness depends on Docker, install, smoke tests, review, packaging, and approved project documentation.
  - Recommended next action: Do not run yet; revisit after Infrastructure MVP workflows exist.

## Stage 0 - Project Charter and project alignment

- [DONE] Planning source document exists.
  - Evidence: `docs/01_Setting-AI-oracle-lab.html`
  - Source: Task prerequisite; planning document sections 1 through 21.
  - Notes: This task was allowed to proceed because the planning document exists.
- [DONE] Project Skill and rules exist.
  - Evidence: `.agents/oracle-ai-lab-codex-planner/SKILL.md`; `.agents/oracle-ai-lab-codex-planner/references/project-rules.md`
  - Source: AGENTS.md; project rules.
  - Notes: These files are the required Codex operating context.
- [PARTIAL] AGENTS.md contains Oracle AI Lab instructions.
  - Evidence: `AGENTS.md`
  - Source: Task requirement 3.
  - Notes: Updated to include the planning document before work.
- [DONE] Create project charter.
  - Evidence: `docs/project-charter.md`
  - Source: Planning document section 12; Decision 010.
  - Notes: Defines purpose, current phase, source of truth, disposable DB runtime, MVP boundaries, first future use case, out-of-scope items, and references.
- [DONE] Create safety rules document.
  - Evidence: `docs/safety-rules.md`
  - Source: Planning document sections 2, 4, 18, and 21.
  - Notes: Defines mandatory repository, DB, DDL/DML, SELECT, secrets, Git-state, compatibility-claim, and testing rules.
- [DONE] Create decision log.
  - Evidence: `docs/decision-log.md`
  - Source: Planning document section 20.
  - Notes: Includes stable decisions `DEC-001` through `DEC-019`.
- [DONE] Create Stage 0 intake TODO baseline.
  - Evidence: `TODO.md`
  - Source: This task.
  - Notes: This file replaces the generic template TODO with the Oracle AI Lab baseline.
- [DONE] Create Hebrew HTML report for T000.
  - Evidence: `docs/stages/stage-00-task-T000-project-intake-todo-baseline.html`
  - Source: This task; project rules Hebrew HTML stage report requirement.
  - Notes: Documentation only; no infrastructure implementation.

## Stage 1 - Repo Skeleton

- [PARTIAL] Root repository skeleton exists.
  - Evidence: `README.md`, `AGENTS.md`, `.env.example`, `.gitignore`, `.github/`, `scripts/`, `src/`, `tests/`
  - Source: Planning document section 7.
  - Notes: Present skeleton is the Python template, not yet the required Oracle lab skeleton.
- [DONE] Align README with Oracle AI Lab scope.
  - Evidence: `README.md`
  - Source: Planning document sections 1, 5, 7, and 12.
  - Notes: README now identifies the repository, display name, fixed project names, current pre-implementation status, retained starter app, and safety rules.
- [DONE] Create required `docs/stages/` documentation area.
  - Evidence: `docs/stages/` created by this task for the T000 report.
  - Source: Project rules required repository structure.
  - Notes: Directory now exists because the T000 stage report was added.
- [DONE] Create required Oracle lab `db/` directory structure.
  - Evidence: `db/`, `db/install/`, `db/src/`, `db/src/tables/`, `db/src/constraints/`, `db/src/indexes/`, `db/src/views/`, `db/src/packages/`, `db/src/triggers/`, `db/src/seed/`, `db/rollback/`, `db/tests/`, `db/tests/sql/`, `db/tests/utplsql/`, `db/review/`, `db/generated/`, and `db/dist/`
  - Source: Planning document section 7; project rules.
  - Notes: Goal 004 created the folder-only skeleton and placeholder READMEs; no implementation SQL was added.
- [DONE] Create required `specs/001-release-management/` directory structure.
  - Evidence: `specs/001-release-management/` and `specs/001-release-management/tasks/`
  - Source: Planning document section 7.
  - Notes: Goal 004 created the folder-only skeleton and placeholder READMEs; functional spec content belongs to later goals.
- [DONE] Create required `tools/` directory.
  - Evidence: `tools/`
  - Source: Planning document section 7.
  - Notes: Goal 004 created the folder-only skeleton and placeholder README; tool implementation belongs to later goals.
- [PARTIAL] Tests exist for template app behavior.
  - Evidence: `tests/test_app.py`, `tests/test_model.py`, `tests/test_services.py`
  - Source: Repository observation.
  - Notes: They do not yet validate the Oracle lab repository contract.

## Stage 2 - Docker Lab DB

- [PARTIAL] Docker files include retained app infrastructure and Oracle lab skeleton.
  - Evidence: `Dockerfile`, `docker-compose.yml`, `docker-compose.dev.yml`, `docker-compose.qa.yml`
  - Source: Repository observation.
  - Notes: `docker-compose.yml` now includes an Oracle `db` skeleton; existing app Docker scaffolding remains retained starter infrastructure.
- [DONE] Define isolated Oracle AI Database 26ai Free Docker service.
  - Evidence: `docker-compose.yml` service `db` uses `container-registry.oracle.com/database/free:latest`, `1521:1521`, and `/opt/oracle/oradata`.
  - Source: Planning document sections 1, 3, 5, 8, and 16.
  - Notes: Docker was not started; this is static skeleton alignment only.
- [DONE] Define required Docker resource names.
  - Evidence: `docker-compose.yml`; `docs/docker-lab-design.md`
  - Source: Project rules fixed names; planning document Decision 004.
  - Notes: Uses `oracle-dev-ai-lab-db`, `oracle-dev-ai-lab-u01`, `oracle-dev-ai-lab-net`, and `FREEPDB1`.
- [DONE] Create lab lifecycle scripts.
  - Evidence: `scripts/lab-up.sh`, `scripts/lab-down.sh`, `scripts/lab-reset.sh`, `scripts/lab-backup.sh`, and `scripts/lab-restore.sh`
  - Source: Planning document section 7; Stage 2 row in section 12.
  - Notes: Scripts are Bash-oriented and include startup, stop, reset, backup, and restore behavior using project names.

## Stage 3 - Lab Schemas

- [DONE] Create managed lab user SQL files.
  - Evidence: `db/install/00_create_lab_users.sql`
  - Source: Planning document sections 7 and 8.
  - Notes: Goal 008 creates or updates required local users `AI_APP_OWNER`, `AI_APP_RUNTIME`, `AI_APP_READONLY`, and `AI_REVIEWER` with password substitution variables supplied by the official install workflow. Runtime validation remains not run.
- [DONE] Create managed schema SQL files.
  - Evidence: `db/install/01_create_schema.sql` and `db/install/install.sql`
  - Source: Planning document section 7; golden rule.
  - Notes: Goal 007 created the controlled install entry point and schema setup skeleton. Goal 008 adds only the infrastructure `LAB_SMOKE_TEST` object; no business objects or functional release-management SQL were added.
- [DONE] Create database source directories.
  - Evidence: `db/src/`, `db/src/tables/`, `db/src/constraints/`, `db/src/indexes/`, `db/src/views/`, `db/src/packages/`, `db/src/triggers/`, and `db/src/seed/`
  - Source: Planning document section 7.
  - Notes: Goal 004 created the source directory structure; Goal 008 adds the first infrastructure table source file under `db/src/tables/`.
- [NOT_APPLICABLE_YET] Verify lab users in a database.
  - Evidence: Runtime Oracle validation has not been run.
  - Source: Planning document sections 8, 13, and 16.
  - Notes: DB verification depends on a running local lab container and local secrets that are not committed to Git.

## Stage 4 - Spec Pipeline

- [DONE] Create release-management spec directory.
  - Evidence: `specs/001-release-management/`
  - Source: Planning document sections 6, 7, 9, and 10.
  - Notes: Goal 004 created the directory; Goal 009 adds the skeleton specification artifacts.
- [DONE] Create semantic `spec.html`.
  - Evidence: `specs/001-release-management/spec.html`
  - Source: Planning document section 10.
  - Notes: Includes required semantic sections, stable requirement IDs, stable acceptance criteria IDs, and optional PL/SQL API section for the Infrastructure MVP.
- [DONE] Create generated/derived spec files.
  - Evidence: `specs/001-release-management/spec.json`, `specs/001-release-management/TODO.md`, and `specs/001-release-management/traceability-matrix.md`
  - Source: Planning document section 9.
  - Notes: Generated artifacts are deterministic skeleton outputs traceable to `REQ-*` and `AC-*` IDs.
- [DONE] Create task directory and task files.
  - Evidence: `specs/001-release-management/tasks/` and `specs/001-release-management/tasks/T001-spec-pipeline-placeholder.md`
  - Source: Planning document sections 7 and 11.
  - Notes: The placeholder task includes source requirements, acceptance criteria, required behavior, and success criteria without starting functional implementation.
- [DONE] Create spec pipeline tools.
  - Evidence: `tools/extract_spec.py`, `tools/validate_spec.py`, `tools/generate_todo.py`, and `tools/generate_tasks.py`
  - Source: Planning document section 7; Stage 4 row in section 12.
  - Notes: Goal 009 implements deterministic skeleton tooling only. PL/SQL skeleton generation remains out of scope because functional generation is not allowed in this goal.
- [DONE] Add unittest coverage for repository/spec contracts.
  - Evidence: `tests/test_spec_pipeline.py`
  - Source: Planning document section 13.
  - Notes: Tests use Python `unittest` and require no network, secrets, Docker, Oracle, or external services.

## Stage 5 - Install/Test Workflow

- [PARTIAL] Generic `scripts/test.sh` exists.
  - Evidence: `scripts/test.sh`
  - Source: Repository observation; project rules standard tests.
  - Notes: It runs unittest locally or inside generic app Docker targets; it does not install or test Oracle DB artifacts.
- [DONE] Create database install workflow script.
  - Evidence: `scripts/install-db.sh`; `docs/install-workflow.md`
  - Source: Planning document sections 5, 7, 12, and 16.
  - Notes: Script targets only `oracle-dev-ai-lab-db`, loads local environment placeholders, and runs only `db/install/install.sql`.
- [DONE] Create database test workflow script.
  - Evidence: `scripts/run-db-tests.sh`
  - Source: Planning document sections 5, 7, 12, and 13.
  - Notes: Goal 008 adds a local-container-only SQL smoke test runner that executes managed files from `db/tests/sql/`.
- [DONE] Create DB test directories.
  - Evidence: `db/tests/`, `db/tests/sql/`, and `db/tests/utplsql/`
  - Source: Planning document section 7.
  - Notes: Goal 004 created the directories; Goal 008 adds SQL smoke tests under `db/tests/sql/`.
- [DONE] Add minimal smoke object for Infrastructure MVP.
  - Evidence: `db/src/tables/lab_smoke_test.sql`
  - Source: Planning document section 5.
  - Notes: `LAB_SMOKE_TEST` is an infrastructure smoke object only and not a business feature.
- [NOT_APPLICABLE_YET] Run clean install on a lab DB.
  - Evidence: Runtime Oracle install validation has not been run.
  - Source: Planning document sections 13 and 16.
  - Notes: Depends on a running local lab container and local secrets that are not committed to Git.

## Stage 6 - Review Workflow

- [DONE] Create review script.
  - Evidence: `scripts/review-db-code.sh`
  - Source: Planning document sections 7, 12, and 14.
  - Notes: Goal 010 adds a static, repository-only review script that validates required review workflow artifacts and managed DB source conventions.
- [DONE] Create review output area.
  - Evidence: `db/review/` and `db/review/review-report.md`
  - Source: Planning document sections 7 and 14.
  - Notes: Goal 004 created the directory and Goal 010 adds the review report template.
- [DONE] Define review report contents.
  - Evidence: `db/review/review-report.md`
  - Source: Planning document section 14.
  - Notes: The template includes required sections, severity levels, and the rule that release packaging is not approved if any BLOCKER exists.
- [NOT_APPLICABLE_YET] Produce review report without BLOCKER findings.
  - Evidence: Full review execution and release approval remain out of scope for the skeleton.
  - Source: Planning document sections 14 and 16.
  - Notes: Goal 010 creates the review workflow skeleton only; runtime diagnostics and release approval require later explicit review execution.

## Stage 7 - Packaging Workflow

- [TODO] Create package script.
  - Evidence: `scripts/package-release.sh` is missing.
  - Source: Planning document sections 7, 12, and 15.
  - Notes: Should create a release package only after install/test/review workflows exist.
- [TODO] Create package output area.
  - Evidence: `db/dist/` does not exist.
  - Source: Planning document sections 7 and 15.
  - Notes: Expected output pattern is `db/dist/release_001/`.
- [TODO] Define release package manifest and contents.
  - Evidence: No `manifest.md`, packaged `install.sql`, `rollback.sql`, reports, or `src/` package output exist.
  - Source: Planning document section 15.
  - Notes: Package should include install, rollback, test report, review report, deployment notes, and source files.
- [NOT_APPLICABLE_YET] Build release package.
  - Evidence: Packaging script and DB artifacts are missing.
  - Source: Planning document section 16.
  - Notes: Depends on Stages 5 and 6.

## Stage 8 - Functional Iterations

- [NOT_APPLICABLE_YET] Implement release-management business tables.
  - Evidence: Infrastructure MVP is not complete; no `db/src/tables/` exists.
  - Source: Planning document sections 5, 6, and 17.
  - Notes: Functional work starts only after Infrastructure MVP completion.
- [NOT_APPLICABLE_YET] Implement release-management constraints, indexes, and views.
  - Evidence: Infrastructure MVP is not complete; no DB source structure exists.
  - Source: Planning document sections 6, 7, and 17.
  - Notes: Candidate entities include release requests, items, environments, statuses, approvals, and execution log.
- [NOT_APPLICABLE_YET] Implement release-management PL/SQL packages.
  - Evidence: Infrastructure MVP is not complete; no `db/src/packages/` exists.
  - Source: Planning document sections 6, 10, and 17.
  - Notes: PL/SQL API is not required for the Infrastructure MVP.
- [NOT_APPLICABLE_YET] Add functional seed data and tests.
  - Evidence: Infrastructure MVP is not complete; no `db/src/seed/` or `db/tests/` exists.
  - Source: Planning document sections 6, 7, 13, and 17.
  - Notes: Functional tests should be traceable to requirement IDs once the spec exists.
- [NOT_APPLICABLE_YET] Produce functional review and release package.
  - Evidence: Infrastructure MVP is not complete.
  - Source: Planning document sections 14, 15, and 17.
  - Notes: Functional package readiness depends on the infrastructure workflows.

## Open questions

- [TODO] Confirm whether the existing Flask/Python template app should remain in the repository long term.
  - Evidence: `src/oracle_ai_lab/`, `templates/`, `static/`, and Flask dependencies exist, but first-stage scope is Oracle database objects only.
  - Source: Planning document section 7; repository observation.
  - Notes: Do not remove or refactor without an explicit decision.
- [TODO] Confirm whether generic Docker app files should be retained, replaced, or separated from Oracle DB Docker infrastructure.
  - Evidence: `Dockerfile` and compose files run a Flask app, not Oracle AI Database 26ai Free.
  - Source: Planning document sections 3 and 8; repository observation.
  - Notes: This task does not change Docker files.
- [TODO] Confirm exact Stage 0 document ownership and approval process.
  - Evidence: `docs/project-charter.md`, `docs/safety-rules.md`, and `docs/decision-log.md` are missing.
  - Source: Planning document Decision 010.
  - Notes: Stage 0 is mandatory before implementation.
- [TODO] Confirm whether generated Python cache and Ruff cache files should be ignored/cleaned in a later housekeeping task.
  - Evidence: `__pycache__/` and `.ruff_cache/` files are visible in the repository working tree scan.
  - Source: Repository observation.
  - Notes: Not changed in this task because it is outside the requested scope.

## Immediate next recommended task

- [TODO] Run `docs/codex-goals/goal-004-repository-structure.md`.
  - Evidence: Goals 002 and 003 are now satisfied; `specs/001-release-management/`, `db/`, `tools/`, and the target Oracle lab folders are still missing.
  - Source: `docs/codex-goals/GOALS_INDEX.md`; `docs/codex-goals/goal-004-repository-structure.md`; repository observation.
  - Notes: Continue with the next incomplete goal in the sequence. Do not add Docker runtime, DB SQL, install, review, packaging, spec pipeline, or functional implementation outside their later goals.
