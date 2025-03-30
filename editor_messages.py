'''
This is a module for retrieving text that is sent in a dialogue with the user when they are editing the bot.
'''


def get_message(callback_data: str, message_language: str) -> str:
    '''A function to get a message from callback_messages using callback_data.'''

    _, *callback_keys = callback_data.split(':')
    index = 0

    def recursion(callback_messages: dict, callback_key: str) -> str:
        nonlocal index

        result = callback_messages[callback_key]

        try:
            return result[message_language]
        except KeyError:
            index += 1
            return recursion(result, callback_keys[index])

    return recursion(CALLBACK_MESSAGES, callback_keys[0])


CALLBACK_MESSAGES = {
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
    }
}
