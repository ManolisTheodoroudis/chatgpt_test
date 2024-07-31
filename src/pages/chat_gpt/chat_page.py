import time
from data.content import Content
from src.pages.base_page import Base_Page
from config.config import CONF
from utils.file import File_Utils


class Chat_Page(Base_Page):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.content = Content()

    # Locators
    answer_area = "div[data-message-author-role='assistant'] p"
    text_area = "#prompt-textarea"
    send_button = "button[data-testid='send-button']"
    stop_button = "button[data-testid='stop-button']"
    user_button = "[data-testid='profile-button']"
    menu_item = "[role='menuitem']"
    upload_icon = "[type='button']  button[class*='text-token-text-primary']"

    def upload_file(self, filename):
        try:
            file_path = File_Utils().get_filepath(filename)

            CONF.logger.info("Clicking the upload icon.")
            element = self.page.locator(self.upload_icon).nth(-1)
            element.click()

            CONF.logger.info("Click on the last menu item to trigger file chooser")
            elements = self.page.locator(self.menu_item)
            elements.last.click()

            # 1st approach that is not currently working
            self.upload_file(file_path)

            # 2nd approach that seem to work
            self.upload_file_with_js(file_path)
        except Exception as e:
            CONF.logger.error(f"Failed to upload file '{filename}': {e}")
            raise
        CONF.logger.info("file uploaded successfully")

    def logout(self):
        self.click_element(self.user_button)
        elements = self.page.locator(self.menu_item)
        elements.last.click()

    def ask_valid_question(self):
        static_content = self.content.get_static_content()
        self.fill_text(static_content)

    def ask_valid_gibberish(self):
        random_content = self.content.get_random_content()
        self.fill_text(random_content)

    def fill_text(self, text):
        self.fill_input(self.text_area, text)

    def press_enter(self):
        self.press_input(self.text_area, "Enter")

    def get_answer(self):
        return self.get_text(self.answer_area)

    def ask(self):
        return self.click_element(self.send_button)

    def wait_until_answer_is_given(self):
        time.sleep(1)
        self.wait_until_element_is_hidden(self.stop_button)
