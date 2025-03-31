'''
This is a module for retrieving text that is sent in a dialogue with the user when they are editing the bot.
'''


def get_message(user_action: str, message_language: str) -> str:
    '''A function to get a message from callback_messages using callback_data or state name.'''

    if user_action.startswith('editor'):
        _, *message_keys = user_action.split(':')
    elif user_action.startswith('States'):
        message_keys = user_action.split(':')

    index = 0

    def recursion(editor_messages: dict, callback_key: str) -> str:
        nonlocal index

        result = editor_messages[callback_key]

        try:
            return result[message_language]
        except KeyError:
            index += 1
            return recursion(result, message_keys[index])

    return recursion(EDITOR_MESSAGES, message_keys[0])


EDITOR_MESSAGES = {
    'menu': {
        'ru': 'Выберите компонент бота для редактирования',
        'en': None
    },
    'text': {
        'action': {
            'ru': 'Выберите действие с текстом',
            'en': None
        }
    },
    'image': {
        'action': {
            'ru': 'Выберите действие с изображением',
            'en': None
        }
    },
    'button': {
        'action': {
            'ru': 'Выберите действие с кнопкой',
            'en': None
        },
        'edit': {
            'component': {
                'ru': 'Выберите компонент кнопки, который вы желаете отредактировать',
                'en': None
            }
        }
    },
    'message': {
        'action': {
            'ru': 'Выберите действие с сообщением',
            'en': None
        },
        'edit': {
            'component': {
                'ru': 'Выберите компонент сообщения, который вы желаете отредактировать',
                'en': None
            },
            'button': {
                'action': {
                    'ru': 'Выберите действие, которые вы желаете выполнить с кнопкой сообщения',
                    'en': None
                },
            },
            'image': {
                'action': {
                    'ru': 'Выберите действие, которые вы желаете выполнить с изображением сообщения',
                    'en': None
                },
            }
        },
    },
    'role': {
        'action':{
            'ru': 'Выберите действие для роли у пользователя',
            'en': None
        }
    },
    'StatesEditorTextCreate': {
        'enter_text_name': {
            'ru': 'Введите наименование для нового текста',
            'en': None
        },
        'enter_text_ru': {
            'ru': 'Введите текст на русском языке',
            'en': None
        },
        'enter_text_en': {
            'ru': 'Введите текст на английском языке',
            'en': None
        }
    },
    'StatesEditorTextEdit': {
        'choose_text_name': {
            'ru': 'Выберите наименование текста, который вы желаете отредактировать',
            'en': None
        },
        'choose_text_language': {
            'ru': 'Выберите язык текста',
            'en': None
        },
        'enter_text': {
            'ru': 'Введите текст',
            'en': None
        }
    },
    'StatesEditorTextDelete': {
        'choose_text_name': {
            'ru': 'Выберите наименование текста, который вы желаете удалить',
            'en': None
        },
        'choose_text_language': {
            'ru': 'Выберите язык текста, который вы желаете удалить',
            'en': None
        }
    },
    'StatesEditorImageLoad': {
        'enter_image_name': {
            'ru': 'Введите наименование для загружаемого изображения',
            'en': None
        },
        'attach_image': {
            'ru': 'Отправьте изображение',
            'en': None
        }
    },
    'StatesEditorImageDelete': {
        'choose_image_name': {
            'ru': 'Введите наименование изображения, которое вы желаете удалить',
            'en': None
        }
    },
    'StatesEditorButtonCreate': {
        'enter_button_name': {
            'ru': 'Введите наименование для новой кнопки',
            'en': None
        },
        'enter_button_label_ru': {
            'ru': 'Введите значение лейбла кнопки на русском языке',
            'en': None
        },
        'enter_button_label_en': {
            'ru': 'Введите значение лейбла кнопки на английском языке',
            'en': None
        },
        'enter_button_message_call': {
            'ru': 'Введите значение вызова сообщения у кнопки',
            'en': None
        }
    },
    'StatesEditorButtonEditLabel': {
        'choose_button_name': {
            'ru': 'Выберите наименование кнопки, лейбл которой вы желаете отредактировать',
            'en': None
        },
        'choose_button_label_language': {
            'ru': 'Выберите язык лейбла кнопки, который вы желаете отредактировать',
            'en': None
        },
        'enter_button_label': {
            'ru': 'Введите новое значение лейбла кнопки',
            'en': None
        }
    },
    'StatesEditorButtonEditMessageCall': {
        'choose_button_name': {
            'ru': 'Выберите наименование кнопки, вызов сообщения которой вы желаете отредактировать',
            'en': None
        },
        'enter_button_message': {
            'ru': 'Введите значение вызова сообщения для кнопки',
            'en': None
        }
    },
    'StatesEditorButtonDelete': {
        'choose_button_name': {
            'ru': 'Выберите наименование кнопки, которую вы желаете удалить',
            'en': None
        }
    },
    'StatesEditorMessageCreate': {
        'enter_message_name': {
            'ru': 'Введите наименование для нового сообщения',
            'en': None
        },
        'choose_message_text_name': {
            'ru': 'Выберите наименование текста, который будет в сообщении',
            'en': None
        },
        'choose_message_image_name': {
            'ru': 'Выберите наименование изображения, которое будет в сообщении',
            'en': None
        },
        'choose_message_button_name': {
            'ru': 'Выберите наименование кнопок, которые будут в сообщении',
            'en': None
        }
    },
    'StatesEditorMessageEditTextReplace': {
        'enter_message_name': {
            'ru': 'Выберите наименование сообщения, текст которого вы желаете заменить',
            'en': None
        },
        'choose_message_text_name_added': {
            'ru': 'Выберите наименование текста, на который вы хотите сделать замену',
            'en': None
        }
    },
    'StatesEditorMessageEditButtonAdd': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, к которому вы желаете добавить кнопку',
            'en': None
        },
        'choose_message_button_name_added': {
            'ru': 'Выберите наименование кнопки, которую хотите добавить в сообщение',
            'en': None
        }
    },
    'StatesEditorMessageEditButtonReplace': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете заменить кнопку',
            'en': None
        },
        'choose_message_button_name_current': {
            'ru': 'Выберите наименование кнопки сообщения, которую вы желаете заменить',
            'en': None
        },
        'choose_message_button_name_added': {
            'ru': 'Выберите наименование кнопки, на которую вы желаете сделать замену',
            'en': None
        }
    },
    'StatesEditorMessageEditButtonDelete': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете удалить кнопку',
            'en': None
        },
        'choose_message_button_name': {
            'ru': 'Выберите наименование кнопки сообщения, которую вы желаете удалить',
            'en': None
        }
    },
    'StatesEditorMessageEditImageAdd': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, к которому вы желаете добавить изображение',
            'en': None
        },
        'choose_message_image_name': {
            'ru': 'Выберите наименование изображения, которое вы желаете добавить в сообщение',
            'en': None
        }
    },
    'StatesEditorMessageEditImageReplace': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете заменить изображение',
            'en': None
        },
        'choose_message_image_name_current': {
            'ru': 'Выберите наименование изображения сообщения, которое вы желаете заменить',
            'en': None
        },
        'choose_message_image_name_added': {
            'ru': 'Выберите наименование изображения, на которое вы желаете сделать замену',
            'en': None
        }
    },
    'StatesEditorMessageEditImageDelete': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете удалить изображение',
            'en': None
        },
        'choose_message_image_name': {
            'ru': 'Выберите наименование изображения сообщения, которое вы желаете удалить',
            'en': None
        }
    },
    'StatesEditorMessageDelete': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, которое вы желаете удалить',
            'en': None
        }
    },
    'StatesEditorRolesAssign': {
        'attach_contact': {
            'ru': 'Пришлите контакт пользователя в приложении',
            'en': None
        },
        'choose_role_added': {
            'ru': 'Выберите роль, которую вы желаете добавить пользователю',
            'en': None
        }
    },
    'StatesEditorRolesRemove': {
        'attach_contact': {
            'ru': 'Пришлите контакт пользователя в приложении',
            'en': None
        },
        'choose_role_current': {
            'ru': 'Выберите роль, которую вы желаете убрать у пользователя',
            'en': None
        }
    }
}
