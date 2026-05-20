# /goal 005 - Add Testing Strategy and Baseline unittest Contracts

## Goal

Add the testing strategy and baseline Python `unittest` tests for repository contracts.

## Prompt to use with Codex

```text
/goal
Add the testing strategy for oracle-dev-ai-lab and baseline unittest tests.

Create or update:
- docs/testing-strategy.md
- tests/test_repo_contract.py or the existing template-equivalent unittest location
- scripts/test.sh if it exists; otherwise create a safe initial script

Testing strategy must define:
1. Python unittest for repository contracts, tools, spec pipeline, packaging, and optional DB smoke orchestration.
2. SQL tests for DB smoke, install verification, invalid objects, grants, and object inventory.
3. utPLSQL for PL/SQL business unit tests in functional iterations.

Mandatory decisions:
- Python tests must use unittest.
- pytest must not be required.
- Infrastructure MVP must include at least one passing Python repository test.
- Infrastructure MVP must include SQL smoke test infrastructure.
- Functional iterations must add real Oracle unit tests using utPLSQL.

Add baseline unittest tests that check:
- docs/project-charter.md exists.
- docs/safety-rules.md exists.
- docs/decision-log.md exists.
- AGENTS.md exists.
- db/ and specs/ required folders exist.

Do not require Docker or Oracle to be running in this goal.

Success criteria:
- python -m unittest discover passes.
- scripts/test.sh quick runs Python unittest only, or explains that DB is not required yet.
- docs/testing-strategy.md clearly distinguishes unittest, SQL tests, and utPLSQL.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add testing strategy and repository contract tests
```
