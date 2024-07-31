import pytest
from data.users import User
from src.funtions.chat_gpt.chat import Chat_Functions
from src.funtions.chat_gpt.login import Login_Functions
from src.pages.chat_gpt.chat_page import Chat_Page

@pytest.mark.usefixtures("page")
class TestChatGptUpload:

    def test_chat_gpt_verify_upload(self, page):
        username = User.get_username()
        password = User.get_password()
        Login_Functions(page).login(username, password)
        Chat_Functions(page).chat_with_image()
        Chat_Page(page).logout()

if __name__ == '__main__':
    pytest.main(["-v", "--tb=short"])  # Adding verbose flag for detailed output