# AGENTS.md

Instructions for Codex CLI, ChatGPT, and other AI-assisted development workflows in this repository.

This repository is the Oracle AI Lab project:

`DEVELOPMENT in Oracle using AI Lab`

The technical repository name is:

`oracle-dev-ai-lab`

This repository is not a generic Python/Flask template project. It may still contain template remnants, but Oracle AI Lab project instructions govern all project work.

## Required reading before any task

Before starting any task in this repository, Codex MUST read and follow:

- `.agents/oracle-ai-lab-codex-planner/SKILL.md`
- `.agents/oracle-ai-lab-codex-planner/references/project-rules.md`
- `docs/01_Setting-AI-oracle-lab.html`
- `TODO.md`

When the task touches governance, repository structure, workflow, safety, or goal
status, Codex MUST also read the relevant governance documents:

- `docs/project-charter.md`
- `docs/safety-rules.md`
- `docs/decision-log.md`
- `docs/repository-structure.md`
- `docs/codex-workflow.md`

If these files conflict with generic instructions, template text, or legacy project files, the Oracle AI Lab instructions take precedence.

## Project purpose

The purpose of this repository is to build an isolated Oracle development lab where AI/Codex can develop Oracle database objects from structured specifications, run tests and reviews, and eventually create a release package.

The database is disposable runtime state. GitHub is the source of truth.

The first MVP is an Infrastructure MVP. It must prove that the lab can be created, installed, tested, reviewed, and packaged reproducibly.

Functional development starts only after the Infrastructure MVP is complete.

## Codex goals

Codex task prompts for this project may be stored under:

- `docs/codex-goals/`

When the user asks Codex to run a goal file, Codex MUST read the referenced goal file and follow it exactly, together with this `AGENTS.md`, the project Skill, `project-rules.md`, `TODO.md`, and the planning document.

Goals SHOULD run in the order defined by:

```text
docs/codex-goals/GOALS_INDEX.md
```

Default discipline:

```text
One goal = one focused commit.
```

Adjacent documentation/governance goals may be combined only when the repository
owner explicitly requests a combined task. Do not implement future goals early.

## Fixed project names

Use these names exactly unless a later explicit project decision changes them:

```text
Repository: oracle-dev-ai-lab
Container:  oracle-dev-ai-lab-db
Volume:     oracle-dev-ai-lab-u01
Network:    oracle-dev-ai-lab-net
PDB:        FREEPDB1
```

## Scope

Initial scope is Oracle database objects and supporting repository workflows only:

- tables
- constraints
- indexes
- views
- packages
- package bodies
- triggers only when justified
- seed data
- install scripts
- rollback scripts
- tests
- review reports
- packaging output
- project documentation

Out of scope for the first phase:

- APEX
- ORDS
- REST APIs
- UI/frontend work
- organizational production/development/test databases
- direct integration with real organizational systems

## Core rules

- Keep changes small and reviewable.
- Make one logical change at a time.
- Work only inside this repository.
- Do not edit unrelated files.
- Do not perform broad refactors unless explicitly requested.
- Prefer explicit, direct, maintainable code over clever code.
- Do not introduce speculative abstractions.
- Do not add dependencies unless they are necessary and documented.
- Do not add secrets, credentials, tokens, passwords, private keys, certificates, or real connection strings.
- Update documentation when setup, commands, behavior, architecture, or workflow changes.
- Run the documented checks before claiming the task is complete.
- If a required assumption is missing, stop and report it.

## Branch naming

For Codex CLI or AI-assisted implementation work, use this branch prefix:

```text
codex-cli/
```

Examples:

```text
codex-cli/T000-project-intake-todo-baseline
codex-cli/T001-create-project-charter
codex-cli/T002-create-repo-skeleton
```

Before starting work, Codex MUST run:

```bash
git fetch
```

## Commit discipline

Each task should produce one small, reviewable commit unless the user explicitly
asks not to commit. For goal-based work, the default is one goal per commit. A
combined-goal commit is allowed only when the repository owner explicitly requests
that grouping.

## Database safety rules

Codex MUST NOT connect to organizational databases.

Codex MUST connect only to the local Docker container named `oracle-dev-ai-lab-db` when database access is needed.

Codex MUST NOT execute ad-hoc DDL or DML.

Codex MAY execute SELECT statements only for:

- diagnostics
- metadata inspection
- compile checks
- test verification
- review

Every database change MUST be represented as a versioned SQL file in the repository.

Every schema change MUST be executed only through official repository scripts.

No database change is valid unless it exists as a versioned SQL file and can be installed on a clean lab database by the official scripts.

If database state conflicts with Git state, Git state wins. Recreate the database from the repository.

## Repository structure target

The planning document defines the target structure. Important paths include:

