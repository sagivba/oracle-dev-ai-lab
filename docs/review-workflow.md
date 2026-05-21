# Purpose

This document defines the Goal 010 review workflow skeleton for
`oracle-dev-ai-lab`.

## Current Skeleton Status

Goal 010 adds a repository-only review workflow skeleton. The default review is
static and does not require Docker, Oracle, network access, secrets, or external
services.

The review entry point is:

```text
scripts/review-db-code.sh
```

The review report template is:

```text
db/review/review-report.md
```

## Required Report Sections

The report must include:

- Spec coverage
- Infrastructure decisions coverage
- Object inventory
- Data model review
- PL/SQL review
- Security review
- Deployment review
- Risks
- Required fixes
- Optional improvements
- Approval status

## Severity Levels

- BLOCKER
- MAJOR
- MINOR
- QUESTION

## Approval Rule

A release package is not approved if any BLOCKER exists.

Goal 010 does not approve release packaging. Packaging belongs to Goal 011.

## Static Checks

The default script checks that:

- the review report template exists;
- required report sections exist;
- required severity levels exist;
- the BLOCKER approval rule is present;
- key governance and workflow files exist;
- DB source files under `db/src/` are versioned `.sql` files or README
  placeholders;
- review documentation and scripts avoid obvious forbidden DB target references;
- the review workflow is usable from the repository root.

## Safety Boundaries

The review workflow:

- must not connect to organizational databases;
- must not require Docker or Oracle for the default skeleton review;
- must not use secrets or real connection strings;
- must not execute ad-hoc DDL or DML;
- must preserve Git/repository state as the source of truth;
- must use official managed repository files only.

## Optional Local DB Diagnostics

Future review iterations may add SELECT-only diagnostics against the local
container named `oracle-dev-ai-lab-db`. Those diagnostics must be explicit,
local-only, safe by default, and must not connect to organizational databases.

Runtime Oracle diagnostics are not implemented or claimed in Goal 010.

## Intentionally Not Checked Yet

Goal 010 does not implement:

- full Oracle runtime object inventory;
- DB grants review through live metadata;
- functional data model review;
- functional PL/SQL review;
- release package validation;
- packaging workflow files;
- functional release-management DB objects.

## Relationship to Goal 011

Goal 010 creates the review workflow skeleton and report template that Goal 011
can later include in release packaging. It does not create package output,
package manifests, deployment notes, or release artifacts.
