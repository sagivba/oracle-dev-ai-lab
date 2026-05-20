# /goal 000 - Operating Rules for All Goals

## Goal

Establish mandatory execution rules for all later Codex goals in this repository.

## Prompt to use with Codex

```text
/goal
You are working in the oracle-dev-ai-lab repository.

Before making changes, inspect the repository structure and current files.

Mandatory project facts:
- Project display name: DEVELOPMENT in Oracle using AI Lab
- Repository name: oracle-dev-ai-lab
- Docker container: oracle-dev-ai-lab-db
- Docker volume: oracle-dev-ai-lab-u01
- Docker network: oracle-dev-ai-lab-net
- Oracle PDB: FREEPDB1
- Oracle version: Oracle AI Database 26ai Free

Mandatory rules:
- Make only the changes requested by the current goal.
- Do not implement future goals early.
- Do not connect to any organizational database.
- Do not create secrets, passwords, tokens, or real credentials.
- Do not execute ad-hoc DDL or DML against any database.
- SELECT is allowed only for diagnostics, metadata inspection, compile checks, tests, and review, and only against the local lab container when it exists.
- Any DB change must be represented as a versioned SQL file.
- Python tests must use unittest, not pytest.
- Use small, reviewable changes.
- If an assumption is required, stop and document it instead of inventing behavior.

At the end:
- Summarize changed files.
- State how to test.
- State any open assumptions.
```

## Expected output

No repository changes are required by this goal. It defines execution rules for later goals.
