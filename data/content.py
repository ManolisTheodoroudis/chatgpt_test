from lorem_text import lorem


class Content:

    def get_static_content(self):
        static_content = "What is the most famous place in Thessaloniki?"
        return static_content

    def get_static_answer(self):
        static_content = "White Tower"
        return static_content

    def get_file_name(self):
        static_content = "white_tower.png"
        return static_content

    def get_random_content(self):
        random_content = lorem.sentence()
        return random_content