from user import Language
from io import BytesIO
from telebot import types

class Text:
    def __init__(self, content_ru, content_en):
        self.lang = Language
        self.content = {
            self.lang.RU: content_ru,
            self.lang.EN: content_en
        }


class Image:
    def __init__(self, img_path):
        with open(img_path, 'rb') as img:
            self.img = img.read()


class Button:
    def __init__(self, view_name, label_ru, label_en, result):
        self.view_name = view_name
        self.lang = Language
        self.label = {self.lang.RU: label_ru, self.lang.EN: label_en}
        self.result = result
    
    def __call__(self, user_lang):
        return types.InlineKeyboardButton(self.label[user_lang], callback_data=self.result)


class Keyboard:
    def __init__(self, view_name):
        self.view_name = view_name
        self.buttons = []
    
    def __call__(self, view_name):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*self.buttons)
        return keyboard


class СontentOutput:
    def __init__(self, obj_bot, obj_user, obj_text=None, obj_image=None):
        self.bot = obj_bot
        self.user_id = obj_user.user_id
        self.text = obj_text.content[obj_user.lang] if obj_text else obj_text
        self.image = BytesIO(obj_image.img) if obj_image else obj_image
        
    def send(self):
        if self.text:
            self.bot.send_message(self.user_id, self.text)
        if self.image:
            self.bot.send_photo(self.user_id, self.image)
