import logging
import os
from colorlog import ColoredFormatter

def get_logger(name="el_pais"):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "execution.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)


        color_formatter = ColoredFormatter(
            "%(log_color)s%(levelname)s:%(reset)s %(message)s",
            log_colors={
                "DEBUG":    "cyan",
                "INFO":     "green",
                "WARNING":  "yellow",
                "ERROR":    "red",
                "CRITICAL": "bold_red",
            },
            secondary_log_colors={},
            style='%'
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(color_formatter)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)

    return logger
