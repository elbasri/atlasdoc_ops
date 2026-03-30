# src/logging/structured_logger.py
import logging
from typing import Any, Dict

class StructuredLogger:
    """
    A structured logger that formats log messages as JSON.
    """
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log(self, level: str, message: str, extra: Dict[str, Any] = None):
        """
        Logs a message with structured data.

        :param level: The logging level (e.g., 'info', 'error').
        :param message: The log message.
        :param extra: Additional structured data to include in the log.
        """
        if extra:
            self.logger.log(getattr(logging, level.upper()), message, extra=extra)
        else:
            self.logger.log(getattr(logging, level.upper()), message)
