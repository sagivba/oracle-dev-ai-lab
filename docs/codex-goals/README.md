# Codex Goals - DEVELOPMENT in Oracle using AI Lab

This folder contains staged `/goal` files for preparing and building the `oracle-dev-ai-lab` repository.

The folder is intended to be copied into:

```text
docs/codex-goals/
```

Recommended flow:

1. Create the new repository from `sagivba/DEVELOPMENT in Oracle using AI Lab`.
2. Clone it locally.
3. Copy this folder into `docs/codex-goals/`.
4. Run the goals in order.
5. After each goal, review `git diff`, run the requested tests, and commit only a small coherent change.

Mandatory project facts:

```text
Project display name: DEVELOPMENT in Oracle using AI Lab
Repository name:      oracle-dev-ai-lab
Docker container:     oracle-dev-ai-lab-db
Docker volume:        oracle-dev-ai-lab-u01
Docker network:       oracle-dev-ai-lab-net
Oracle PDB:           FREEPDB1
Oracle version:       Oracle AI Database 26ai Free
```

Core rule:

```text
No database change is valid unless it exists as a versioned SQL file and can be installed on a clean lab database by the official scripts.
```

Testing model:

```text
Python unittest: repository contracts, tools, spec pipeline, packaging, optional DB smoke orchestration.
SQL tests: DB smoke, installation verification, metadata checks, grants, invalid objects.
utPLSQL: future PL/SQL business unit tests during functional iterations.
```
