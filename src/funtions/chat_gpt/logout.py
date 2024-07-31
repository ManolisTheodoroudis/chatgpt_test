from src.pages.chat_gpt.chat_page import Chat_Page
from utils.assertions import Assert
from src.pages.chat_gpt.home_page import Home_Page

class Logout_Functions:
    def __init__(self, page):
        self.page = page

    def logout(self):
        chat = Chat_Page(self.page)
        chat.logout()
        home = Home_Page(self.page)
        current_url = self.page.url
        Assert().are_equal(home.url, current_url, "logout has failed to redirect to the home page")