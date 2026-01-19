"""log.py"""

from loguru import logger

from pythonstarter.component import settings


def _configure_logger() -> None:
    log_level = (settings.log_level or "INFO").upper()

    if getattr(settings.log, "to_file", False):
        logger.add(
            settings.log.output,
            level=log_level,
            rotation="10 MB",
            retention="7 days",
            encoding="utf-8",
            enqueue=True,
        )
        logger.add(
            settings.log.error,
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
