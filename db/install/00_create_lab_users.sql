-- Purpose: Goal 007 skeleton for controlled Oracle AI Lab user/schema creation.
-- This file documents the required local lab users and reserves the managed SQL
-- location for later runtime-validated DDL. It does not store real passwords.

set echo off
set feedback on
set heading on
set verify off

prompt Preparing Oracle AI Lab user/schema creation skeleton.

-- Intended local lab users/schemas:
-- AI_APP_OWNER    - future owner of lab tables, views, packages, and related objects.
-- AI_APP_RUNTIME  - future runtime account with the minimum execution privileges.
-- AI_APP_READONLY - future read-only account for tests and reports.
-- AI_REVIEWER     - future metadata/review account with narrow dictionary access.

-- Password substitution variables are defined by install.sql and populated by
-- scripts/install-db.sh from local environment variables:
-- &&AI_APP_OWNER_PWD
-- &&AI_APP_RUNTIME_PWD
-- &&AI_APP_READONLY_PWD
-- &&AI_REVIEWER_PWD

-- Goal 007 intentionally avoids executable CREATE USER and GRANT statements until
-- runtime validation is authorized against the disposable local lab container.
-- The later implementation must keep all DDL in this managed file and run it only
-- through db/install/install.sql and scripts/install-db.sh.

-- TODO(G007/G008+): Add validated CREATE USER or ALTER USER statements for:
--   AI_APP_OWNER
--   AI_APP_RUNTIME
--   AI_APP_READONLY
--   AI_REVIEWER

-- TODO(G007/G008+): Add the smallest validated privilege set. Broad grants such
-- as DBA, RESOURCE, unlimited system privileges, or organizational DB access are
-- intentionally excluded from this skeleton.

-- Conservative future baseline to validate before enabling:
--   GRANT CREATE SESSION TO AI_APP_OWNER;
--   GRANT CREATE SESSION TO AI_APP_RUNTIME;
--   GRANT CREATE SESSION TO AI_APP_READONLY;
--   GRANT CREATE SESSION TO AI_REVIEWER;
-- Object privileges should be granted only after managed objects exist.

prompt User/schema creation remains a safe skeleton in Goal 007.
