from __future__ import annotations

from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from pydantic import field_validator
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

from pythonstarter.common.path import CONFIG_ROOT, PROJECT_ROOT, SECRETS_ROOT

# ========= .env =========
load_dotenv(CONFIG_ROOT / ".env")


# ========= YAML files =========
_env = getenv("ENV")
_yaml_files = (
    [CONFIG_ROOT / "config.yml", CONFIG_ROOT / f"config_{_env}.yml"]
    if _env
    else [CONFIG_ROOT / "config.yml"]
)


class LogConfig(BaseSettings):
    to_file: bool | None = None
    info_path: Path | None = None
    error_path: Path | None = None

    @field_validator("info_path", "error_path", mode="before")
    @classmethod
    def resolve_relative_path(cls, v: str | None) -> Path | None:
        """将相对路径解析为以 PROJECT_ROOT 为基准的绝对路径.

        Args:
            v (str | None): _description_

        Returns
        -------
            Path | None: _description_
        """
        if v is None:
            return None

        path = Path(v)

        if not path.is_absolute():
            path = PROJECT_ROOT / path

        return path.resolve()


class AppConfig(BaseSettings):
    log_level: str | None = None
    log: LogConfig | None = None

    model_config = SettingsConfigDict(
        secrets_dir=SECRETS_ROOT, yaml_file=_yaml_files, yaml_file_encoding="utf-8"
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        # TODO: deep_merge https://docs.pydantic.dev/dev/concepts/pydantic_settings/#other-settings-source
        return (YamlConfigSettingsSource(settings_cls),)


settings = AppConfig()

if __name__ == "__main__":
    print(settings.model_dump())
