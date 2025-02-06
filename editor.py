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
    enter_text_name = State()
    enter_text_ru = State()
    enter_text_en = State()


class StatesTextEdit(StatesBase):
    push_text_name = State()
    push_text_lang = State()
    enter_edited_text = State()


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

    def __init__(self, stg_content):
        self.stg_content = stg_content
        self.user_states = {}
        self.user_responses = {}

        self._state_to_storage_method = {
            'push_text_name': self.stg_content.text.get_all_text_names,
            'push_text_lang': lambda: ['ru', 'en']
        }

    def set_user_states(self, user_id, state):
        self.user_states[user_id] = state

    def get_next_user_state(self, user_id):
        return next(self.user_states[user_id])

    def collect_user_responses(self, user_id, user_state, user_input):
        content_type, action, state_name = self.state_parser(user_state)

        if user_id not in self.user_responses:
            self.user_responses[user_id] = {
                'content_type': content_type,
                'action': action,
                'user_responses': {}
            }
        
        self.user_responses[user_id]['user_responses'][state_name] = user_input

    def commit_user_responses(self, content_type, action, user_responses):
        if content_type == 'text':
            if action == 'new':
                self.stg_content.text.save(
                    name=user_responses['enter_text_name'],
                    text_ru=user_responses['enter_text_ru'],
                    text_en=user_responses['enter_text_en']
                )

            elif action == 'edit':
                lang = user_responses['push_text_lang']

                if lang == 'ru':
                    self.stg_content.text.save(
                        name=user_responses['push_text_name'],
                        text_ru=user_responses['enter_edited_text'],
                    )
                elif lang == 'en':
                    self.stg_content.text.save(
                        name=user_responses['push_text_name'],
                        text_en=user_responses['enter_edited_text'],
                    )

            elif action == 'delete':
                pass

        elif content_type == 'image':
            pass

        elif content_type == 'button':
            pass

        elif content_type == 'view':
            pass

    def state_to_keyboard(self, state_name):
        if state_name not in self._state_to_storage_method:
            return None
        
        button_labels = self._state_to_storage_method[state_name]()

        keyboard = types.ReplyKeyboardMarkup(
            resize_keyboard=True, 
            one_time_keyboard=True
        )

        for button_label in button_labels:
            keyboard.add(button_label)

        return keyboard

    def state_parser(self, state):
        state_group, state_name = state.split(':')

        index_left = 0
        separated_words = []

        for i, symbol in enumerate(state_group):
            if i > 0 and symbol.isupper():
                separated_words.append(state_group[index_left:i])
                index_left = i
        separated_words.append(state_group[index_left:])

        _, content_type, action = separated_words

        return content_type.lower(), action.lower(), state_name
