editor_msg = {
    'editor_menu': {
        'ru': 'Что ты желаешь редактировать?',
        'en': 'What would you like to edit?'
    },
    'edit_txt_menu': {
        'ru': 'Что ты желаешь сделать с текстом?',
        'en': 'What do you want to do with the text?'
    },
    'edit_img_menu': {
        'ru': 'Что ты желаешь сделать с изображением?',
        'en': 'What do you want to do with the image?'
    },
    'edit_btn_menu': {
        'ru': 'Что ты желаешь сделать с кнопкой?',
        'en': 'What do you want to do with the button?'
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
    'image': {
        'new': {
            'enter_image_name': {
                'ru': 'Введите системное имя для изображения',
                'en': 'Enter a system name for the image'
            },
            'enter_image': {
                'ru': 'Зыгрузите изображение',
                'en': 'Upload image'
            }
        },
        'delete': {
            'push_image_name': {
                'ru': 'Выберите имя изображения для удаления',
                'en': 'Select image name for deleting'
            }
        }
    },
    'button': {
        'new': {
            'enter_button_name': {
                'ru': 'Введитие системное имя кнопки',
                'en': 'Enter a system name for the button'
            },
            'enter_button_label_ru': {
                'ru': 'Введите лейбл кнопки на русском языке',
                'en': 'Enter the button label in Russian'
            },
            'enter_button_label_en': {
                'ru': 'Введите лейбл кнопки на английском языке',
                'en': 'Enter the button label in English'
            },
            'enter_button_to_view_name': {
                'ru': 'Введите имя представления, вызываемое кнопкой',
                'en': 'Enter the name of the view called by the button'
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
            'cnt_next': 'edit_img_menu'
        },
        'buttons': {
            'label': {
                'ru': 'Кнопки',
                'en': 'Buttons'
            },
            'cnt_next': 'edit_btn_menu'
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
    'edit_img_menu': {
        'new_image': {
            'label': {
                'ru': 'Загрузить',
                'en': 'Upload'
            },
            'cnt_next': 'state:image:new'
        },
        'delete_image': {
            'label': {
                'ru': 'Удалить',
                'en': 'Delete'
            },
            'cnt_next': 'state:image:delete'
        }
    },
    'edit_btn_menu': {
        'new_button': {
            'label': {
                'ru': 'Создать кнопку',
                'en': 'New button'
            },
            'cnt_next': 'state:button:new'
        },
        'edit_button': {
            'label': {
                'ru': 'Редактировать кнопку',
                'en': 'Edit button'
            },
            'cnt_next': 'state:button:edit'
        },
        'delete_button': {
            'label': {
                'ru': 'Удалить кнопку',
                'en': 'Delete button'
            },
            'cnt_next': 'state:button:delete'
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
