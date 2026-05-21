# Repository Structure

## Purpose

This document describes the current retained starter structure, the target Oracle
lab infrastructure structure, and the future functional iteration structure for
`oracle-dev-ai-lab`.

This document is descriptive. It does not create the full target structure.

## Current Retained Python Starter Infrastructure

The repository currently includes useful starter infrastructure retained from the
original Python template:

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

The retained Flask app, templates, static files, generic Docker files, and Python
tests are starter tooling only. They are not the Oracle database lab runtime.

## Governance Documentation

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

## Target Oracle Lab Infrastructure Structure

The following paths are expected in later infrastructure goals. They are not all
created in this documentation/governance task.

```text
docs/
  project-charter.md
  safety-rules.md
  decision-log.md
  repository-structure.md
  codex-workflow.md
  stages/

specs/
  001-release-management/
    spec.html
    spec.json
    TODO.md
    traceability-matrix.md
    tasks/

db/
  install/
  src/
  rollback/
  tests/
  review/
  generated/
  dist/

scripts/
  lab-up.sh
  lab-down.sh
  lab-reset.sh
  lab-backup.sh
  lab-restore.sh
  install-db.sh
  run-db-tests.sh
  review-db-code.sh
  package-release.sh
  test.sh

tools/
```

## Target DB Source Categories

Future `db/src/` content should be organized by object type:

```text
db/src/
  tables/
  constraints/
  indexes/
  views/
  packages/
  triggers/
  seed/
```

Triggers require explicit justification.

## Future Functional Iteration Structure

Future functional work for the fictional release-to-production management system
must wait until Infrastructure MVP is stable and approved.

Functional work may later add:

```text
specs/001-release-management/
  spec.html
  spec.json
  TODO.md
  traceability-matrix.md
  tasks/

db/src/
  tables/
  constraints/
  indexes/
  views/
  packages/
  triggers/
  seed/

db/tests/
  sql/
  utplsql/
```

Candidate future entities may include:

- `RELEASE_REQUESTS`
- `RELEASE_ITEMS`
- `RELEASE_ENVIRONMENTS`
- `RELEASE_STATUSES`
- `RELEASE_APPROVALS`
- `RELEASE_EXECUTION_LOG`

These are not part of the current governance documentation task.

## Structure Rules

- Do not create the full target structure unless the current goal explicitly asks
  for it.
- Do not add DB SQL implementation files in documentation-only tasks.
- Preserve retained Python starter infrastructure until a later goal explicitly
  changes it.
- Every new implementation file must be traceable to a goal, task, requirement, or
  decision.
