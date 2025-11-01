import logging
import re
import os
from .constants import is_log_file, today, console_log_format,file_log_format, log_file_path, DateTimeFormats, AnsiColors

class CustomFormatter(logging.Formatter):
    """A custom formatter class for logging"""

    ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

    FORMATS = {
            logging.DEBUG: AnsiColors.BLUE.value + console_log_format,
            logging.INFO:  AnsiColors.GREEN.value + console_log_format,
            logging.WARNING: AnsiColors.YELLOW.value + console_log_format,
            logging.ERROR:  AnsiColors.RED.value  + console_log_format,
        }

    COLORS = {
        logging.DEBUG: AnsiColors.BLUE.value,
        logging.INFO: AnsiColors.GREEN.value,
        logging.WARNING: AnsiColors.YELLOW.value,
        logging.ERROR: AnsiColors.RED.value,
    }

    def format(self, record):
        log_colors = self.COLORS.get(record.levelno)
        log_fmt = self.FORMATS.get(record.levelno)
        # each element in self.FORMATS is a tuple(levelno: int, format: str: loggerFormat)
        formatter = logging.Formatter(log_fmt, datefmt= DateTimeFormats.DATE_TIME.value)  # Custom timestamp format
        return formatter.format(record)

class Logger():
    """
    A class is used to create a logger object

    Attributes:
        project_name (str): The name of the project
        level (object): The logging level
        logger (logging.Logger): The logger object
        ch (logging.StreamHandler): The console handler
        file_handler (logging.FileHandler): The file handler

    Methods:
        get_logger(): Returns the logger object
        set_logger(logger): Sets the logger object

    Returns:
        Logger: A logger object
    """

    def __init__(self, project_name: str='logger', level: object=logging.DEBUG, is_log_file = False):
        # set logger project name
        self.logger = logging.getLogger(project_name)

        #  Set the logging level
        self.logger.setLevel(level)

        # create console handler with a higher log level
        ch = logging.StreamHandler()

        # Set the logging level
        ch.setLevel(level)

        # Set the formatter for the console handler
        ch.setFormatter(CustomFormatter())

        # Add the console handler to the logger
        self.logger.addHandler(ch)

        # FileHandler (logs to a file)
        if is_log_file:
            # folder log
            if not os.path.exists(log_file_path):
                os.makedirs(log_file_path,exist_ok=True)
            file_handler = logging.FileHandler(f"{log_file_path}/{project_name}.log", mode= 'w', encoding="UTF-8")  # This will create a log file with the logger's name
            file_handler.setLevel(level)
            file_handler.setFormatter(logging.Formatter(file_log_format, datefmt= DateTimeFormats.DATE_TIME.value))
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

    def set_logger(self, logger):
        self.logger = logger
        return self.logger

logger = Logger(f'logger {today}', logging.DEBUG, is_log_file).get_logger()

