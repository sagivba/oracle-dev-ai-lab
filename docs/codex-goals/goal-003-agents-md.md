# /goal 003 - Create Strict AGENTS.md

## Goal

Create or replace `AGENTS.md` with strict Codex operating rules for this repository.

## Prompt to use with Codex

```text
/goal
Create a strict AGENTS.md for the oracle-dev-ai-lab repository.

AGENTS.md must define mandatory rules for Codex:
- Work only inside this repository.
- Do not connect to organizational databases.
- Connect only to local container oracle-dev-ai-lab-db when DB work is required and the lab exists.
- Do not execute ad-hoc DDL or DML.
- SELECT is allowed only for diagnostics, metadata inspection, compile checks, tests, and review.
- Every schema change must be a versioned SQL file.
- Every task must be traceable to a requirement id, task id, or decision id.
- Do not modify unrelated files.
- Do not invent missing requirements.
- Python tests must use unittest, not pytest.
- Business PL/SQL unit tests must use utPLSQL in functional iterations.
- One task should produce a small reviewable change.

AGENTS.md must also define:
- Standard test commands.
- Required final response format for Codex.
- Allowed and forbidden database actions.
- Branch naming recommendation: codex-cli/...
- Commit discipline: one goal per commit.

Do not implement Oracle files in this goal.

Success criteria:
- AGENTS.md exists and is strict.
- It is consistent with docs/project-charter.md and docs/safety-rules.md.
- It contains no secrets or environment-specific credentials.

Run:
python -m unittest discover
```

## Commit suggestion

```text
Add strict Codex operating rules
```
