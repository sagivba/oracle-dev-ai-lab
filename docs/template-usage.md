# Legacy Template Usage Notes

This repository is now the `oracle-dev-ai-lab` project for:

```text
DEVELOPMENT in Oracle using AI Lab
```

It is not currently maintained as a generic Python project template. The original
template helper script is still present as retained starter infrastructure:

```text
scripts/init_from_template.sh
```

Do not run that script as part of normal Oracle AI Lab work. It can rename package
and project references, so using it inside this repository would conflict with the
fixed project identity:

```text
Repository:     oracle-dev-ai-lab
Python package: oracle_ai_lab
Display name:   DEVELOPMENT in Oracle using AI Lab
```

## Why This File Remains

The file remains only to document that some starter infrastructure was inherited
from an earlier Python template. Useful retained pieces include:

- Python 3.12+ conventions
- `unittest`
- `scripts/test.sh`
- `scripts/lint.sh`
- GitHub Actions CI
- optional Flask/Docker starter app scaffolding

Those pieces are not the Oracle lab implementation. They are retained support
infrastructure until later Codex goals decide whether to keep, adapt, or remove
them.

## Current Project Workflow

For current work, use the Oracle AI Lab instructions instead:

```text
AGENTS.md
.agents/oracle-ai-lab-codex-planner/SKILL.md
.agents/oracle-ai-lab-codex-planner/references/project-rules.md
docs/01_Setting-AI-oracle-lab.html
TODO.md
docs/codex-goals/GOALS_INDEX.md
```

Run Codex goals in the order defined by `docs/codex-goals/GOALS_INDEX.md`, unless
the expected output already exists and passes the stated success criteria.

## Validation

Use the current project checks:

```bash
scripts/test.sh quick
scripts/lint.sh
```

If the shell cannot find `python` but the repository virtual environment exists:

```bash
PATH=.venv/bin:$PATH scripts/test.sh quick
PATH=.venv/bin:$PATH scripts/lint.sh
```
