'''
This is a module for retrieving text that is sent in a dialogue with the user when they are editing the bot.
'''


def get_message(user_action: str, message_language: str) -> str:
    '''A function to get a message from callback_messages using callback_data or state name.'''

    message_keys = user_action.split(':')
    message_keys = message_keys[1:] if message_keys[0] == 'editor' else message_keys

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
        'en': 'Select a bot component to edit'
    },
    'text': {
        'action': {
            'ru': 'Выберите действие с текстом',
            'en': 'Select an action with text'
        }
    },
    'image': {
        'action': {
            'ru': 'Выберите действие с изображением',
            'en': 'Select an action with image'
        }
    },
    'button': {
        'action': {
            'ru': 'Выберите действие с кнопкой',
            'en': 'Select an action with button'
        },
        'edit': {
            'component': {
                'ru': 'Выберите компонент кнопки, который вы желаете отредактировать',
                'en': 'Select the button component you want to edit'
            }
        }
    },
    'message': {
        'action': {
            'ru': 'Выберите действие с сообщением',
            'en': 'Select an action with message'
        },
        'edit': {
            'component': {
                'ru': 'Выберите компонент сообщения, который вы желаете отредактировать',
                'en': 'Select the message component you want to edit'
            },
            'button': {
                'action': {
                    'ru': 'Выберите действие, которые вы желаете выполнить с кнопкой сообщения',
                    'en': 'Select the action you want to perform with the message button'
                },
            },
            'image': {
                'action': {
                    'ru': 'Выберите действие, которые вы желаете выполнить с изображением сообщения',
                    'en': 'Select the action you want to perform with the message image'
                },
            }
        },
    },
    'role': {
        'action':{
            'ru': 'Выберите действие для роли у пользователя',
            'en': 'Select an action for the user role'
        }
    },
    'StatesEditorTextCreate': {
        'enter_text_name': {
            'ru': 'Введите наименование для нового текста',
            'en': 'Enter a name for the new text'
        },
        'enter_text_ru': {
            'ru': 'Введите текст на русском языке',
            'en': 'Enter text in Russian'
        },
        'enter_text_en': {
            'ru': 'Введите текст на английском языке',
            'en': 'Enter text in English'
        }
    },
    'StatesEditorTextEdit': {
        'choose_text_name': {
            'ru': 'Выберите наименование текста, который вы желаете отредактировать',
            'en': 'Select the text name you want to edit'
        },
        'choose_text_language': {
            'ru': 'Выберите язык текста',
            'en': 'Select the text language'
        },
        'enter_text': {
            'ru': 'Введите текст',
            'en': 'Enter the text'
        }
    },
    'StatesEditorTextDelete': {
        'choose_text_name': {
            'ru': 'Выберите наименование текста, который вы желаете удалить',
            'en': 'Select the text name you want to delete'
        },
        'choose_text_language': {
            'ru': 'Выберите язык текста, который вы желаете удалить',
            'en': 'Select the text language you want to delete'
        }
    },
    'StatesEditorImageLoad': {
        'enter_image_name': {
            'ru': 'Введите наименование для загружаемого изображения',
            'en': 'Enter a name for the image to be uploaded'
        },
        'attach_image': {
            'ru': 'Отправьте изображение',
            'en': 'Send the image'
        }
    },
    'StatesEditorImageDelete': {
        'choose_image_name': {
            'ru': 'Введите наименование изображения, которое вы желаете удалить',
            'en': 'Enter the name of the image you want to delete'
        }
    },
    'StatesEditorButtonCreate': {
        'enter_button_name': {
            'ru': 'Введите наименование для новой кнопки',
            'en': 'Enter a name for the new button'
        },
        'enter_button_label_ru': {
            'ru': 'Введите значение лейбла кнопки на русском языке',
            'en': 'Enter the button label value in Russian'
        },
        'enter_button_label_en': {
            'ru': 'Введите значение лейбла кнопки на английском языке',
            'en': 'Enter the button label value in English'
        },
        'enter_button_message_call': {
            'ru': 'Введите значение вызова сообщения у кнопки',
            'en': 'Enter the message call value for the button'
        }
    },
    'StatesEditorButtonEditLabel': {
        'choose_button_name': {
            'ru': 'Выберите наименование кнопки, лейбл которой вы желаете отредактировать',
            'en': 'Select the name of the button whose label you want to edit'
        },
        'choose_button_label_language': {
            'ru': 'Выберите язык лейбла кнопки, который вы желаете отредактировать',
            'en': 'Select the button label language you want to edit'
        },
        'enter_button_label': {
            'ru': 'Введите новое значение лейбла кнопки',
            'en': 'Enter a new button label value'
        }
    },
    'StatesEditorButtonEditMessageCall': {
        'choose_button_name': {
            'ru': 'Выберите наименование кнопки, вызов сообщения которой вы желаете отредактировать',
            'en': 'Select the name of the button whose message call you want to edit'
        },
        'enter_button_message': {
            'ru': 'Введите значение вызова сообщения для кнопки',
            'en': 'Enter the message call value for the button'
        }
    },
    'StatesEditorButtonDelete': {
        'choose_button_name': {
            'ru': 'Выберите наименование кнопки, которую вы желаете удалить',
            'en': 'Select the name of the button you want to delete'
        }
    },
    'StatesEditorMessageCreate': {
        'enter_message_name': {
            'ru': 'Введите наименование для нового сообщения',
            'en': 'Enter a name for the new message'
        },
        'choose_message_text_name': {
            'ru': 'Выберите наименование текста, который будет в сообщении',
            'en': 'Select the text name that will be in the message'
        },
        'choose_message_image_name': {
            'ru': 'Выберите наименование изображения, которое будет в сообщении',
            'en': 'Select the image name that will be in the message'
        },
        'choose_message_button_name': {
            'ru': 'Выберите наименование кнопок, которые будут в сообщении',
            'en': 'Select the button names that will be in the message'
        }
    },
    'StatesEditorMessageEditTextReplace': {
        'enter_message_name': {
            'ru': 'Выберите наименование сообщения, текст которого вы желаете заменить',
            'en': 'Select the name of the message whose text you want to replace'
        },
        'choose_message_text_name_added': {
            'ru': 'Выберите наименование текста, на который вы хотите сделать замену',
            'en': 'Select the text name you want to replace with'
        }
    },
    'StatesEditorMessageEditButtonAdd': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, к которому вы желаете добавить кнопку',
            'en': 'Select the name of the message to which you want to add a button'
        },
        'choose_message_button_name_added': {
            'ru': 'Выберите наименование кнопки, которую хотите добавить в сообщение',
            'en': 'Select the name of the button you want to add to the message'
        }
    },
    'StatesEditorMessageEditButtonReplace': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете заменить кнопку',
            'en': 'Select the name of the message whose button you want to replace'
        },
        'choose_message_button_name_current': {
            'ru': 'Выберите наименование кнопки сообщения, которую вы желаете заменить',
            'en': 'Select the current message button name you want to replace'
        },
        'choose_message_button_name_added': {
            'ru': 'Выберите наименование кнопки, на которую вы желаете сделать замену',
            'en': 'Select the button name you want to replace with'
        }
    },
    'StatesEditorMessageEditButtonDelete': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете удалить кнопку',
            'en': 'Select the name of the message whose button you want to delete'
        },
        'choose_message_button_name': {
            'ru': 'Выберите наименование кнопки сообщения, которую вы желаете удалить',
            'en': 'Select the message button name you want to delete'
        }
    },
    'StatesEditorMessageEditImageAdd': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, к которому вы желаете добавить изображение',
            'en': 'Select the name of the message to which you want to add an image'
        },
        'choose_message_image_name': {
            'ru': 'Выберите наименование изображения, которое вы желаете добавить в сообщение',
            'en': 'Select the name of the image you want to add to the message'
        }
    },
    'StatesEditorMessageEditImageReplace': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете заменить изображение',
            'en': 'Select the name of the message whose image you want to replace'
        },
        'choose_message_image_name_current': {
            'ru': 'Выберите наименование изображения сообщения, которое вы желаете заменить',
            'en': 'Select the current message image name you want to replace'
        },
        'choose_message_image_name_added': {
            'ru': 'Выберите наименование изображения, на которое вы желаете сделать замену',
            'en': 'Select the image name you want to replace with'
        }
    },
    'StatesEditorMessageEditImageDelete': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, у которого вы желаете удалить изображение',
            'en': 'Select the name of the message whose image you want to delete'
        },
        'choose_message_image_name': {
            'ru': 'Выберите наименование изображения сообщения, которое вы желаете удалить',
            'en': 'Select the message image name you want to delete'
        }
    },
    'StatesEditorMessageDelete': {
        'choose_message_name': {
            'ru': 'Выберите наименование сообщения, которое вы желаете удалить',
            'en': 'Select the name of the message you want to delete'
        }
    },
    'StatesEditorRolesAssign': {
        'attach_contact': {
            'ru': 'Пришлите контакт пользователя в приложении',
            'en': 'Send the user contact in the app'
        },
        'choose_role_added': {
            'ru': 'Выберите роль, которую вы желаете добавить пользователю',
            'en': 'Select the role you want to add to the user'
        }
    },
    'StatesEditorRolesRemove': {
        'attach_contact': {
            'ru': 'Пришлите контакт пользователя в приложении',
            'en': 'Send the user contact in the app'
        },
        'choose_role_current': {
            'ru': 'Выберите роль, которую вы желаете убрать у пользователя',
            'en': 'Select the role you want to remove from the user'
        }
    }
}
