from src.pages.chat_gpt.home_page import Home_Page


class Login_Functions:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        home = Home_Page(self.page)
        home.go_chat_gpt_home()
        login = home.click_login_button()
        login.fill_username(username)
        login.click_continue_username()
        login.fill_password(password)
        login.click_continue_password()