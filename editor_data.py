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
            'text_sys_name': {
                'ru': 'Введите системное имя для текста',
                'en': 'Enter a system name for the text'
            },            
            'text_ru': {
                'ru': 'Введите текст на русском языке',
                'en': 'Enter text in Russian'
            },
            'text_en': {
                'ru': 'Введите тескт на английском языке',
                'en': 'Enter text in English'
            }
        }
    },
    'confirmation': {
        'ru': 'Подтвердите данные',
        'en': 'Confirm data'
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
            'cnt_next': 'edit_txt'
        },
        'delete_text': {
            'label': {
                'ru': 'Удалить текст',
                'en': 'Delete text'
            },
            'cnt_next': 'del_txt'
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