```text
README.md
AGENTS.md
TODO.md
.env.example
.gitignore
docker-compose.yml

docs/
  01_Setting-AI-oracle-lab.html
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
```

Do not create or modify this entire structure unless the current task explicitly asks for it.

## Documentation rules

Every implementation stage MUST create or update a Hebrew standalone HTML stage report under:

```text
docs/stages/
```

Stage report filenames should follow this pattern:

```text
docs/stages/stage-XX-task-TXXX-short-name.html
```

Every stage report must start with:

```html
<!doctype html>
<html lang="he" dir="rtl">
```

The stage report must include:

- stage number
- task id
- task title
- date
- files created
- files updated
- decisions implemented
- important assumptions
- commands run
- checks/tests run
- checks/tests not run and why
- test results
- known limitations
- next recommended step

A task is not complete without the relevant stage report unless the task explicitly says no stage report is required.

## File-level documentation rules

Every created or materially updated source file, script, SQL file, Python file, shell script, or generated project file MUST start with a short purpose header.

The header should explain:

- what the file does
- where it fits in the lab workflow
- whether it changes the database, validates the repository, runs tests, performs review, or creates packaging output
- the related task id, decision id, or requirement id where applicable

For non-trivial logic, comments MUST explain why the approach is used, not merely what the next line does.

Avoid obvious comments that repeat the code.

## Testing policy

This project uses `unittest` for Python tests.

Do not introduce `pytest` unless explicitly requested.

Business PL/SQL unit tests must use utPLSQL in future functional iterations.

Run documented checks before claiming completion.

If `scripts/test.sh` exists, use it as the primary test entrypoint.

Common check:

```bash
scripts/test.sh quick
```

If the environment requires the virtual environment on PATH, use:

```bash
PATH=.venv/bin:$PATH scripts/test.sh quick
```

If `scripts/lint.sh` exists, run it when relevant:

```bash
scripts/lint.sh
```

If the environment requires the virtual environment on PATH, use:

```bash
PATH=.venv/bin:$PATH scripts/lint.sh
```

If a check cannot be run, state clearly:

- which check was not run
- why it was not run
- whether this affects confidence in the change

Do not claim Docker, Oracle DB, install, review, or package compatibility unless the relevant checks were actually executed successfully.

## Dependency rules

- Keep dependencies minimal.
- Prefer the Python standard library when practical.
- Add a dependency only when it is clearly justified.
- Update dependency files and documentation when dependencies change.
- Do not add development tools, frameworks, or libraries unrelated to the current task.
- Do not silently change the packaging approach.

## Secrets and configuration

Never commit:

- credentials
- passwords
- tokens
- private keys
- certificates
- real connection strings
- local `.env` files

Allowed to track:

```text
.env.example
```

Do not track local secret-bearing files such as:

```text
.env
.env.*
```

Use placeholder values only in examples.

## Preferred change style

Prefer:

- explicit code
- clear names
- small functions
- narrow scope
- direct control flow
- simple tests
- stable commands
- readable documentation
- traceability to a task id, requirement id, or decision id

Every task must be traceable to a goal id, task id, requirement id, or decision
id. If no traceable source exists, stop and ask for clarification before creating
implementation behavior.

Avoid:

- speculative abstractions
- hidden magic
- over-engineering
- global rewrites
- unnecessary layers
- unrelated cleanup
- renaming or moving files without a strong task-specific reason

## AI-assisted workflow

When using Codex, ChatGPT, or another AI coding tool:

- keep each task narrow and self-contained
- make one logical change at a time
- preserve existing structure unless instructed otherwise
- update docs together with code
- do not invent missing requirements
- do not create extra layers beyond the intended architecture
- do not silently change runtime assumptions
- run the documented checks before claiming completion

## Review checklist

Before submitting a change, verify:

- [ ] The diff is focused.
- [ ] The change matches the current task.
- [ ] No unrelated files were edited.
- [ ] Required documentation was created or updated.
- [ ] Required stage report exists under `docs/stages/`.
- [ ] Tests/checks were run, or skipped with a clear reason.
- [ ] No secrets or local environment files were committed.
- [ ] No unrelated formatting or cleanup was included.
- [ ] Database changes, if any, exist only as versioned SQL files.
- [ ] No ad-hoc DDL or DML was run.
- [ ] Assumptions and limitations are documented.

## Final response requirements

For implementation and governance tasks, the final Codex response should include:

- files created
- files updated
- commands run
- checks/tests run
- checks/tests not run and why
- assumptions
- limitations
- recommended next goal

If the user requests a stricter final response format, follow the user request.

## If unsure

If a requirement is unclear:

- do not invent behavior
- make the smallest safe change
- document assumptions explicitly
- ask for clarification before broad changes
- stop and report if proceeding would violate project safety rules
