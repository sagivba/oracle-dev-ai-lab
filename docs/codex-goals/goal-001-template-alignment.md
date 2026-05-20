# /goal 001 - Align Template Identity

## Goal

Adapt the repository created from `sagivba/DEVELOPMENT in Oracle using AI Lab` so its identity matches `oracle-dev-ai-lab` without adding Oracle implementation yet.

## Prompt to use with Codex

```text
/goal
Align this repository identity for the project DEVELOPMENT in Oracle using AI Lab.

Current repository should become:
- Technical repository name: oracle-dev-ai-lab
- Python package name: oracle_ai_lab
- Project display name: DEVELOPMENT in Oracle using AI Lab

Tasks:
1. Inspect README, pyproject/config files, scripts, package folders, tests, and template references.
2. Replace generic template naming with oracle-dev-ai-lab naming where appropriate.
3. Preserve useful template conventions: Python 3.12+, unittest, scripts, docs, CI, Docker-friendly structure.
4. Do not add Oracle Docker implementation yet.
5. Do not add DB SQL implementation yet.
6. Do not remove useful template infrastructure unless clearly obsolete.

Mandatory constraints:
- Do not introduce secrets.
- Do not change unrelated files.
- Do not use pytest.
- Keep changes small and reviewable.

Success criteria:
- README and package metadata identify the project as DEVELOPMENT in Oracle using AI Lab.
- Python package is named oracle_ai_lab if package renaming is needed.
- Existing Python tests still run with python -m unittest.
- No Oracle implementation is added in this goal.

Run:
python -m unittest discover
```

## Documentation to update

- `README.md`
- Project metadata file, if present
- Existing package naming, if present

## Commit suggestion

```text
Initialize oracle-dev-ai-lab project identity
```
