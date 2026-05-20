# /goal 006 - Add Oracle Docker Lab Skeleton

## Goal

Add Docker lab skeleton for Oracle AI Database 26ai Free without requiring a full working database install yet.

## Prompt to use with Codex

```text
/goal
Add the Oracle Docker lab skeleton for oracle-dev-ai-lab.

Create or update:
- docker-compose.yml
- .env.example
- scripts/lab-up.sh
- scripts/lab-down.sh
- scripts/lab-reset.sh
- scripts/lab-backup.sh
- scripts/lab-restore.sh
- docs/docker-lab-design.md

Mandatory Docker names:
- Container: oracle-dev-ai-lab-db
- Volume: oracle-dev-ai-lab-u01
- Network: oracle-dev-ai-lab-net
- PDB: FREEPDB1

Oracle version:
- Oracle AI Database 26ai Free

Rules:
- Do not put real passwords or secrets in repository files.
- Use .env.example for placeholder variables only.
- Scripts must be safe and explicit.
- lab-reset.sh must clearly warn that it removes the disposable lab runtime.
- Do not connect to organizational databases.

Do not implement application schema SQL in this goal.

Success criteria:
- Docker Compose uses mandatory resource names.
- .env.example contains placeholders only.
- Scripts are executable or documented as shell scripts.
- Existing unittest tests pass.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add Oracle Docker lab skeleton
```
