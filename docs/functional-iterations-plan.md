# Purpose

This document records the Goal 012 high-level plan for future functional
iterations after the Infrastructure MVP skeleton closure.

It is planning documentation only. It does not create database objects, runtime
behavior, deployment logic, or release-management business implementation.

## Context

The Infrastructure MVP skeleton is closed and documented in
`docs/infrastructure-mvp-closure.md`. The repository now has isolated lab
infrastructure, controlled install scripts, smoke tests, review workflow, and a
release packaging skeleton.

Goal 012 starts the functional planning track by clarifying the future fictional
release-management use case without implementing it.

## Future Use Case

The future use case is a fictional, non-sensitive release-management system.
Future iterations may refine requirements for request tracking, release items,
environment metadata, statuses, approvals, and execution logging.

## Candidate Future Entities

These names are planning candidates only:

- `RELEASE_REQUESTS`
- `RELEASE_ITEMS`
- `RELEASE_ENVIRONMENTS`
- `RELEASE_STATUSES`
- `RELEASE_APPROVALS`
- `RELEASE_EXECUTION_LOG`

Goal 012 does not create these tables or any related SQL files.

## Suggested Iteration Order

1. Refine functional requirements and acceptance criteria in the semantic spec.
2. Define traceability from requirements to future DB objects and tests.
3. Add a minimal data model only in a later approved goal.
4. Add constraints, indexes, and seed/reference data only after table scope is
   approved.
5. Add PL/SQL contracts only after the data model and review criteria are clear.
6. Extend tests, review, and packaging evidence alongside each functional slice.

## Required Boundaries for Future Work

Future functional iterations must:

- keep GitHub/repository state as the source of truth;
- represent every DB change as a versioned SQL file;
- run DB changes only through official repository scripts;
- keep secrets and real connection strings out of Git;
- use local lab infrastructure only;
- avoid organizational DB access;
- avoid ad-hoc DDL and DML;
- use `unittest` for Python tests;
- use utPLSQL for future business PL/SQL unit tests when PL/SQL exists.

## Out of Scope for Goal 012

- functional release-management DB tables;
- PL/SQL packages, package bodies, procedures, or functions;
- views, triggers, constraints, indexes, or business seed data;
- deployment logic;
- runtime Oracle validation claims;
- REST, ORDS, APEX, or UI;
- Oracle 19c compatibility claims.

## Recommended Next Step

Plan the first functional iteration as a separate goal. Do not implement
functional DB objects until that goal explicitly defines the approved scope,
traceability, tests, and review criteria.
