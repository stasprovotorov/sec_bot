from user import Language
from telebot.handler_backends import StatesGroup, State
from editor_dialog import editor_dialog

class StatesBase(StatesGroup):
    @classmethod
    def get_states_obj(cls):
        return [i for i in cls.__dict__.values() if isinstance(i, State)]

    @classmethod
    def get_states_str(cls):
        states = []
        for attr, value in cls.__dict__.items():
            if isinstance(value, State):
                states.append(f'{cls.__name__}:{attr}')
        return states


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
        self.states = {
            'StatesText': StatesText.get_states_str(),
            'StatesImage': StatesImage.get_states_str(),
            'StatesButton': StatesButton.get_states_str()
        }

    def dialog_provider(self, bot, user, user_state, chat_id):
        state_key, msg_key = user_state.split(':')
        msg = editor_dialog[state_key][msg_key][user.lang]
        bot.send_message(user.user_id, msg)
        try:
            index = self.states[state_key].index(user_state) + 1
            bot.set_state(user.user_id, self.states[state_key][index], chat_id)
        except IndexError:
            bot.delete_state(user.user_id, )
