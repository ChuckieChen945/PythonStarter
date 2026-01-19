"""log.py"""

from loguru import logger

# Import settings directly from the local module to avoid a package-level
# circular import when `pythonstarter.component` is imported.
from .config_manager import settings


def _configure_logger() -> None:
    log_level = (settings.log_level or "INFO").upper()

    log_cfg = getattr(settings, "log", None)
    # Only configure file logging when configuration and paths are present
    if log_cfg and getattr(log_cfg, "to_file", False):
        if getattr(log_cfg, "info_path", None):
            logger.add(
                log_cfg.info_path,
                level=log_level,
                rotation="10 MB",
                retention="7 days",
                encoding="utf-8",
                enqueue=True,
            )
        if getattr(log_cfg, "error_path", None):
            logger.add(
                log_cfg.error_path,
                level="WARNING",
                rotation="10 MB",
                retention="30 days",
                encoding="utf-8",
                enqueue=True,
            )


_configure_logger()

if __name__ == "__main__":
    logger.info("Log manager configured.")
    logger.debug(f"Log settings: {settings.log}")
