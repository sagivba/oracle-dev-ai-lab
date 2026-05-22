# Purpose

This directory is the governed home for future task files derived from the
release-management specification.

Goal 004 created the placeholder directory. Goal 013 adds the readiness rule:
real functional task implementation under this directory is blocked until
`docs/functional-readiness-checklist.md` is satisfied.

## Readiness Requirement

Before adding task files that create real release-management database objects,
the repository must pass the functional readiness checklist. That checklist
requires Infrastructure MVP completion, repository tests, clean lab install,
DB smoke tests, review without `BLOCKER` findings, release packaging evidence,
strict `AGENTS.md`, approved charter, approved testing strategy, and future
utPLSQL structure.

## Future Task Sequence

The first functional iteration must be a separate later goal. Future task files
must follow this sequence:

1. Create release-management tables.
2. Add constraints and indexes.
3. Add seed data.
4. Add SQL tests.
5. Add PL/SQL package spec/body only when needed.
6. Add utPLSQL tests for PL/SQL logic.
7. Run review.
8. Package release.

## Goal 013 Boundary

Goal 013 does not add functional DB objects, SQL business tests, PL/SQL packages,
views, triggers, deployment logic, REST, ORDS, APEX, or UI.

Traceability: Goal 004 - Create Oracle Lab Repository Structure; Goal 013 - Add
Functional Iteration Readiness Checklist.
