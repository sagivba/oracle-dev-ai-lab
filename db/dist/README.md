# Purpose

This directory is reserved for generated release package outputs for the Oracle
AI Lab repository workflow.

The packaging workflow creates or refreshes `db/dist/release_001/` from managed,
versioned repository files only. It does not connect to Oracle, does not run
Docker, does not access organizational databases, and does not execute ad-hoc
DDL or DML.

Release package output must not include local `.env` or `.env.*` files, secrets,
tokens, private keys, certificates, or unmanaged database changes. The current
package remains explicitly not approved for deployment because it is a
deterministic Infrastructure MVP package contract, not a functional release.

Empty package object-type folders may contain deterministic `README.md` marker
files so the folder contract is represented in Git. These markers document that
no managed SQL files exist for that object type and are not database source
files.
