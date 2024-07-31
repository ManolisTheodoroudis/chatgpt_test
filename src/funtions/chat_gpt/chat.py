from src.pages.chat_gpt.chat_page import Chat_Page
from utils.assertions import Assert
from data.content import Content

class Chat_Functions:
    def __init__(self, page):
        self.page = page

    def chat_text_messages(self):
        chat = Chat_Page(self.page)
        chat.ask_valid_question()
        chat.press_enter()
        chat.wait_until_answer_is_given()
        answer = chat.get_answer()
        expected_text = Content().get_static_answer()
        Assert.contains(expected_text, answer, "Chat Gpt first answer is not correct")
        chat.ask_valid_gibberish()
        chat.press_enter()
        chat.wait_until_answer_is_given()
        answer = chat.get_answer()
        Assert.is_true(len(answer) > 0 , "Chat Gpt second answer is not correct")

    def chat_with_image(self):
        chat = Chat_Page(self.page)
        filename = Content().get_file_name()
        chat.ask_valid_question()
        chat.upload_file(filename)
        chat.press_enter()
        chat.wait_until_answer_is_given()
        answer = chat.get_answer()
        expected_text = Content().get_static_answer()
        Assert.contains(expected_text, answer, "Chat Gpt answer is not correct")
