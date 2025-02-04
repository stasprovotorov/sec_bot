from telebot import types
from telebot.handler_backends import StatesGroup, State
import editor_data as ed


class StatesBase(StatesGroup):
    @classmethod
    def get_states_list(cls):
        states_list = []

        for state in cls.__dict__.values():
            if isinstance(state, State):
                states_list.append(state.name)
                
        return states_list

    @classmethod
    def get_states_iter(cls):
        return iter(cls.get_states_list())


class StatesTextNew(StatesBase):
    text_sys_name = State()
    text_ru = State()
    text_en = State()


class StatesTextEdit(StatesBase):
    pass


class StatesTextDelete(StatesBase):
    pass


class StatesEditor:
    states = {
        'text': {
            'new': StatesTextNew,
            'edit': StatesTextEdit,
            'delete': StatesTextDelete
        }
    }


class Editor(StatesEditor):
    def __init__(self):
        self.user_states = {}
        self.dialog_data = {}

    def set_user_states(self, user_id, state):
        self.user_states[user_id] = state

    def get_next_user_state(self, user_id):
        return next(self.user_states[user_id])

    def save_user_input(self, user_state, user_input):
        self.dialog_data[user_state] = user_input
