import logging

from .formatters import colored_console_formatter, console_formatter, file_formatter
from .utils import supports_color


def get_logger(
    name: str,
    *,
    level=logging.INFO,
    console_level=logging.INFO,
    file_level=logging.ERROR,
    filename=".log",
    colored=None,
) -> logging.Logger:
    """
    Return a logger with console (stream) and file handlers.
    Console formatter is colored if terminal supports colors
    (or `colored == True`).
    """

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    if colored is None:
        colored = supports_color()
    _console_fmt = colored_console_formatter if colored else console_formatter
    console_handler.setFormatter(_console_fmt)

    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(file_formatter)

    logger = logging.getLogger(name=name)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
