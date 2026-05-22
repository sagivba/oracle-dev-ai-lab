# Goals Index

Run these goals in order. Do not skip a goal unless its output already exists and passes the stated success criteria.

| Order | File | Purpose |
|---:|---|---|
| 000 | `goal-000-operating-rules.md` | Establish how Codex must execute all later goals. |
| 001 | `goal-001-template-alignment.md` | Align the Python template identity with `oracle-dev-ai-lab`. |
| 002 | `goal-002-project-docs.md` | Create project charter, safety rules, decision log, and scope docs. |
| 003 | `goal-003-agents-md.md` | Create/replace strict `AGENTS.md` rules for Codex. |
| 004 | `goal-004-repository-structure.md` | Add Oracle lab folders without breaking the Python template. |
| 005 | `goal-005-testing-strategy.md` | Add testing strategy and baseline `unittest` contract tests. |
| 006 | `goal-006-docker-lab-skeleton.md` | Add Oracle Docker 26ai Free skeleton and lab scripts. |
| 007 | `goal-007-install-workflow.md` | Add DB installation workflow and lab user SQL skeletons. |
| 008 | `goal-008-db-smoke-tests.md` | Add smoke object and SQL smoke tests. |
| 009 | `goal-009-spec-pipeline-skeleton.md` | Add spec extraction/validation/generation skeleton. |
| 010 | `goal-010-review-workflow.md` | Add review workflow and report structure. |
| 011 | `goal-011-packaging-workflow.md` | Add release packaging workflow and manifest structure. |
| 012 | `goal-012-functional-spec-placeholder.md` | Add release-management functional spec placeholder only. |
| 013 | `goal-013-functional-iteration-readiness.md` | Add readiness checklist before real functional development. |
| 014 | `goal-014-record-local-oracle-lab-runtime-validation.md` | Record local Dev Oracle runtime validation evidence. |

Commit recommendation:

```text
One goal = one commit.
```

Branch recommendation:

```text
codex-cli/goal-xxx-short-name
```
