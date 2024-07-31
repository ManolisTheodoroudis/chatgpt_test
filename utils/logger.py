import logging
import datetime
import os
from config.config import CONF


class Logger_Utils():

    def __init__(self):
        self.logger = None

    def set_logger(self, logger):
        self.logger = logger

    def get_logger(self):
        return self.logger

    def setup_logger(self):
        run_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        logger = logging.getLogger("Test_Suite")
        logger.setLevel(logging.INFO)
        logs_directory = f"logs/logger_{run_time}"
        run_handler = self.format_logger(f"{logs_directory}/logger")
        logger.addHandler(run_handler)
        CONF.set_logger(logger)
        CONF.set_log_folder(logs_directory)


    def format_logger(self, file_path):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        handler = logging.FileHandler(f'{file_path}.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        return handler