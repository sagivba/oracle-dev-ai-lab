# Architecture

This project uses a simple layered structure.

## Layers

```text
routes -> services -> model
              |
            utils
```

## src/oracle_ai_lab/app.py

Creates and configures the Flask application.

## src/oracle_ai_lab/config.py

Loads configuration from environment variables.

## src/oracle_ai_lab/routes

HTTP boundary.

Route handlers should:

- parse inputs
- call services
- return responses

Route handlers should not contain business logic.

## src/oracle_ai_lab/services

Business logic.

Services should be easy to test with unittest.

## src/oracle_ai_lab/model

Domain models, data structures, and model-facing code.

## src/oracle_ai_lab/utils

Small generic utilities.

Do not put project-specific business rules here.
