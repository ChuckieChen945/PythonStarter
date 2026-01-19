from __future__ import annotations

from os import getenv

from dotenv import load_dotenv
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

from pythonstarter.common.path import CONFIG_ROOT, SECRETS_ROOT

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
    output: str | None = None
    error: str | None = None


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
