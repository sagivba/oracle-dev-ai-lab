# Purpose

This document explains the Goal 009 specification pipeline skeleton for
`oracle-dev-ai-lab`.

## Scope

Goal 009 adds a local, deterministic skeleton for turning a semantic HTML
specification into traceable placeholder artifacts. It does not implement
functional release-management behavior and does not generate Oracle business
objects.

## Input

The pipeline starts from:

```text
specs/001-release-management/spec.html
```

The file is a semantic HTML skeleton with stable requirement and acceptance
criteria identifiers such as `REQ-001` and `AC-001`. The `plsql-api` section is
present but optional for the Infrastructure MVP.

## Derived Outputs

The skeleton derives:

```text
specs/001-release-management/spec.json
specs/001-release-management/TODO.md
specs/001-release-management/traceability-matrix.md
specs/001-release-management/tasks/T001-spec-pipeline-placeholder.md
```

These outputs are traceability placeholders only. They are intended to support
later review and packaging workflows by making requirement IDs and acceptance
criteria machine-readable.

## Tools

Run the tools from the repository root:

```bash
python tools/extract_spec.py
python tools/validate_spec.py
python tools/generate_todo.py
python tools/generate_tasks.py
```

Each tool supports `--help`:

```bash
python tools/extract_spec.py --help
python tools/validate_spec.py --help
python tools/generate_todo.py --help
python tools/generate_tasks.py --help
```

Current check modes:

```bash
python tools/extract_spec.py --check
python tools/generate_todo.py --check
python tools/generate_tasks.py --check
```

## Current Skeleton Status

- `tools/extract_spec.py` reads semantic HTML and writes deterministic JSON.
- `tools/validate_spec.py` validates required sections, stable IDs, and JSON
  synchronization.
- `tools/generate_todo.py` writes a traceable placeholder TODO from `spec.json`.
- `tools/generate_tasks.py` writes a placeholder task and traceability matrix.
- `tests/test_spec_pipeline.py` covers repository-only behavior with `unittest`.

## Intentionally Not Implemented

Goal 009 does not implement:

- real release-management business logic;
- release-management database tables;
- generated functional PL/SQL objects;
- review workflow files from Goal 010;
- packaging workflow files from Goal 011;
- runtime Oracle validation;
- Docker startup;
- external service access.

## Safety Rules

The pipeline is repository-only. It does not connect to Oracle, Docker, network
services, organizational systems, or any database. It uses only the Python
standard library and does not introduce `pytest`.

## Relationship to Later Goals

Goal 009 provides structured inputs for later review and packaging workflows.
Those workflows remain out of scope until their own goals are executed.
