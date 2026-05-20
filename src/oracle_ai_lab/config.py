import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    project_name: str = "DEVELOPMENT in Oracle using AI Lab-template"

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            project_name=os.getenv("PROJECT_NAME", "DEVELOPMENT in Oracle using AI Lab-template"),
        )
