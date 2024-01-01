import logging
from enum import Enum
from logging import LogRecord


class ANSIColor(Enum):
    GREY = "\x1b[90m"
    WHITE = "\x1b[37m"
    YELLOW = "\x1b[33m"
    RED = "\x1b[31m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

    def __str__(self) -> str:
        return self.value


class ColoredConsoleFormatter(logging.Formatter):
    def __init__(self, fmt=None, *args, **kwargs) -> None:
        self.fmt = fmt
        self.args = args
        self.kwargs = kwargs

        self.FORMATS = {
            logging.DEBUG: f"{ANSIColor.GREY}{self.fmt}{ANSIColor.RESET}",
            logging.INFO: f"{ANSIColor.WHITE}{self.fmt}{ANSIColor.RESET}",
            logging.WARNING: f"{ANSIColor.YELLOW}{self.fmt}{ANSIColor.RESET}",
            logging.ERROR: f"{ANSIColor.RED}{self.fmt}{ANSIColor.RESET}",
            logging.CRITICAL: f"{ANSIColor.BOLD_RED}{self.fmt}{ANSIColor.RESET}",
        }

        super().__init__(fmt, *args, **kwargs)

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, *self.args, **self.kwargs)
        return formatter.format(record)


class NoExceptionFormatter(logging.Formatter):
    def format(self, record: LogRecord) -> str:
        record.exc_info = None
        record.exc_text = None
        return super().format(record)


console_line = {
    "fmt": "{name: <10} | {levelname: <8} | {relativepath}:{lineno}: {message}",
    "style": "{",
}

file_line = {
    "fmt": "{asctime} | {name: <10} | {levelname: <8} | {relativepath}:{lineno}: {message}",
    "style": "{",
}


colored_console_formatter = ColoredConsoleFormatter(**console_line)
console_formatter = logging.Formatter(**console_line)
file_formatter = logging.Formatter(**file_line)
