class Config:

    def __init__(self):
        self.logger = None
        self.suite_logger = None
        self.driver = None
        self.log_folder = None

    def set_logger(self, logger):
        self.logger = logger

    def set_driver(self, driver):
        self.driver = driver

    def get_page(self, url):
        self.driver.get(url)

    def set_log_folder(self, log_folder):
        self.log_folder = log_folder

    def set_suite_logger(self, logger):
        self.suite_logger = logger


CONF = Config()