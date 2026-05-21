# Purpose

This directory is reserved for generated release package outputs for the Oracle
AI Lab repository workflow.

Goal 011 adds a skeleton-only packaging workflow. The workflow creates or
refreshes `db/dist/release_001/` from managed, versioned repository files only.
It does not connect to Oracle, does not run Docker, does not access
organizational databases, and does not execute ad-hoc DDL or DML.

Release package output must not include local `.env` or `.env.*` files, secrets,
tokens, private keys, certificates, or unmanaged database changes. Goal 011
keeps the package explicitly not approved for deployment because the workflow is
only a deterministic contract skeleton.
