# /goal 010 - Add Review Workflow Skeleton

## Goal

Add a structured review workflow for DB code, repository contract, safety rules, and traceability.

## Prompt to use with Codex

```text
/goal
Add the review workflow skeleton for oracle-dev-ai-lab.

Create or update:
- scripts/review-db-code.sh
- db/review/review-report.md
- docs/review-workflow.md
- tests/test_review_contract.py or equivalent unittest location

Review report must include sections:
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

Severity levels:
- BLOCKER
- MAJOR
- MINOR
- QUESTION

Rules:
- A release package is not approved if any BLOCKER exists.
- Review workflow must not connect to organizational databases.
- SELECT diagnostics are allowed only against the local lab container.
- Review must check that DB objects are represented as versioned SQL files.

Success criteria:
- review-db-code.sh exists and is safe.
- review-report.md template exists.
- unittest contract checks the report template structure.
- Existing tests pass.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add DB review workflow skeleton
```
