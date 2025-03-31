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
        'ru': None,
        'en': None
    },
    'text': {
        'action': {
            'ru': None,
            'en': None
        },
        'create': {
            'ru': None,
            'en': None
        },
        'edit': {
            'ru': None,
            'en': None
        },
        'delete': {
            'ru': None,
            'en': None
        }
    },
    'image': {
        'action': {
            'ru': None,
            'en': None
        },
        'load': {
            'ru': None,
            'en': None
        },
        'delete': {
            'ru': None,
            'en': None
        }
    },
    'button': {
        'action': {
            'ru': None,
            'en': None
        },
        'create': {
            'ru': None,
            'en': None
        },
        'edit': {
            'component': {
                'ru': None,
                'en': None
            },
            'label': {
                'ru': None,
                'en': None
            },
            'message': {
                'ru': None,
                'en': None
            }
        },
        'delete': {
            'ru': None,
            'en': None
        }
    },
    'message': {
        'action': {
            'ru': None,
            'en': None
        },
        'create': {
            'ru': None,
            'en': None
        },
        'edit': {
            'component': {
                'ru': None,
                'en': None
            },
            'text': {
                'ru': None,
                'en': None
            },
            'button': {
                'action': {
                    'ru': None,
                    'en': None
                },
                'add': {
                    'ru': None,
                    'en': None
                },
                'replace': {
                    'ru': None,
                    'en': None
                },
                'delete': {
                    'ru': None,
                    'en': None
                }
            },
            'image': {
                'action': {
                    'ru': None,
                    'en': None
                },
                'add': {
                    'ru': None,
                    'en': None
                },
                'replace': {
                    'ru': None,
                    'en': None
                },
                'delete': {
                    'ru': None,
                    'en': None
                }
            }
        },
        'delete': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorTextCreate': {
        'enter_text_name': {
            'ru': None,
            'en': None
        },
        'enter_text_ru': {
            'ru': None,
            'en': None
        },
        'enter_text_en': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorTextEdit': {
        'choose_text_name': {
            'ru': None,
            'en': None
        },
        'choose_text_language': {
            'ru': None,
            'en': None
        },
        'enter_text': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorTextDelete': {
        'choose_text_name': {
            'ru': None,
            'en': None
        },
        'choose_text_language': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorImageLoad': {
        'enter_image_name': {
            'ru': None,
            'en': None
        },
        'attach_image': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorImageLoad': {
        'choose_image_name': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorButtonCreate': {
        'enter_button_name': {
            'ru': None,
            'en': None
        },
        'enter_button_label_ru': {
            'ru': None,
            'en': None
        },
        'enter_button_label_en': {
            'ru': None,
            'en': None
        },
        'enter_button_message': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorButtonEditLabel': {
        'choose_button_name': {
            'ru': None,
            'en': None
        },
        'choose_button_label_language': {
            'ru': None,
            'en': None
        },
        'enter_button_label': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorButtonEditMessage': {
        'choose_button_name': {
            'ru': None,
            'en': None
        },
        'enter_button_message': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorButtonDelete': {
        'choose_button_name': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageCreate': {
        'enter_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_text_name': {
            'ru': None,
            'en': None
        },
        'choose_message_image_name': {
            'ru': None,
            'en': None
        },
        'choose_message_button_name': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageEditTextReplace': {
        'enter_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_text_name_added': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageEditButtonAdd': {
        'choose_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_button_name_added': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageEditButtonReplace': {
        'choose_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_button_name_current': {
            'ru': None,
            'en': None
        },
        'choose_message_button_name_added': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageEditButtonDelete': {
        'choose_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_button_name': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageEditImageAdd': {
        'choose_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_image_name': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageEditImageReplace': {
        'choose_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_image_name_current': {
            'ru': None,
            'en': None
        },
        'choose_message_image_name_added': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageEditImageDelete': {
        'choose_message_name': {
            'ru': None,
            'en': None
        },
        'choose_message_image_name': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorMessageDelete': {
        'choose_message_name': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorRolesAssign': {
        'attach_contact': {
            'ru': None,
            'en': None
        },
        'choose_role_added': {
            'ru': None,
            'en': None
        }
    },
    'StatesEditorRolesRemove': {
        'attach_contact': {
            'ru': None,
            'en': None
        },
        'choose_role_current': {
            'ru': None,
            'en': None
        }
    }
}
