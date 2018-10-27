
import logging
from pythonjsonlogger import jsonlogger
from logging.config import fileConfig

if __name__ == "__main__":

    fileConfig("log_config.ini")
    # to make logging happen in GMT time
    import time
    logging.Formatter.converter = time.gmtime


    log_message_info = {"message": "info message",
                        "input": {"x": 5, "y": 6}}

    log_message_warn = {"message": "warn message",
                        "input": {"x": 0, "y": 0}}

    log_message_error = {"message": "error message"}

    logging.info(log_message_info)
    logging.warn(log_message_warn)
    logging.error(log_message_error)
