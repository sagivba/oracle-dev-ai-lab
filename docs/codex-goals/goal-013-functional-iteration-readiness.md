# /goal 013 - Add Functional Iteration Readiness Checklist

## Goal

Add the readiness checklist that must pass before starting real functional development.

## Prompt to use with Codex

```text
/goal
Add a functional iteration readiness checklist for oracle-dev-ai-lab.

Create or update:
- docs/functional-readiness-checklist.md
- docs/goals-plan.md
- specs/001-release-management/tasks/README.md

The checklist must require:
- Infrastructure MVP is complete.
- scripts/test.sh quick passes.
- scripts/install-db.sh passes on a clean lab DB.
- scripts/run-db-tests.sh smoke passes.
- scripts/review-db-code.sh produces no BLOCKER findings.
- scripts/package-release.sh creates a package with manifest, install, rollback, reports, and deployment notes.
- AGENTS.md is complete and strict.
- Project charter is approved.
- Unit testing strategy is approved.
- utPLSQL structure exists for future PL/SQL tests.

The checklist must also define the first functional iteration sequence:
1. Create release-management tables.
2. Add constraints and indexes.
3. Add seed data.
4. Add SQL tests.
5. Add PL/SQL package spec/body only when needed.
6. Add utPLSQL tests for PL/SQL logic.
7. Run review.
8. Package release.

Do not implement functional DB objects in this goal.

Success criteria:
- Readiness checklist exists.
- It blocks functional work until Infrastructure MVP is complete.
- Existing tests pass.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add functional iteration readiness checklist
```
