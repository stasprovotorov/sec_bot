from user import Language

class Text:
    def __init__(self, content_ru, content_en):
        self.lang = Language
        self.content = {
            self.lang.RU: content_ru,
            self.lang.EN: content_en
        }


class Message:
    def __init__(self, obj_bot, obj_user, obj_text):
        self.bot = obj_bot
        self.user_id = obj_user.user_id
        self.text = obj_text.content[obj_user.lang]

    def send(self):
        self.bot.send_message(self.user_id, self.text)
