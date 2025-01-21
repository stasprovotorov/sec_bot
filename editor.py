from user import Language
from telebot import types
from telebot.handler_backends import StatesGroup, State
from editor_data import editor_msg, editor_btn


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
    text_sys_name = State()
    text_ru = State()
    text_en = State()
    confirmation = State()

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
        self.dialog_data = {}

    def dialog_provider(self, bot, user, user_state, chat_id, user_input):
        print(user_state, user_input)
        state_key, msg_key = user_state.split(':')
        self.dialog_data.setdefault(state_key, {})
        msg = editor_msg[msg_key][user.lang]
        prev_state_index = self.states[state_key].index(user_state) - 1
        try:
            index = self.states[state_key].index(user_state) + 1
            bot.set_state(user.user_id, self.states[state_key][index], chat_id)
            bot.send_message(user.user_id, msg)
        except IndexError:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            btn_row = []
            for btn_name in editor_btn['confirmation']:
                btn_row.append(
                    types.InlineKeyboardButton(
                        text=editor_btn['confirmation'][btn_name]['label'][user.lang],
                        callback_data=editor_btn['confirmation'][btn_name]['cnt_next']
                    )
                )
            keyboard.row(*btn_row)
            bot.send_message(user.user_id, msg, reply_markup=keyboard)
