# Docker Lab Design

## Purpose

This document defines the local Oracle AI Database 26ai Free Docker lab skeleton
for `oracle-dev-ai-lab`.

The technical baseline is Sagiv Barhoom's Oracle 26ai Docker setup post:

```text
https://www.sagiv-barhoom.me/oracle/2026/04/05/oracle_26ai_docker_setup.html
```

The project adapts the post's Docker approach while replacing generic names and
example passwords with project-mandated names and placeholder-only configuration.

## Baseline Adapted from the Post

Use:

- image: `container-registry.oracle.com/database/free:latest`
- Oracle data directory mount: `/opt/oracle/oradata`
- listener port mapping: `1521:1521`
- service/PDB: `FREEPDB1`
- readiness log marker: `DATABASE IS READY TO USE!`
- Bash-oriented scripts suitable for WSL/Linux-style execution

Do not copy the blog's generic runtime names or example password.

## Project Runtime Names

Use these names exactly:

```text
Container: oracle-dev-ai-lab-db
Volume:    oracle-dev-ai-lab-u01
Network:   oracle-dev-ai-lab-net
PDB:       FREEPDB1
```

## Security

No real password is committed.

The tracked `.env.example` contains only placeholders:

```text
ORACLE_PWD=change_me_in_local_env
```

Before starting the lab, create a local untracked `.env` and replace the
placeholder value:

```bash
cp .env.example .env
```

Do not commit `.env`.

## Oracle Container Registry

Before pulling or starting the image, accept Oracle Container Registry terms for
the database/free image and log in locally:

```bash
docker login container-registry.oracle.com
```

This uses an Oracle account for registry access. It is not the database password
and must not be committed.

## Compose Service

The `db` service in `docker-compose.yml` uses:

```text
image: container-registry.oracle.com/database/free:latest
container_name: oracle-dev-ai-lab-db
ports:
  - 1521:1521
volumes:
  oracle-dev-ai-lab-u01:/opt/oracle/oradata
networks:
  oracle-dev-ai-lab-net
```

## Lab Scripts

The Docker lab scripts are:

```text
scripts/lab-up.sh
scripts/lab-down.sh
scripts/lab-reset.sh
scripts/lab-backup.sh
scripts/lab-restore.sh
```

`scripts/lab-up.sh` starts only the Oracle `db` service and prints readiness
guidance.

`scripts/lab-down.sh` stops the container without deleting the persisted volume.

`scripts/lab-reset.sh --yes` removes the disposable container, volume, and network.

`scripts/lab-backup.sh` saves useful container metadata, volume metadata, image
name, runtime notes, and a compressed archive of the Oracle data volume. It stops
the container before archiving volume data and restarts it when it had been
running.

`scripts/lab-restore.sh <backup_directory> [--replace]` restores the volume data
using a temporary Alpine container and then starts the Oracle lab container using
Docker Compose.

## Readiness

Startup can take several minutes. Follow logs with:

```bash
docker logs -f oracle-dev-ai-lab-db
```

The lab should be treated as ready only after the logs contain:

```text
DATABASE IS READY TO USE!
```

Check the marker with:

```bash
docker logs oracle-dev-ai-lab-db | grep 'DATABASE IS READY TO USE!'
```

## Connection Baseline

When running locally:

```text
Host: localhost
Port: 1521
Service/PDB: FREEPDB1
```

Do not commit real connection strings.

## Validation Status

The initial Goal 006 skeleton was checked statically without starting Docker.
Later Goal 014 / [PR #22](https://github.com/sagivba/oracle-dev-ai-lab/pull/22)
recorded local Dev runtime validation on 2026-05-22 at `v0.1.0`, including startup,
readiness, clean install after reset, and SQL smoke tests. See
[the closure record](infrastructure-mvp-closure.md) for the evidence boundaries.

This documentation reconciliation did not start Docker or validate Oracle.
Backup/restore, repeated install on an installed lab, and portability to another
developer are not established by the Goal 014 record. A new environment must
verify readiness and run the managed install and smoke tests. The default image
tag is `latest`; a later pull may select a different image from the historical
validation baseline.
