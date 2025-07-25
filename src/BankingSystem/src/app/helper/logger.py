# app/logger.py
import logging
from logging import getLogger, StreamHandler, FileHandler, Formatter

def get_logger(log_file: str):
    logger = getLogger(log_file)  # use file name as logger name
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = FileHandler(log_file)
        file_handler.setFormatter(Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            "%Y-%m-%d %H:%M:%S"
        ))

        console_handler = StreamHandler()
        console_handler.setFormatter(Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            "%Y-%m-%d %H:%M:%S"
        ))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
