editor_msg = {
    'editor_menu': {
        'ru': 'Что ты желаешь редактировать?',
        'en': 'What would you like to edit?'
    },
    'edit_txt_menu': {
                'ru': 'Что ты желаешь сделать с текстом?',
                'en': 'What do you want to do with the text?'
    },
    'text': {
        'new': {
            'enter_text_name': {
                'ru': 'Введите системное имя для текста',
                'en': 'Enter a system name for the text'
            },            
            'enter_text_ru': {
                'ru': 'Введите текст на русском языке',
                'en': 'Enter text in Russian'
            },
            'enter_text_en': {
                'ru': 'Введите тескт на английском языке',
                'en': 'Enter text in English'
            }
        },
        'edit': {
            'push_text_name': {
                'ru': 'Выберите текст для редактирования',
                'en': 'Select the text name for editing'
            },
            'push_text_lang': {
                'ru': 'Выберите язык редактирования',
                'en': 'Select the editing language'
            },
            'enter_text_edited': {
                'ru': 'Введите редактированный текст',
                'en': 'Enter the edited text'
            }
        },
        'delete': {
            'push_text_name': {
                'ru': 'Выберите текст для удаления',
                'en': 'Select the text name for deleting'
            }
        }
    },
    'confirmation': {
        'confirm_request': {
            'ru': 'Подтвердите данные',
            'en': 'Confirm data'
        },
        'confirm_response': {
            'approved': {
                'ru': 'Изменения сохранены',
                'en': 'Changes saved' 
            },
            'canceled': {
                'ru': 'Изменения отменены',
                'en': 'Changes canceled'
            }
        }
    }
}

editor_btn = {
    'editor_menu': {
        'texts': {
            'label': {
                'ru': 'Тексты',
                'en': 'Texts'
            },
            'cnt_next': 'edit_txt_menu'
        },
        'images': {
            'label': {
                'ru': 'Изображения',
                'en': 'Images'
            },
            'cnt_next': 'edit_img'
        },
        'buttons': {
            'label': {
                'ru': 'Кнопки',
                'en': 'Buttons'
            },
            'cnt_next': 'edit_btn'
        },
        'views': {
            'label': {
                'ru': 'Представления',
                'en': 'Views'
            },
            'cnt_next': 'edit_vw'
        }
    },
    'edit_txt_menu': {
        'new_text': {
            'label': {
                'ru': 'Новый текст',
                'en': 'New text'
            },
            'cnt_next': 'state:text:new'
        },
        'edit_text': {
            'label': {
                'ru': 'Редактировать текст',
                'en': 'Edit text'
            },
            'cnt_next': 'state:text:edit'
        },
        'delete_text': {
            'label': {
                'ru': 'Удалить текст',
                'en': 'Delete text'
            },
            'cnt_next': 'state:text:delete'
        }
    },
    'confirmation': {
        'confirm': {
            'label': {
                'ru': 'Подтвердить',
                'en': 'Confirm'
            },
            'cnt_next': 'confirm'
        },
        'cancel': {
            'label': {
                'ru': 'Отменить',
                'en': 'Cancel'
            },
            'cnt_next': 'cancel'
        }
    }
}

editor_states = {
    'text': {
        'new_text': (
            'text_sys_name',
            'text_ru',
            'text_en'
        )
    }
}

# Mapping state_groups to the content_types from data_content.db file structure
state_groups_text = ('StatesTextNew', 'StatesTextEdit', 'StatesTextDelete')
state_groups_image = ('StatesImageNew', 'StatesImageDelete')
state_groups_button = ('StatesButtonNew', 'StatesButtonEdit', 'StatesButtonDelete')
state_groups_view = ('StatesViewNew', 'StatesViewDelete')

state_groups_all = (
    state_groups_text, 
    state_groups_image, 
    state_groups_button, 
    state_groups_view
)

content_types = ('text', 'image', 'button', 'view')

state_group_to_content_type = {}
for content_type, state_group in zip(content_types, state_groups_all):
    state_group_to_content_type.update(
        dict.fromkeys(state_group, content_type)
    )
