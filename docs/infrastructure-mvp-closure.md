# Purpose

This document records the T012 documentation-only closure decision for the
Infrastructure MVP skeleton in `oracle-dev-ai-lab`. It summarizes completed
governance, repository, runtime, review, and packaging evidence without starting
Goal 012 or adding functional release-management implementation.

## Baseline Commit

- Baseline after merged PR #18: `6f0718ebe1d4259db860a4bc0911134a808fdc6b`
- Source of truth: GitHub/main at the merged Goal 011 baseline.
- Runtime QA evidence: provided from the aligned QA worktree after Goal 011.

## Completed Goals and Supporting PRs

- Goals 000-011 are complete and merged.
- PR #13-#16 completed the post-Goal-010 runtime infrastructure fixes.
- PR #17 added the Goal 011 source-of-truth file.
- PR #18 implemented the Goal 011 release packaging workflow skeleton.

## What the Infrastructure MVP Now Proves

The Infrastructure MVP skeleton now proves the repository can support:

- an isolated Docker Oracle lab using the fixed project resource names;
- a controlled install workflow through managed repository scripts;
- local lab schemas and users created from versioned SQL files;
- managed, versioned SQL source under `db/src/`;
- SQL smoke tests for connectivity, object inventory, and invalid objects;
- a repository-safe review workflow;
- a deterministic release packaging skeleton;
- static QA through the Python unittest and lint entry points;
- runtime QA after Goal 011 from the QA worktree.

## Intentionally Out of Scope

The closure decision does not include:

- Goal 012;
- functional release-management DB objects;
- business workflow logic;
- organizational DB access;
- secrets or real connection strings;
- ad-hoc DDL or DML;
- APEX, ORDS, REST, or UI work;
- Oracle 19c compatibility claims.

## QA Results Summary

Runtime QA after Goal 011 passed from the QA worktree:

| Check | Result |
| --- | --- |
| Oracle readiness | PASS |
| `scripts/install-db.sh` | PASS |
| `scripts/run-db-tests.sh` | PASS |
| `db/tests/sql/001_db_connectivity.sql` | PASS |
| `db/tests/sql/002_object_inventory.sql` | PASS |
| `db/tests/sql/003_no_invalid_objects.sql` | PASS |
| `scripts/review-db-code.sh` | PASS |
| `scripts/package-release.sh` | PASS |
| `PATH=.venv/bin:$PATH scripts/test.sh quick` | PASS, 51 tests |
| `PATH=.venv/bin:$PATH scripts/lint.sh` | PASS |
| `agw_review_output --run` | PASS |
| QA worktree clean | PASS |

## Environmental QA Notes

Runtime QA initially failed for environmental reasons only:

- `scripts/lab-reset.sh` was first run without `--yes`, so the old DB state
  remained and `LAB_SMOKE_TEST` already existed.
- The QA `.env` later had a duplicate or placeholder `ORACLE_PWD`.

After correcting the QA environment, the install workflow and SQL smoke tests
passed. These initial failures are not recorded as code defects.

## Decision

The Infrastructure MVP skeleton is complete.

This decision closes the Infrastructure MVP skeleton only. It does not approve
functional release-management development inside this task, and it does not
change any runtime behavior.

## Local Dev Runtime Validation After v0.1.0

Goal 014 records manual local Oracle Lab runtime validation performed in the Dev
repository after tag `v0.1.0` at commit
`1c6b46797766656e5db537047d8e91b61853e71d`.

The validation was performed only in:

```text
/home/sagivba-adm/src/oracle-dev-ai-lab
```

The QA worktree was not touched.

Successful validation covered:

- AGW status on `main` at `1c6b467` with a clean working tree;
- local `.env` created from `.env.example` with `ORACLE_PWD` set locally;
- `scripts/lab-up.sh` starting `oracle-dev-ai-lab-db`;
- `scripts/lab-reset.sh --yes` removing the disposable container, volume, and
  network before the successful install validation;
- Oracle readiness marker `DATABASE IS READY TO USE!`;
- `scripts/install-db.sh` completing the controlled install on the clean local
  lab runtime;
- `scripts/run-db-tests.sh smoke` passing connectivity, object inventory, and
  invalid-object checks;
- `scripts/review-db-code.sh` passing the review skeleton checks;
- `scripts/package-release.sh` writing `db/dist/release_001`;
- `agw_review_output --run` passing with no repository changes.

The successful install validation was a clean install after `lab-reset`. Repeated
idempotent install on an already-installed lab was not validated and must not be
claimed.

The smoke connectivity check observed `CURRENT_SCHEMA=SYS`; this is recorded as
an observation, not as a failure.

No organizational database access was used. No secrets were committed. The local
`.env` file and password remain local and are not repository evidence.

## v0.1.1 Intended Meaning

After Goal 014 is merged, the project can create tag `v0.1.1` with this intended
meaning:

```text
Infrastructure MVP + local Oracle runtime validation baseline.
Ready to start Codex Oracle development capability study.
```

This tag meaning does not claim QA worktree validation, repeated idempotent
install behavior, portability for other developers, Oracle 19c compatibility, or
functional release-management implementation.

## Recommended Next Step

Merge Goal 014, then create tag `v0.1.1` as the local Oracle runtime validation
baseline before starting the Codex Oracle development capability study.
