-- Purpose: Official Goal 007/008 database install entry point for the Oracle AI Lab.
-- This SQL*Plus/sqlcl-compatible file defines the managed install order for the
-- local lab only. It installs infrastructure objects only and stores no secrets.

set echo off
set feedback on
set heading on
set verify off
whenever sqlerror exit sql.sqlcode

prompt Oracle AI Lab controlled install entry point
prompt Goal 008: controlled install workflow with infrastructure smoke object

-- Password values are supplied by scripts/install-db.sh from local environment
-- variables. The values must never be committed to Git.
define AI_APP_OWNER_PWD = "&1"
define AI_APP_RUNTIME_PWD = "&2"
define AI_APP_READONLY_PWD = "&3"
define AI_REVIEWER_PWD = "&4"

prompt Running managed install file: 00_create_lab_users.sql
@@00_create_lab_users.sql

prompt Running managed install file: 01_create_schema.sql
@@01_create_schema.sql

prompt Running managed source file: ../src/tables/lab_smoke_test.sql
@@../src/tables/lab_smoke_test.sql

prompt Oracle AI Lab controlled install completed.
