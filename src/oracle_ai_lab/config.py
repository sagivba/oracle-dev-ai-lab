import os
from dataclasses import dataclass

DEFAULT_PROJECT_NAME = "DEVELOPMENT in Oracle using AI Lab"


@dataclass(frozen=True)
class AppConfig:
    """Configuration for the retained Python starter app."""

    project_name: str = DEFAULT_PROJECT_NAME

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            project_name=os.getenv("PROJECT_NAME", DEFAULT_PROJECT_NAME),
        )
