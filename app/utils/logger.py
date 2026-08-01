import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Log directory
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Log file
LOG_FILE = LOG_DIR / "trade-assistant.log"


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger.

    The logger writes to:
        - Console
        - logs/trade-assistant.log

    Log files are automatically rotated.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    #
    # Console
    #
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    #
    # Rotating log file
    #
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=10,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger