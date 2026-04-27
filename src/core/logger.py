"""
Application logging configuration.
"""

import logging
import sys

from src.core.config import settings


def setup_logger() -> logging.Logger:
    """
    Configure root logger.

    Returns:
        logging.Logger: configured logger
    """
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    return logging.getLogger(settings.app_name)


logger = setup_logger()