# Project Charter

## Purpose

This document defines the purpose, boundaries, current phase, and governance
references for `oracle-dev-ai-lab`.

## Project Identity

- Project display name: `DEVELOPMENT in Oracle using AI Lab`
- Technical repository name: `oracle-dev-ai-lab`
- Python package name retained for starter tooling: `oracle_ai_lab`

## Project Purpose

The project exists to build an isolated Oracle development lab where AI/Codex can
develop Oracle database objects from structured specifications, run tests and
review checks, and eventually create a release package.

The lab is intentionally repository-first. GitHub and repository state are the
source of truth. Database runtime state is disposable and can be recreated from
versioned repository files.

## Current Phase

The Infrastructure MVP is complete and merged; the first functional Oracle DB
iteration has not started. Docker lab infrastructure, managed install, SQL smoke
tests, static review, packaging skeleton, and specification tooling exist.
T015 handoff documentation was merged in PR #24 on 2026-05-22.

Local Oracle runtime validation was recorded by Goal 014 / PR #22 at the
`v0.1.0` baseline. That historical evidence does not guarantee a fresh runtime
succeeds. See [the closure record](infrastructure-mvp-closure.md) and
[the current ledger](../TODO.md). A separate functional goal must satisfy
[the readiness gate](functional-readiness-checklist.md), including revalidation
of missing or stale evidence, before business objects are implemented.

## Source of Truth

GitHub and the repository files are the source of truth.

If database state conflicts with Git state, Git state wins. The database must be
recreated from repository files rather than patched manually.

## Database Runtime Policy

Database runtime state is disposable. The lab database is a build/test runtime
artifact, not the authoritative project state.

All future schema and database changes must be represented as versioned SQL files
and executed through official repository scripts.

## First MVP

The first MVP is an Infrastructure MVP.

It must prove that the lab can:

- create and reset an isolated Oracle Docker lab runtime;
- create lab users and schemas through managed files;
- run controlled install scripts;
- run repository and DB smoke tests;
- run review scripts;
- create a release package from versioned files.

The Infrastructure MVP is not a business application implementation.

## First Functional Use Case

The first future functional use case is a fictional release-to-production
management system.

Functional development must wait until the Infrastructure MVP is stable, tested,
reviewed, packaged, and approved.

Candidate future entities may include release requests, release items, release
environments, release statuses, release approvals, and release execution logs, but
they have not been implemented.

## Out of Scope for the Current Phase

The following are out of scope for the current phase:

- APEX;
- ORDS;
- REST APIs;
- UI/frontend work;
- real organizational integrations;
- organizational production databases;
- organizational development databases;
- organizational test databases;
- organizational staging databases.

## Governance References

Read these files together:

- `docs/01_Setting-AI-oracle-lab.html`
- `docs/project-charter.md`
- `docs/safety-rules.md`
- `docs/decision-log.md`
- `docs/repository-structure.md`
- `docs/codex-workflow.md`
- `AGENTS.md`
- `TODO.md`
- `.agents/oracle-ai-lab-codex-planner/references/project-rules.md`

If these documents conflict with retained starter/template text, the Oracle AI Lab
governance documents and `AGENTS.md` take precedence.
