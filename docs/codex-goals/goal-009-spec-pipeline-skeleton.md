# /goal 009 - Add Specification Pipeline Skeleton

## Goal

Add skeleton tooling and docs for the HTML spec to JSON/TODO/tasks pipeline.

## Prompt to use with Codex

```text
/goal
Add the specification pipeline skeleton for oracle-dev-ai-lab.

Create or update:
- specs/001-release-management/spec.html
- specs/001-release-management/spec.json placeholder or generated sample
- specs/001-release-management/TODO.md placeholder
- specs/001-release-management/traceability-matrix.md placeholder
- tools/extract_spec.py
- tools/validate_spec.py
- tools/generate_todo.py
- tools/generate_tasks.py
- tests/test_spec_pipeline.py or equivalent unittest location
- docs/spec-pipeline.md

Rules:
- This goal creates skeleton tooling only.
- Do not implement full business logic generation yet.
- spec.html must use stable requirement ids, e.g. REQ-001, AC-001.
- PL/SQL API section must be optional for Infrastructure MVP.
- Tools must be deterministic and safe.
- Python tests must use unittest.

Success criteria:
- Spec skeleton exists.
- Tools can run with --help or produce deterministic placeholder output.
- unittest tests validate required sections or placeholders.
- No Oracle DB is required for this goal.

Run:
python -m unittest discover
scripts/test.sh quick
```

## Commit suggestion

```text
Add specification pipeline skeleton
```
