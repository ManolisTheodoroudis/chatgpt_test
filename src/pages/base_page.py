from playwright.sync_api import Page, expect
from config.config import CONF


class Base_Page:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 5000

    input_file = "input[type='file']"

    def set_timeout(self, timeout):
        self.timeout = timeout

    def click_element(self, selector: str):
        try:
            element = self.page.locator(selector)
            expect(element).to_be_visible(timeout=self.timeout)
            expect(element).to_be_enabled(timeout=self.timeout)
            element.click()
            CONF.logger.info(f"click_element '{selector}'")
        except Exception as e:
            raise Exception(f"Failed to click element with selector '{selector}': {str(e)}")

    def fill_input(self, selector: str, value: str):
        try:
            element = self.page.locator(selector)
            expect(element).to_be_visible(timeout=self.timeout)
            expect(element).to_be_enabled(timeout=self.timeout)
            element.fill(value)
            CONF.logger.info(f"fill_input '{selector}' and value '{value}'")
        except Exception as e:
            raise Exception(f"Failed to fill input with selector '{selector}': {str(e)}")

    def press_input(self, selector: str, value: str):
        try:
            element = self.page.locator(selector)
            expect(element).to_be_visible(timeout=self.timeout)
            expect(element).to_be_enabled(timeout=self.timeout)
            element.press(value)
            CONF.logger.info(f"press_input '{selector}' and value '{value}'")
        except Exception as e:
            raise Exception(f"Failed to fill input with selector '{selector}': {str(e)}")

    def get_text(self, selector: str) -> str:
        try:
            elements = self.page.locator(selector)
            first_element = elements.first
            expect(first_element).to_be_visible(timeout=60000)  # Use a larger timeout if needed
            text = first_element.inner_text()
            CONF.logger.info(f"get_text '{selector}' text '{text}'")
            return text
        except Exception as e:
            raise Exception(f"Failed to get text from element with selector '{selector}': {str(e)}")

    def is_element_visible(self, selector: str) -> bool:
        try:
            element = self.page.locator(selector)
            is_visible =  element.is_visible(timeout=self.timeout)
            CONF.logger.info(f"is_element_visible '{selector}' : '{is_visible}'")
            return is_visible
        except Exception:
            return False

    def press_keyboard_enter(self,):
        try:
            self.page.keyboard.press('Enter')
            CONF.logger.info(f"press_keyboard_enter")
        except Exception as e:
            raise Exception(f"Failed to fill input with selector: {str(e)}")

    def wait_until_element_is_hidden(self, selector):
        element = self.page.locator(selector)
        while not element.is_hidden():
            CONF.logger.info(f"wait until element {selector}  is hidden ")
            self.page.wait_for_timeout(100)  # Wait 100ms before checking again
            try:
                element = self.page.locator(selector)  # Refresh the element locator
            except Exception as e:
                CONF.logger.info(f"Exception {e}")

    def wait_until_element_is_enabled(self, selector):
        element = self.page.locator(selector)
        while not element.is_visible():
            CONF.logger.info(f"wait until element {selector}  is visible ")
            self.page.wait_for_timeout(100)  # Wait 100ms before checking again
            element = self.page.locator(selector)  # Refresh the element locator

    def upload_file(self, file_path):
        CONF.logger.info(f"Upload file {file_path}")
        self.page.locator(self.input_file).set_input_files(file_path)

    def upload_file_with_js(self, file_path):
        CONF.logger.info(f"Upload file with javascript {file_path}")
        with self.page.expect_file_chooser() as fc_info:
            self.page.evaluate("""() => {
                const input = document.createElement('input');
                input.type = 'file';
                input.click();
            }""")
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)




