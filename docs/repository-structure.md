# Repository Structure

## Purpose

This document describes the retained Python starter structure, the governance
documentation, the Oracle Docker skeleton from Goal 006, and the repository
folders created by Goal 004 for `oracle-dev-ai-lab`.

This document is descriptive. Goal 004 creates folder structure only. It does
not add Oracle SQL, schemas/users, install workflow, smoke objects, DB tests,
review workflow, packaging workflow, or functional release-management
implementation.

## 1. Retained Python Starter Structure

The repository still preserves the useful starter tooling from the original
Python template:

```text
README.md
AGENTS.md
TODO.md
.env.example
.gitignore
.github/
Dockerfile
docker-compose.yml
docker-compose.dev.yml
docker-compose.qa.yml
docs/
scripts/
src/oracle_ai_lab/
static/
templates/
tests/
pyproject.toml
requirements.in
requirements.txt
```

The retained Flask app, templates, static files, generic Docker files, and
Python tests are starter tooling only. They are not the Oracle database lab
runtime.

## 2. Governance Documentation

The governance documentation area is:

```text
docs/
  01_Setting-AI-oracle-lab.html
  project-charter.md
  safety-rules.md
  decision-log.md
  repository-structure.md
  codex-workflow.md
  codex-goals/
  stages/
```

The governance documents define the project rules, stage order, safety policy,
and stage-report requirements.

## 3. Oracle Docker Skeleton From Goal 006

Goal 006 already added the local Oracle Docker lab skeleton. That skeleton is
still retained and is separate from the Goal 004 folder-structure work:

```text
docker-compose.yml
.env.example
scripts/
  lab-up.sh
  lab-down.sh
  lab-reset.sh
  lab-backup.sh
  lab-restore.sh
docs/
  docker-lab-design.md
```

This skeleton defines the Docker naming and runtime conventions only. It does
not prove Oracle runtime compatibility until Docker is actually started and
validated.

## 4. Goal 004 Oracle Lab Repository Structure

Goal 004 adds the missing Oracle lab folder structure while keeping the retained
Python starter layout intact. The newly created folders are:

```text
specs/
  001-release-management/
    README.md
    tasks/
      README.md

db/
  README.md
  install/
    README.md
  src/
    README.md
    tables/
      README.md
    constraints/
      README.md
    indexes/
      README.md
    views/
      README.md
    packages/
      README.md
    triggers/
      README.md
    seed/
      README.md
  rollback/
    README.md
  tests/
    README.md
    sql/
      README.md
    utplsql/
      README.md
  review/
    README.md
  generated/
    README.md
  dist/
    README.md

tools/
  README.md
```

The placeholder READMEs exist only to keep otherwise-empty directories tracked
in Git and to explain where future implementation files belong.

## 5. Future Implementation Files Still Intentionally Missing

The following files and workflows are still intentionally missing after Goal 004:

```text
db/install/install.sql
db/install/00_create_lab_users.sql
db/install/01_create_schema.sql
db/rollback/rollback.sql
db/src/tables/*.sql
db/src/constraints/*.sql
db/src/indexes/*.sql
db/src/views/*.sql
db/src/packages/*.sql
db/src/triggers/*.sql
db/src/seed/*.sql
db/tests/sql/*.sql
db/tests/utplsql/*
db/review/review-report.md
db/generated/*
db/dist/*
scripts/install-db.sh
scripts/run-db-tests.sh
scripts/review-db-code.sh
scripts/package-release.sh
tools/extract_spec.py
tools/validate_spec.py
tools/generate_todo.py
tools/generate_tasks.py
```

Goal 004 does not create the functional release-management entities or any
smoke-test object such as `LAB_SMOKE_TEST`.

## 6. Structure Rules

- Preserve retained Python starter infrastructure until a later goal explicitly
  changes it.
- Do not add DB SQL implementation files in Goal 004.
- Do not add install, review, package, or spec pipeline implementation artifacts
  in Goal 004.
- Every new implementation file must be traceable to a goal, task, requirement,
  or decision.
