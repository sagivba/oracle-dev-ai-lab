# Project rules for oracle-dev-ai-lab

## Fixed names

- Project display name: `DEVELOPMENT in Oracle using AI Lab`
- Repository: `oracle-dev-ai-lab`
- Container: `oracle-dev-ai-lab-db`
- Volume: `oracle-dev-ai-lab-u01`
- Network: `oracle-dev-ai-lab-net`
- PDB: `FREEPDB1`

## Core decisions

- GitHub is the only source of truth.
- The database is disposable runtime state.
- The lab must use Oracle AI Database 26ai Free in Docker.
- The first MVP is an Infrastructure MVP.
- Functional development starts only after the Infrastructure MVP is complete.
- The first functional use case is a fictional release-to-production management system.
- Stage 0 - Project Charter is mandatory before implementation.

## Scope

The initial scope is Oracle database objects only:

- tables
- constraints
- indexes
- views
- packages
- package bodies
- triggers only when justified
- seed data
- tests
- review
- packaging

Out of scope for the first stage:

- REST
- ORDS
- APEX
- UI
- organizational production/development/test databases

## Golden rule

No database change is valid unless it exists as a versioned SQL file and can be installed on a clean lab database by the official scripts.

## Required repository structure highlights

Codex tasks should preserve and use this structure unless a later approved decision changes it:

```text
docs/
  project-charter.md
  safety-rules.md
  decision-log.md
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
code/
```

## Hebrew HTML stage report required sections

Every implementation task must create or update a file under `docs/stages/` containing:

- summary
- files created
- files updated
- decisions implemented
- implementation notes
- commands run
- tests
- known limitations
- next step

## Standard tests

Prefer this default test command:

```bash
scripts/test.sh quick
```

If deeper debugging is needed:

```bash
scripts/test.sh full
```

If `scripts/test.sh` does not exist yet, Codex must state that explicitly and run the closest available repository checks.
