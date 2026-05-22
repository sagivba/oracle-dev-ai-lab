# Documentation Index

## Purpose

This directory contains the project documentation for `oracle-dev-ai-lab`.

Use this file as the first navigation point for understanding which documents are active project guidance, which documents are workflow references, and which documents are historical records.

The repository is an isolated Oracle AI Lab. Git is the source of truth, and the local Oracle Docker database is disposable runtime state.

## Documentation categories

### Live governance documents

These documents define the current rules and boundaries of the project:

- `project-charter.md` - project purpose, scope, and operating assumptions.
- `safety-rules.md` - database, secret, and environment safety rules.
- `decision-log.md` - accepted project decisions and their rationale.
- `repository-structure.md` - intended repository layout and directory responsibilities.
- `codex-workflow.md` - AI/Codex working workflow and expectations.

Treat these documents as active guidance.

### Live workflow and reference documents

These documents explain how current repository workflows are expected to work:

- `docker-lab-design.md` - local Oracle Docker lab design.
- `install-workflow.md` - controlled database install workflow.
- `testing-strategy.md` - Python and database testing approach.
- `review-workflow.md` - static review workflow.
- `packaging-workflow.md` - deterministic release package workflow.
- `functional-readiness-checklist.md` - gate before functional Oracle DB work.
- `infrastructure-mvp-closure.md` - Infrastructure MVP completion status and boundary.

Treat these documents as active references unless a later decision explicitly replaces them.

### Planning source

- `01_Setting-AI-oracle-lab.html`

This document is the original planning and design source for the lab. It is useful for project context, but current implementation work should follow the active governance, workflow documents, `AGENTS.md`, and `TODO.md`.

### Historical stage reports

- `stages/`

This directory contains completed Hebrew stage reports. These files are historical records of work already performed. They are not active implementation instructions.

See `stages/README.md` before using files from that directory.

### Codex goal files

- `codex-goals/`

This directory contains goal/task source material used to drive staged implementation work. It is useful for traceability and historical task review.

Do not assume that an older goal file describes the next current action. Use `TODO.md` and the current branch/task context for the next action.

### Generated and specification-related artifacts

Specification artifacts live outside this directory under:

- `../specs/001-release-management/`

The generated files under `specs/` are deterministic artifacts of the specification pipeline. If they appear out of sync, run the relevant tools and review the generated diff rather than editing generated output blindly.

## Retained Flask starter status

The retained Flask/Python starter surface is frozen.

Files under `src/oracle_ai_lab/`, `templates/`, and `static/` remain as retained Python, test, and CI starter infrastructure. They are not part of the Oracle database lab runtime and must not be extended during functional Oracle DB iterations unless a future explicit decision changes their role.

## CI validation scope

GitHub Actions currently validates repository-level Python contracts and lint checks.

A green CI run does not prove that the Oracle Docker database started, that SQL was installed, or that SQL smoke tests passed against a live Oracle container.

Local Oracle runtime validation remains a local lab responsibility unless a later project decision adds Oracle integration validation to CI.

## How to choose what to read

For a new task, start with:

1. `../AGENTS.md`
2. `../TODO.md`
3. this `docs/README.md`
4. the relevant workflow/reference document
5. the relevant spec or task file, if the task is functional

For historical context, inspect `stages/` and `codex-goals/`, but do not treat them as the active next-step source.
