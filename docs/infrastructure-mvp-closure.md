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

## Recommended Next Step

Plan Goal 012 as the next separate task. Do not implement Goal 012 as part of
T012.
