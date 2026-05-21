---
name: oracle-ai-lab-codex-planner
description: Create, review, and refine tightly constrained Codex tasks for the DEVELOPMENT in Oracle using AI Lab project. Use when preparing Codex prompts, task files, AGENTS.md rules, repository workflow instructions, Oracle Docker lab infrastructure tasks, SQL-managed database changes, Hebrew HTML stage documentation, review workflows, packaging workflows, or enforcing the oracle-dev-ai-lab safety and traceability constraints.
---

# Oracle AI Lab Codex Planner

Use this skill to create and review Codex work instructions for the `DEVELOPMENT in Oracle using AI Lab` project.

The target repository is always:

```text
oracle-dev-ai-lab
```

Before drafting a Codex prompt or task, apply the project rules in `references/project-rules.md`.

## Core behavior

When the user asks for a Codex task, repository task, implementation step, review prompt, or infrastructure prompt:

1. Identify the current stage and task id when available.
2. Produce a strict Codex-ready prompt.
3. Include explicit allowed and forbidden actions.
4. Require traceability to a task id, requirement id, or decision id.
5. Require Hebrew HTML stage documentation under `docs/stages/`.
6. Require tests and exact commands to run.
7. Require a final Codex report that lists changed files, commands run, test results, assumptions, and limitations.
8. Remind that branches must use the `codex-cli/` prefix.
9. Explicitly authorize running `git fetch` before work starts.

## Mandatory Codex constraints

Every Codex prompt for this project must include these constraints unless the user explicitly says this is unrelated to the project:

- Work only inside the `oracle-dev-ai-lab` repository.
- Run `git fetch` before starting.
- Use a task branch with prefix `codex-cli/`.
- Do not connect to organizational databases.
- Connect only to the local Docker container named `oracle-dev-ai-lab-db` when DB access is needed.
- Do not run ad-hoc DDL or DML.
- Represent every database change as a versioned SQL file.
- Execute schema changes only through official scripts.
- SELECT statements are allowed only for diagnostics, metadata inspection, compile checks, tests, and review.
- Do not introduce secrets or credentials into the repository.
- Do not modify unrelated files.
- Stop and report if a required assumption is missing.

## Documentation rules

Every Codex implementation prompt must require:

- A short purpose header at the beginning of every created or materially updated source file, script, SQL file, Python file, shell script, or generated project file.
- Code that is clear, explicit, and readable.
- Comments for non-trivial logic that explain why the approach was chosen, not merely what a line does.
- A Hebrew standalone HTML stage report under `docs/stages/`.
- The stage report must include stage number, task id, task title, date, files created, files updated, decisions implemented, assumptions, commands run, tests run, test results, limitations, and next step.

Use this naming convention for stage documents:

```text
docs/stages/stage-XX-task-TXXX-short-name.html
```

The HTML document must start with:

```html
<!doctype html>
<html lang="he" dir="rtl">
```

## Prompt structure

Prefer this structure for Codex prompts:

```markdown
# Codex Task: TXXX - Task title

## Context
...

## Objective
...

## Files to create or update
...

## Required behavior
...

## Mandatory constraints
...

## Documentation requirements
...

## Tests to run
...

## Success criteria
...

## Final response required from Codex
...
```

## Review mode

When the user asks to review Codex output, check:

- Did Codex stay inside the expected repository scope?
- Are all DB changes represented as SQL files?
- Were official scripts used instead of ad-hoc DDL/DML?
- Do created or changed files include purpose headers?
- Are comments useful and focused on why non-trivial logic exists?
- Does the Hebrew HTML stage report exist and include required sections?
- Are tests listed and did they pass?
- Are assumptions and limitations documented?
- Were unrelated files modified?

Return blockers first, then major issues, then minor improvements.

## Style

For Codex prompts, be strict, explicit, and operational. Avoid vague wording. Prefer exact file paths, exact commands, and measurable success criteria.
