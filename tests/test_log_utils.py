import sys
import os
from pathlib import Path
import logging as std_logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_utils import log_utils

LOG_FILE_PATH = Path("logs/dev.log")


def reset_logging():
    for handler in std_logging.root.handlers[:]:
        std_logging.root.removeHandler(handler)
    if LOG_FILE_PATH.exists():
        LOG_FILE_PATH.unlink()


def test_setup_default_logging_creates_log_file_and_writes_message():
    reset_logging()
    log_utils.setup_default_logging()
    logger = std_logging.getLogger("test_logger")
    logger.info("This is a test log message")

    assert LOG_FILE_PATH.exists()

    with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        assert "This is a test log message" in content


def test_get_logger_returns_configured_logger():
    reset_logging()
    logger = log_utils.get_logger("my_test_logger")
    logger.warning("Logger test message")

    assert LOG_FILE_PATH.exists()
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Logger test message" in content
