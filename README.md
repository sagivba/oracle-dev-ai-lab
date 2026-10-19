# DEVELOPMENT in Oracle using AI Lab

`oracle-dev-ai-lab` is the repository for an isolated Oracle development lab where
AI/Codex can help develop Oracle database objects from structured specifications,
run tests and review checks, and eventually produce a release package.

This repository is not a generic Python/Flask template project. It still preserves
useful starter infrastructure from the original template, including Python 3.12+,
`unittest`, scripts, CI, and optional Flask/Docker app scaffolding, but Oracle AI Lab
project instructions govern all project work.

## Current Status

The Infrastructure MVP is implemented and merged to `main`. The first functional
release-management database iteration has **not started**.

| Area | Implemented baseline | Evidence and limits |
| --- | --- | --- |
| Oracle Docker lab | `docker-compose.yml` (`db` service), `.env.example`, `scripts/lab-{up,down,reset,backup,restore}.sh` | Local disposable lab infrastructure; file presence alone does not prove startup or backup/restore success. |
| Managed install and DB smoke tests | `db/install/`, `scripts/install-db.sh`, `AI_APP_OWNER.LAB_SMOKE_TEST`, `db/tests/sql/`, `scripts/run-db-tests.sh` | Infrastructure-only users/schema and smoke object; no business objects. |
| Static review and packaging | `scripts/review-db-code.sh`, `scripts/package-release.sh`, `tools/package_release.py`, `db/dist/release_001/` | Review/package skeletons exist. Generated package entry points do not perform deployment and the package is not approved for deployment. |
| Specification and readiness | `tools/` spec pipeline, placeholder `specs/001-release-management/`, `docs/functional-readiness-checklist.md` | Planning and traceability exist; functional implementation requires a separate approved goal. |
| Handoff documentation (T015) | `docs/README.md`, `docs/stages/README.md`, Flask/CI scope documentation and Compose service comment | Completed in [PR #24](https://github.com/sagivba/oracle-dev-ai-lab/pull/24), merged on 2026-05-22. |

**Historical validation:** [PR #22](https://github.com/sagivba/oracle-dev-ai-lab/pull/22)
records manual local Dev validation on 2026-05-22 at the `v0.1.0` baseline:
Oracle readiness, clean install after reset, SQL smoke tests, static review, and
package generation. See [the closure record](docs/infrastructure-mvp-closure.md)
and [the Goal 014 report](docs/stages/stage-014-local-oracle-lab-runtime-validation.html).
This is recorded prior evidence, not a fresh execution against today's environment.
Repeated install on an already-installed lab, portability to other developers,
backup/restore, and Oracle 19c compatibility are not established by that record.

**Current documentation reconciliation:** no Oracle container startup, install,
SQL smoke tests, or backup/restore was run. No fresh Oracle runtime or deployment
compatibility is claimed. Repository-only checks do not replace those checks.

The Flask starter is retained-but-frozen: it supports Python/test/CI tooling and
must not be extended during functional Oracle DB iterations without an explicit
new decision. CI runs Python tests and lint; it does not validate live Oracle.

Use [TODO.md](TODO.md) for current status and the next action, and
[docs/README.md](docs/README.md) for documentation navigation. The next step is to
define the first functional goal and satisfy the readiness gate, including fresh
validation wherever the existing evidence is stale or insufficient.

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

`docker-compose.yml` contains the Oracle `db` service and a separate retained
Flask `app` service. The Oracle lifecycle scripts operate on the `db` service;
use [the Docker lab guide](docs/docker-lab-design.md) and
[the managed install guide](docs/install-workflow.md) for local setup.

After creating an untracked `.env` and replacing all required password
placeholders locally, the lab workflow is:

```bash
scripts/lab-up.sh
docker logs oracle-dev-ai-lab-db | grep 'DATABASE IS READY TO USE!'
# Continue only after the readiness marker appears.
scripts/install-db.sh
scripts/run-db-tests.sh smoke
```

These are runtime instructions, not commands executed during this documentation
change. Startup requests alone do not prove readiness. The default image tag is
`latest`, so prior validation does not guarantee the same image on a later pull.

## Repository Structure

See [the repository structure guide](docs/repository-structure.md) for current
paths and responsibilities. The original planning document describes the target;
not every planned business feature has been implemented.

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
