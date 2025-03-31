from telebot.handler_backends import State, StatesGroup


class StatesEditorTextCreate(StatesGroup):
    enter_text_name = State()
    enter_text_ru = State()
    enter_text_en = State()

class StatesEditorTextEdit(StatesGroup):
    choose_text_name = State()
    choose_text_language = State()
    enter_text = State()

class StatesEditorTextDelete(StatesGroup):
    choose_text_name = State()
    choose_text_language = State()

class StatesEditorImageLoad(StatesGroup):
    enter_image_name = State()
    attach_image = State()

class StatesEditorImageDelete(StatesGroup):
    choose_image_name = State()

class StatesEditorButtonCreate(StatesGroup):
    enter_button_name = State()
    enter_button_label_ru = State()
    enter_button_label_en = State()
    enter_button_message = State()

class StatesEditorButtonEditLabel(StatesGroup):
    choose_button_name = State()
    choose_button_label_language = State()
    enter_button_label = State()

class StatesEditorButtonEditMessageCall(StatesGroup):
    choose_button_name = State()
    enter_button_message = State()

class StatesEditorButtonDelete(StatesGroup):
    choose_button_name = State()

class StatesEditorMessageCreate(StatesGroup):
    enter_message_name = State()
    choose_message_text_name = State()
    choose_message_image_name = State()
    choose_message_button_name = State()

class StatesEditorMessageEditTextReplace(StatesGroup):
    enter_message_name = State()
    choose_message_text_name_added = State()

class StatesEditorMessageEditButtonAdd(StatesGroup):
    choose_message_name = State()
    choose_message_button_name_added = State()

class StatesEditorMessageEditButtonReplace(StatesGroup):
    choose_message_name = State()
    choose_message_button_name_current = State()
    choose_message_button_name_added = State()

class StatesEditorMessageEditButtonDelete(StatesGroup):
    choose_message_name = State()
    choose_message_button_name = State()

class StatesEditorMessageEditImageAdd(StatesGroup):
    choose_message_name = State()
    choose_message_image_name = State()

class StatesEditorMessageEditImageReplace(StatesGroup):
    choose_message_name = State()
    choose_message_image_name_current = State()
    choose_message_image_name_added = State()

class StatesEditorMessageEditImageDelete(StatesGroup):
    choose_message_name = State()
    choose_message_image_name = State()

class StatesEditorMessageDelete(StatesGroup):
    choose_message_name = State()

class StatesEditorRolesAssign(StatesGroup):
    attach_contact = State()
    choose_role_added = State()
    
class StatesEditorRolesRemove(StatesGroup):
    attach_contact = State()
    choose_role_current = State()
