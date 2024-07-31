from src.pages.base_page import Base_Page


class Login_Page(Base_Page):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    # Locators
    continue_username_button = ".continue-btn"
    continue_password_button = "._button-login-password"
    user_name = ".email-input"
    password = "#password"

    def fill_username(self, username):
        self.fill_input(self.user_name, username)

    def fill_password(self, password):
        self.fill_input(self.password, password)

    def click_continue_username(self):
        self.click_element(self.continue_username_button)

    def click_continue_password(self):
        self.click_element(self.continue_password_button)