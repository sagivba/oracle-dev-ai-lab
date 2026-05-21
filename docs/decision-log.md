# Decision Log

## Purpose

This document records stable project decisions for `oracle-dev-ai-lab`. Decision
identifiers are stable and should be referenced from tasks, documentation, tests,
review findings, and implementation files when relevant.

## Decisions

### DEC-001 - Project Display Name

Project display name is `DEVELOPMENT in Oracle using AI Lab`.

### DEC-002 - Technical Repository Name

Technical repository name is `oracle-dev-ai-lab`.

### DEC-003 - Source of Truth

GitHub/repository state is the source of truth.

### DEC-004 - Disposable Database Runtime

Database runtime state is disposable.

### DEC-005 - Docker Container Name

Docker container name must be `oracle-dev-ai-lab-db`.

### DEC-006 - Docker Volume Name

Docker volume name must be `oracle-dev-ai-lab-u01`.

### DEC-007 - Docker Network Name

Docker network name must be `oracle-dev-ai-lab-net`.

### DEC-008 - Oracle PDB Name

Oracle PDB must be `FREEPDB1`.

### DEC-009 - Oracle Version

Oracle version must be Oracle AI Database 26ai Free.

### DEC-010 - No Ad-Hoc DDL or DML

Codex must not execute ad-hoc DDL or DML.

### DEC-011 - Python Test Framework

Python tests must use `unittest`, not `pytest`.

### DEC-012 - Future PL/SQL Unit Test Framework

Business PL/SQL unit tests will use utPLSQL in functional iterations.

### DEC-013 - First MVP

First MVP is Infrastructure MVP.

### DEC-014 - Functional Work Gate

Functional development starts only after Infrastructure MVP is stable and
approved.

### DEC-015 - First Functional Use Case

First functional use case is a fictional release-to-production management system.

### DEC-016 - Governance Before Implementation

Stage 0 / project governance documentation is mandatory before implementation.

### DEC-017 - Out-of-Scope Current Phase

APEX, ORDS, REST APIs, UI/frontend work, real organizational integrations, and
organizational production/development/test/staging databases are out of scope for
the current phase.

### DEC-018 - Versioned Database Changes

Every schema or database change must be represented as a versioned SQL file and
run only through official repository scripts.

### DEC-019 - Compatibility Claims Require Checks

Docker, Oracle, DB, install, review, package, and release compatibility must not
be claimed unless the relevant checks actually ran and passed.

## Source References

These decisions are derived from:

- `docs/01_Setting-AI-oracle-lab.html`
- `.agents/oracle-ai-lab-codex-planner/references/project-rules.md`
- `AGENTS.md`
- `docs/project-charter.md`
- `docs/safety-rules.md`
