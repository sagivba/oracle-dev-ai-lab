# Purpose

This directory stores SQL-based database tests for the local Oracle lab.

These tests are executed by `scripts/run-db-tests.sh` against the disposable
local lab container. They should validate state and avoid ad-hoc schema changes.
