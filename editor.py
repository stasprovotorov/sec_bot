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
    text_choose_sys_name = State()
    text_choose_lang = State()
    text_enter = State()


class StatesTextDelete(StatesBase):
    text_choose_sys_name = State()


class StatesImageNew(StatesBase):
    image_sys_name = State()
    image_enter = State()


class StatesImageDelete(StatesBase):
    image_choose_sys_name = State()


class StatesButtonNew(StatesBase):
    button_sys_name = State()
    button_label_ru = State()
    button_label_en = State()
    button_action = State()


# As example. Should be refactored in future
class StatesButtonEdit(StatesBase):
    button_choose_sys_name = State()
    button_choose_component = State()
    button_edit_component = State()


class StatesButtonDelete(StatesBase):
    button_choose_sys_name = State()


class StatesViewNew(StatesBase):
    view_sys_name = State()
    view_choose_text = State()
    view_choose_image = State()
    view_choose_button = State()


# To think about. Not added to StatesEditor.states
class StatesViewEdit(StatesBase):
    pass


class StatesViewDelete(StatesBase):
    view_choose_sys_name = State()


class StatesEditor:
    states = {
        'text': {
            'new': StatesTextNew,
            'edit': StatesTextEdit,
            'delete': StatesTextDelete
        },
        'image': {
            'new': StatesImageNew,
            'delete': StatesImageDelete
        },
        'button': {
            'new': StatesButtonNew,
            'edit': StatesButtonEdit,
            'delete': StatesButtonDelete
        },
        'view': {
            'new': StatesButtonNew,
            'delete': StatesButtonDelete
        }
    }

    @classmethod
    def get_all_states(cls):
        all_states = []

        for state_category in cls.states.values():
            for state_group in state_category.values():
                all_states.extend(state_group.get_states_list())
                
        return all_states
    

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


if __name__ == '__main__':
    editor = Editor()

    all_states = editor.get_all_states()

    print(*all_states, sep='\n')
