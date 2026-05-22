# Purpose

This document records the Goal 013 transition plan from Infrastructure MVP and
placeholder functional planning into readiness-gated functional iterations. It
is planning and governance documentation only; it does not add database objects,
runtime behavior, deployment logic, or functional release-management
implementation.

## Current Goal Track

Goals 000 through 011 established the Oracle AI Lab governance, repository
structure, local lab infrastructure skeleton, install workflow, smoke-test
workflow, review workflow, and release packaging workflow.

Goal 012 added a release-management functional specification placeholder. That
placeholder is a planning source only and does not authorize DB implementation.

Goal 013 adds the readiness checklist that controls when real functional work
may begin.

## Transition Rule

Functional development may start only after the readiness gate in
`docs/functional-readiness-checklist.md` is satisfied. The gate protects the
repository from starting business DB implementation before the Infrastructure
MVP evidence, safety rules, test strategy, review workflow, and packaging
workflow are complete and current.

## Planning Status After Goal 013

- Infrastructure MVP closure is documented in `docs/infrastructure-mvp-closure.md`.
- Functional scope remains represented by the placeholder specification under
  `specs/001-release-management/`.
- Real functional DB implementation remains blocked until a later goal explicitly
  starts the first functional iteration.
- Goal 013 itself does not implement release-management tables, constraints,
  indexes, seed data, SQL business tests, PL/SQL packages, views, triggers, or
  deployment logic.

## Required First Functional Goal

The first functional iteration must be a separate later goal. It must start from
the readiness checklist, name the requirements and acceptance criteria it
implements, and keep one focused change set.

The required implementation sequence for that later goal is:

1. Create release-management tables.
2. Add constraints and indexes.
3. Add seed data.
4. Add SQL tests.
5. Add PL/SQL package spec/body only when needed.
6. Add utPLSQL tests for PL/SQL logic.
7. Run review.
8. Package release.

## Non-Goals for Goal 013

- No functional DB objects are added.
- No Oracle runtime behavior changes.
- No install, rollback, review, packaging, Docker, or deployment behavior
  changes.
- No REST, ORDS, APEX, or UI work is started.
- No organizational database access is needed or allowed.

Traceability: Goal 013 - Add Functional Iteration Readiness Checklist; DEC-013;
DEC-014; DEC-018; DEC-019.
