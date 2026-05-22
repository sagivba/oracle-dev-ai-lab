# Purpose

This document defines the Goal 013 readiness gate that must pass before any real
functional database development starts in `oracle-dev-ai-lab`. It is governance
documentation only; it does not create database objects, change runtime behavior,
or approve the first functional implementation goal.

## Readiness Gate

Real functional release-management database development is blocked until every
item in this checklist is satisfied and evidenced in the repository or in an
explicit validation record.

| Gate | Required evidence before functional work |
| --- | --- |
| Infrastructure MVP complete | `docs/infrastructure-mvp-closure.md` records that the Infrastructure MVP skeleton is complete. |
| Repository quick checks pass | `scripts/test.sh quick` passes. |
| Clean lab install passes | `scripts/install-db.sh` passes on a clean local lab database. |
| DB smoke tests pass | `scripts/run-db-tests.sh smoke` passes against the local lab database. |
| Static review has no blockers | `scripts/review-db-code.sh` produces no `BLOCKER` findings. |
| Release package is complete | `scripts/package-release.sh` creates a package with manifest, install files, rollback files, reports, and deployment notes. |
| Strict agent rules exist | `AGENTS.md` is complete and strict for Oracle AI Lab work. |
| Project charter approved | `docs/project-charter.md` is approved as the project governance baseline. |
| Unit testing strategy approved | `docs/testing-strategy.md` is approved and keeps Python tests on `unittest`. |
| Future PL/SQL test structure exists | `db/tests/utplsql/` exists for future business PL/SQL tests. |

## Current Validation Evidence

Goal 014 records local Dev runtime validation after `v0.1.0`. That evidence shows
the readiness gates for local clean lab install, SQL smoke tests, review, and
package workflow passed in the Dev repository only.

The validation scope is intentionally narrow:

- validated: clean install on a disposable local lab runtime after
  `scripts/lab-reset.sh --yes`;
- not validated: repeated idempotent install on an already-installed lab;
- not validated: QA worktree behavior;
- not validated: portability or onboarding for other developers.

Functional work remains blocked unless the current branch also has fresh task
scope, traceability, and validation requirements for the first functional goal.

## Blocking Rule

If any readiness item is missing, failing, stale, or not evidenced, functional
DB development must not start. The next task must repair or revalidate the
missing readiness item before creating real release-management DB objects.

Goal 013 does not implement functional DB objects. It does not create
release-management tables, constraints, indexes, seed data, SQL business tests,
PL/SQL packages, views, triggers, deployment logic, REST, ORDS, APEX, or UI.

## First Functional Iteration Sequence

The first functional iteration must be a separate later goal. When that goal is
approved, it must follow this sequence:

1. Create release-management tables.
2. Add constraints and indexes.
3. Add seed data.
4. Add SQL tests.
5. Add PL/SQL package spec/body only when needed.
6. Add utPLSQL tests for PL/SQL logic.
7. Run review.
8. Package release.

## Required Evidence for the Separate Functional Goal

The first functional goal must explicitly name the requirement IDs, task IDs, or
decision IDs it implements. It must keep every database change in versioned SQL
files and execute those changes only through official repository scripts.

Traceability: Goal 013 - Add Functional Iteration Readiness Checklist; DEC-003;
DEC-010; DEC-011; DEC-012; DEC-013; DEC-014; DEC-018; DEC-019.
