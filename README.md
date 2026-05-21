# DEVELOPMENT in Oracle using AI Lab

`oracle-dev-ai-lab` is the repository for an isolated Oracle development lab where
AI/Codex can help develop Oracle database objects from structured specifications,
run tests and review checks, and eventually produce a release package.

This repository is not a generic Python/Flask template project. It still preserves
useful starter infrastructure from the original template, including Python 3.12+,
`unittest`, scripts, CI, and optional Flask/Docker app scaffolding, but Oracle AI Lab
project instructions govern all project work.

## Current Status

This repository is in early identity and planning alignment.

Implemented so far:

- Oracle AI Lab operating rules in `AGENTS.md`
- project planning source in `docs/01_Setting-AI-oracle-lab.html`
- staged Codex goal files in `docs/codex-goals/`
- a root `TODO.md` baseline
- retained Python starter package named `oracle_ai_lab`
- retained `unittest`, lint, CI, and optional Flask/Docker starter tooling

Not implemented yet:

- Oracle Docker lab runtime
- database schemas or SQL install files
- DB smoke tests
- review workflow
- packaging workflow
- release-management functional database objects

Do not treat the retained Flask app or generic Docker files as the final Oracle lab
implementation. They are starter infrastructure kept until later goals decide how
they should fit into the lab.

## Fixed Project Names

Use these names exactly unless a later explicit project decision changes them:

```text
Project display name: DEVELOPMENT in Oracle using AI Lab
Repository name:      oracle-dev-ai-lab
Python package name:  oracle_ai_lab
Container:            oracle-dev-ai-lab-db
Volume:               oracle-dev-ai-lab-u01
Network:              oracle-dev-ai-lab-net
PDB:                  FREEPDB1
Oracle version:       Oracle AI Database 26ai Free
```

## Start Here

Before making changes, read:

```text
AGENTS.md
.agents/oracle-ai-lab-codex-planner/SKILL.md
.agents/oracle-ai-lab-codex-planner/references/project-rules.md
docs/01_Setting-AI-oracle-lab.html
TODO.md
```

For staged implementation work, follow the goals in:

```text
docs/codex-goals/GOALS_INDEX.md
```

Run goals in order unless the expected output already exists and passes the stated
success criteria.

## Development Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create local environment overrides:

```bash
cp .env.example .env
```

The tracked `.env.example` uses placeholder/non-secret values only.

## Running Tests

This project uses `unittest`.

Preferred project command:

```bash
scripts/test.sh quick
```

Full local test output:

```bash
scripts/test.sh full local
```

Equivalent direct command:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

If your shell cannot find `python` but the repository virtual environment exists,
run:

```bash
PATH=.venv/bin:$PATH scripts/test.sh quick
```

## Lint and Formatting

Run lint checks:

```bash
scripts/lint.sh
```

If needed with the local virtual environment:

```bash
PATH=.venv/bin:$PATH scripts/lint.sh
```

Formatting commands:

```bash
python -m ruff format src tests
python -m ruff check --fix src tests
```

## Retained Python Starter App

The current Python package is:

```text
src/oracle_ai_lab/
```

It contains a small Flask starter app with a web page and health endpoint. This is
retained starter infrastructure only. It is useful for checking Python tooling, CI,
Docker scaffolding, and `unittest`, but it is not the Oracle database lab runtime.

Run it locally if needed:

```bash
PYTHONPATH=src flask --app oracle_ai_lab.app:create_app run --debug
```

Health endpoint:

```text
http://127.0.0.1:5000/api/health
```

Expected response:

```json
{
  "status": "ok"
}
```

## Docker Status

Docker files are currently retained starter app infrastructure. They do not yet
define the Oracle AI Database 26ai Free lab container.

Do not claim Oracle Docker compatibility until the relevant Docker lab goal is
implemented and tested.

Starter app Docker commands, if needed:

```bash
docker compose -p oracle_ai_lab_dev -f docker-compose.yml -f docker-compose.dev.yml up -d --build
docker compose -p oracle_ai_lab_dev -f docker-compose.yml -f docker-compose.dev.yml down
```

## Repository Structure

Current important paths:

```text
AGENTS.md
TODO.md
docs/
  01_Setting-AI-oracle-lab.html
  codex-goals/
  stages/
scripts/
src/oracle_ai_lab/
tests/
```

Target Oracle lab structure is defined in:

```text
docs/01_Setting-AI-oracle-lab.html
.agents/oracle-ai-lab-codex-planner/references/project-rules.md
```

Do not create the full target structure outside the goal that explicitly asks for it.

## AI / Codex Workflow

Use branch prefix:

```text
codex-cli/
```

For goal-based work, prefer:

```text
codex-cli/goal-xxx-short-name
```

One goal should produce one focused commit.

Each implementation task must update or create a Hebrew standalone HTML report under:

```text
docs/stages/
```

## Important Files

- `AGENTS.md`: mandatory repository instructions for Codex and AI-assisted work
- `.agents/oracle-ai-lab-codex-planner/SKILL.md`: project-specific Codex planning skill
- `.agents/oracle-ai-lab-codex-planner/references/project-rules.md`: fixed names, safety rules, and target structure
- `docs/01_Setting-AI-oracle-lab.html`: planning source document
- `docs/codex-goals/GOALS_INDEX.md`: staged goal sequence
- `TODO.md`: current repository baseline and goal status
- `scripts/test.sh`: canonical test runner
- `scripts/lint.sh`: canonical lint runner
- `.github/workflows/ci.yml`: CI definition

## Safety Rules

- Do not connect to organizational databases.
- Do not connect to any Oracle database unless the current goal explicitly requires it.
- Do not run ad-hoc DDL or DML.
- Do not add secrets or real credentials.
- Do not introduce `pytest`.
- Keep changes small, reviewable, and scoped to the current goal.
