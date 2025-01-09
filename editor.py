from user import Language
from telebot.handler_backends import StatesGroup, State


class StatesBase(StatesGroup):
    @classmethod
    def get_states(cls):
        return [i for i in cls.__dict__.values() if isinstance(i, State)]


class StatesText(StatesBase):
    vw_src = State()
    text_ru = State()
    text_en = State()
    

class StatesImage(StatesBase):
    vw_src = State()
    image = State()


class StatesButton(StatesBase):
    btn_sys_name = State()
    btn_label_ru = State()
    btn_label_en = State()
    vw_src = State()
    vw_next = State()


editor_dialog = {
    'button': {
        StatesButton.btn_sys_name: {
            Language.RU: 'Введите системное имя кнопки',
            Language.EN: 'Enter system button name'
        },
        StatesButton.btn_label_ru: {
            Language.RU: 'Введите значение лейбла кнопки на русском языке',
            Language.EN: 'Enter label value on russian language'
        },
        StatesButton.btn_label_en: {
            Language.RU: 'Введите значение лейбла кнопки на английском языке',
            Language.EN: 'Enter label value on english language'
        },
        StatesButton.vw_src: {
            Language.RU: 'Введите имя исходного представления',
            Language.EN: 'Enter source view name'
        },
        StatesButton.vw_next: {
            Language.RU: 'Введите имя поледующего представления',
            Language.EN: 'Enter next view name'
        }
    }
}


class Editor:
    def __init__(self):
        self.states_txt = StatesText.get_states()
        self.states_img = StatesImage.get_states()
        self.states_btn = StatesButton.get_states()


if __name__ == '__main__':
    editor = Editor()
