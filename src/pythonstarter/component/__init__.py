"""Component package for pythonstarter.

This module re-exports the configuration helpers provided by
``config_manager`` so callers can import them directly from
``pythonstarter.component`` (for example: ``from pythonstarter.component import settings``).
"""

from .config_manager import settings
from .log_manager import logger

__all__ = ["logger", "settings"]
