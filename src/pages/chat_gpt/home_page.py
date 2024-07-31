import time
from src.pages.chat_gpt.login_page import Login_Page
from src.pages.base_page import Base_Page

class Home_Page(Base_Page):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = "https://chatgpt.com/auth/login"

    login_button = "button[data-testid='login-button']"

    def go_chat_gpt_home(self):
        self.page.goto(self.url)

    def click_login_button(self):
        time.sleep(1)
        for i in range(0, 6):
            self.click_element(self.login_button)
            time.sleep(3)
            if self.page.url != self.url:
                break

        return Login_Page(self.page)
