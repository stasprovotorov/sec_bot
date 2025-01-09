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


class Editor:
    def __init__(self):
        self.states_txt = StatesText.get_states()
        self.states_img = StatesImage.get_states()
        self.states_btn = StatesButton.get_states()


if __name__ == '__main__':
    editor = Editor()
