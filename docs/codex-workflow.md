# Codex Workflow

## Purpose

This document defines the Oracle AI Lab workflow for Codex and other AI-assisted
development in `oracle-dev-ai-lab`.

## Required Reading Before Every Codex Task

Before editing, Codex must read:

```text
AGENTS.md
.agents/oracle-ai-lab-codex-planner/SKILL.md
.agents/oracle-ai-lab-codex-planner/references/project-rules.md
docs/01_Setting-AI-oracle-lab.html
TODO.md
```

For goal-based work, Codex must also read:

```text
docs/codex-goals/GOALS_INDEX.md
docs/codex-goals/goal-XXX-*.md
```

When governance details matter, read:

```text
docs/project-charter.md
docs/safety-rules.md
docs/decision-log.md
docs/repository-structure.md
```

## Branching

Run before starting:

```bash
git fetch
```

Use branch prefix:

```text
codex-cli/
```

For goal-based work, prefer:

```text
codex-cli/goal-xxx-short-name
```

Branches should start from current `origin/main` unless the task explicitly says
otherwise.

## Goal Order and Commit Discipline

Run goals in the order defined by:

```text
docs/codex-goals/GOALS_INDEX.md
```

Default discipline:

```text
One goal = one focused commit.
```

Exception: adjacent documentation/governance goals may be grouped only when the
repository owner explicitly requests a combined task.

Do not implement future goals early.

## Safety Rules

Codex must:

- work only inside this repository;
- avoid unrelated files;
- avoid secrets and real credentials;
- use `unittest`, not `pytest`;
- avoid ad-hoc DDL and DML;
- avoid organizational database connections;
- connect only to local container `oracle-dev-ai-lab-db` when DB work is required
  and the lab exists;
- represent every database change as a versioned SQL file;
- run schema/database changes only through official repository scripts.

Documentation-only tasks must not connect to any database.

## Standard Checks

Run:

```bash
scripts/test.sh quick
scripts/lint.sh
```

If `python` is not on the shell `PATH`, run:

```bash
PATH=.venv/bin:$PATH scripts/test.sh quick
PATH=.venv/bin:$PATH scripts/lint.sh
```

Direct unittest fallback:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

If needed:

```bash
PATH=.venv/bin:$PATH PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

Do not claim Docker, Oracle DB, install, review, packaging, or release
compatibility unless the relevant checks actually ran and passed.

## Stage Reports

Every implementation or governance task must create or update a Hebrew standalone
HTML stage report under:

```text
docs/stages/
```

The report must start with:

```html
<!doctype html>
<html lang="he" dir="rtl">
```

The report must include:

- stage number;
- task or goal id;
- task title;
- date;
- files created;
- files updated;
- decisions documented or implemented;
- assumptions;
- commands run;
- checks/tests run;
- checks/tests not run and why;
- test results;
- known limitations;
- next recommended goal or task.

## Final Codex Response Format

Final responses for implementation and governance tasks should include:

```text
Summary

Files created

Files updated

Commands run

Checks/tests run

Checks/tests not run and why

Assumptions

Limitations

Recommended next goal

Branch name

Commit hash
```

If a task requires a different final format, follow the task.

## PR and Review Expectations

Before opening or reviewing a PR, verify:

- the diff is focused on the requested goal or task;
- no unrelated files were modified;
- no future-goal implementation was added early;
- no secrets were added;
- `unittest` remains the Python test framework;
- required checks were run or explicitly explained;
- the Hebrew stage report exists;
- `TODO.md` reflects completed goal status accurately;
- database work, if any, is represented as versioned SQL files and official
  scripts only.

Review findings should identify blockers first, then major issues, then minor
improvements.
