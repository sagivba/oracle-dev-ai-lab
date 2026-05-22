# Purpose

This directory stores repository-local tooling for specification processing,
validation, review support, packaging, and other Oracle AI Lab workflows.

Tools in this directory must stay deterministic, local to the repository, and
safe by default. They must not embed secrets, contact organizational databases,
or perform ad-hoc DDL/DML outside official workflows.
