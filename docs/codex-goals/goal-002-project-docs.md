# /goal 002 - Create Project Documentation Baseline

## Goal

Create the mandatory baseline documentation for the project before implementation.

## Prompt to use with Codex

```text
/goal
Create the baseline documentation for DEVELOPMENT in Oracle using AI Lab.

Create or update these files:
- docs/project-charter.md
- docs/safety-rules.md
- docs/decision-log.md
- docs/repository-structure.md
- docs/codex-workflow.md

The documentation must include these approved decisions:
- Project display name: DEVELOPMENT in Oracle using AI Lab
- Repository name: oracle-dev-ai-lab
- Docker container: oracle-dev-ai-lab-db
- Docker volume: oracle-dev-ai-lab-u01
- Docker network: oracle-dev-ai-lab-net
- Oracle PDB: FREEPDB1
- Oracle version: Oracle AI Database 26ai Free
- GitHub is the only source of truth.
- Database runtime is disposable.
- First MVP is Infrastructure MVP.
- Functional development starts only after Infrastructure MVP is stable.
- Codex must not execute ad-hoc DDL/DML.
- Python tests must use unittest.
- PL/SQL business unit tests will use utPLSQL in functional iterations.

The documentation must distinguish:
1. Infrastructure MVP
2. Functional iterations
3. Future organizational integration, which is out of scope

Do not implement scripts or DB files in this goal.

Success criteria:
- All requested docs exist.
- Decision log includes numbered decisions.
- Safety rules are mandatory, not advisory.
- No implementation files are created except documentation.

Run:
python -m unittest discover
```

## Commit suggestion

```text
Add project charter and mandatory safety documentation
```
