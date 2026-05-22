# /goal 014 - Record Local Oracle Lab Runtime Validation

## Goal

Record the local Oracle Lab runtime validation that was performed manually in
the Dev repository after `v0.1.0`.

This goal is documentation/governance only. It turns the manually observed Dev
validation into repository source-of-truth documentation so the project can
later tag `v0.1.1` as:

```text
Infrastructure MVP + local Oracle runtime validation baseline.
Ready to start Codex Oracle development capability study.
```

## Baseline

- Repository: `/home/sagivba-adm/src/oracle-dev-ai-lab`
- Baseline branch: `main`
- Baseline commit: `1c6b46797766656e5db537047d8e91b61853e71d`
- Baseline tag: `v0.1.0`
- AGW version observed: `v0.6.0-dev`
- AGW tool git ref observed: `v0.6.0`
- QA worktree: not touched

## Validation Evidence to Record

### 1. AGW status

Command:

```bash
source tools/ai-git-workflow-tools/scripts/load-agw.sh
agw_status
```

Result:

- `current_repository`: `/home/sagivba-adm/src/oracle-dev-ai-lab`
- `current_branch`: `main`
- `current_head`: `1c6b467`
- working tree was clean.

### 2. Initial combined validation attempt

A combined command sequence was initially run before the lab was fully prepared.
It reported missing local password configuration and was not counted as
successful runtime validation.

Observed errors:

- Create a local `.env` from `.env.example` and set `ORACLE_PWD` before starting
  the lab.
- Set `ORACLE_PWD` in local `.env` or environment before running
  `install-db.sh`.
- Set `ORACLE_PWD` in local `.env` or environment before running
  `run-db-tests.sh`.

The review and package skeletons ran during this attempt, but this attempt did
not prove Oracle runtime readiness.

### 3. Local `.env` setup

A local `.env` file was created from `.env.example`, and `ORACLE_PWD` was set
locally.

Do not commit `.env`. Do not document the password.

### 4. Lab startup

Command:

```bash
scripts/lab-up.sh
```

Result:

- Container `oracle-dev-ai-lab-db` started.
- Startup requested.
- Connection baseline:
  - Host: `localhost`
  - Port: `1521`
  - Service/PDB: `FREEPDB1`

### 5. Clean reset

Because an earlier install attempt found `LAB_SMOKE_TEST` already existed, the
disposable local runtime was reset.

Command:

```bash
scripts/lab-reset.sh --yes
```

Result:

- Removed container: `oracle-dev-ai-lab-db`
- Removed volume: `oracle-dev-ai-lab-u01`
- Removed network: `oracle-dev-ai-lab-net`

Interpretation:

The successful validation scope is a clean install on a disposable local lab
runtime. Repeated idempotent install on an already-installed lab was not
validated and must not be claimed.

### 6. Oracle readiness

Command:

```bash
docker logs oracle-dev-ai-lab-db | grep 'DATABASE IS READY TO USE!'
```

Result:

```text
DATABASE IS READY TO USE!
```

### 7. Controlled DB install

Command:

```bash
scripts/install-db.sh
```

Result:

- Files copied to `oracle-dev-ai-lab-db`.
- `00_create_lab_users.sql` ran successfully.
- `01_create_schema.sql` ran successfully.
- `db/src/tables/lab_smoke_test.sql` ran successfully.
- `AI_APP_OWNER.LAB_SMOKE_TEST` was created.
- Oracle AI Lab controlled install completed.

### 8. SQL smoke tests

Command:

```bash
scripts/run-db-tests.sh smoke
```

Result:

- `001_db_connectivity.sql` passed.
- Connected to `FREEPDB1`.
- `CURRENT_SCHEMA` was `SYS` during the smoke connectivity check.
- `002_object_inventory.sql` passed.
- `LAB_SMOKE_TEST` object inventory check passed.
- `003_no_invalid_objects.sql` passed.
- No invalid objects were found in `AI_APP_OWNER`.

Observation:

`CURRENT_SCHEMA=SYS` is recorded as an observation only, not as a failure.

### 9. Review workflow

Command:

```bash
scripts/review-db-code.sh
```

Result:

- Review skeleton checks passed.
- Report template: `db/review/review-report.md`

### 10. Package workflow

Command:

```bash
scripts/package-release.sh
```

Result:

- Release package skeleton written: `db/dist/release_001`

### 11. AGW review output

Command:

```bash
source tools/ai-git-workflow-tools/scripts/load-agw.sh
agw_review_output --run
```

Result:

- `git branch --show-current` reported `main`.
- `git status --short` produced no changes.
- `git diff --stat` produced no unexpected diff.
- `git diff --name-status` produced no unexpected diff.
- `git diff --check` passed.

## Boundaries

- Goal 014 does not implement functional DB objects.
- Goal 014 does not add business tables, constraints, indexes, seed data,
  PL/SQL packages, views, triggers, REST, ORDS, APEX, or UI.
- Goal 014 does not change runtime scripts or Oracle runtime behavior.
- Goal 014 does not access organizational databases.
- Goal 014 does not commit `.env`, passwords, or secrets.
- Goal 014 does not run ad-hoc DDL or DML.
- Goal 014 does not validate QA worktree behavior.
- Goal 014 does not validate portability or onboarding for other developers.

## Files to Create or Update

Create:

- `docs/codex-goals/goal-014-record-local-oracle-lab-runtime-validation.md`
- `docs/stages/stage-014-local-oracle-lab-runtime-validation.html`

Update if appropriate:

- `TODO.md`
- `docs/functional-readiness-checklist.md`
- `docs/infrastructure-mvp-closure.md`
- `docs/goals-plan.md`
- `docs/codex-goals/GOALS_INDEX.md`

## Validation to Run

```bash
PATH=.venv/bin:$PATH PYTHONPATH=src python -m unittest discover
PATH=.venv/bin:$PATH scripts/test.sh quick
PATH=.venv/bin:$PATH scripts/lint.sh
git diff --check | cat
source tools/ai-git-workflow-tools/scripts/load-agw.sh
agw_review_output --run
```

Do not run QA validation.

## Success Criteria

- Goal 014 source-of-truth file exists.
- Hebrew stage report exists.
- TODO.md records Goal 014 as complete.
- Readiness and closure documentation record the local Dev runtime validation
  without overclaiming.
- Documentation distinguishes validated clean local disposable runtime from
  unvalidated repeated idempotent install, QA worktree, and portability.
- No functional DB implementation is added.
- No secrets are added.
- Existing tests pass.
- `agw_review_output --run` passes.

## Commit Suggestion

```text
Record local Oracle lab runtime validation
```
