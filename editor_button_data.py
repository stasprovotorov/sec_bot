EDITOR_BUTTON_DATA = {
    'menu': {
        'text': {
            'label': {
                'ru': 'Текст',
                'en': 'Text'
            },
            'callback_data': 'editor:text:action'
        },
        'image': {
            'label': {
                'ru': 'Изображение',
                'en': 'Image'
            },
            'callback_data': 'editor:image:action'
        },
        'button': {
            'label': {
                'ru': 'Кнопка',
                'en': 'Button'
            },
            'callback_data': 'editor:button:action'
        },
        'message': {
            'label': {
                'ru': 'Сообщение',
                'en': 'Message'
            },
            'callback_data': 'editor:message:action'
        },
        'role': {
            'label': {
                'ru': 'Роли',
                'en': 'Roles'
            },
            'callback_data': 'editor:role:action'
        }
    },
    'text': {
        'action': {
            'create': {
                'label': {
                    'ru': 'Создать',
                    'en': 'Create'
                },
                'callback_data': 'editor:text:create' # Callback to StatesEditorTextCreate
            },
            'edit': {
                'label': {
                    'ru': 'Редактировать',
                    'en': 'Edit'
                },
                'callback_data': 'editor:text:edit' # Callback to StatesEditorTextEdit
            },
            'delete': {
                'label': {
                    'ru': 'Удалить',
                    'en': 'Delete'
                },
                'callback_data': 'editor:text:delete' # Callback to StatesEditorTextDelete
            }
        }
    },
    'image': {
        'action': {
            'load': {
                'label': {
                    'ru': 'Загрузить',
                    'en': 'Load'
                },
                'callback_data': 'editor:image:load' # Callback to StatesEditorImageLoad
            },
            'delete': {
                'label': {
                    'ru': 'Удалить',
                    'en': 'Delete'
                },
                'callback_data': 'editor:image:delete' # Callback to StatesEditorImageDelete
            }
        }
    },
    'button': {
        'action': {
            'create': {
                'label': {
                    'ru': 'Создать',
                    'en': 'Create'
                },
                'callback_data': 'editor:button:create' # Callback to StatesEditorButtonCreate
            },
            'edit': {
                'label': {
                    'ru': 'Редактировать',
                    'en': 'Edit'
                },
                'callback_data': 'editor:button:edit'
            },
            'delete': {
                'label': {
                    'ru': 'Удалить',
                    'en': 'Delete'
                },
                'callback_data': 'editor:button:delete' # Callback to StatesEditorButtonDelete
            }
        },
        'edit': {
            'label': {
                'label': {
                    'ru': 'Лейбл',
                    'en': 'Label'
                },
                'callback_data': 'editor:button:edit:label' # Callback to StatesEditorButtonEditLabel
            },
            'message_call': {
                'label': {
                    'ru': 'Сообщение вызова',
                    'en': 'Message call'
                },
                'callback_data': 'editor:button:edit:message_call' # Callback to StatesEditorButtonEditMessageCall
            }
        }
    },
    'message': {
        'action': {
            'create': {
                'label': {
                    'ru': 'Создать',
                    'en': 'Create'
                },
                'callback_data': 'editor:message:create' # Callback to StatesEditorMessageCreate
            },
            'edit': {
                'label': {
                    'ru': 'Редактировать',
                    'en': 'Edit'
                },
                'callback_data': 'editor:message:edit:component'
            },
            'delete': {
                'label': {
                    'ru': 'Удалить',
                    'en': 'Delete'
                },
                'callback_data': 'editor:message:delete' # Callback to StatesEditorMessageDelete
            }
        },
        'edit': {
            'component': {
                'text': {
                    'label': {
                        'ru': 'Текст',
                        'en': 'Text'
                    },
                    'callback_data': 'editor:message:edit:text' # Callback to StatesEditorMessageEditTextReplace
                },
                'button': {
                    'label': {
                        'ru': 'Кнопка',
                        'en': 'Button'
                    },
                    'callback_data': 'editor:message:edit:button'
                },
                'image': {
                    'label': {
                        'ru': 'Изображение',
                        'en': 'Image'
                    },
                    'callback_data': 'editor:message:edit:image'
                }
            },
            'button': {
                'add': {
                    'label': {
                        'ru': 'Добавить',
                        'en': 'Add'
                    },
                    'callback_data': 'editor:message:edit:button:add' # Callback to StatesEditorMessageEditButtonAdd
                },
                'replace': {
                    'label': {
                        'ru': 'Заменить',
                        'en': 'Replace'
                    },
                    'callback_data': 'editor:message:edit:button:replace' # Callback to StatesEditorMessageEditButtonReplace
                },
                'delete': {
                    'label': {
                        'ru': 'Удалить',
                        'en': 'Delete'
                    },
                    'callback_data': 'editor:message:edit:button:delete' # Callback to StatesEditorMessageEditButtonDelete
                }
            },
            'image': {
                'add': {
                    'label': {
                        'ru': 'Добавить',
                        'en': 'Add'
                    },
                    'callback_data': 'editor:message:edit:image:add' # Callback to StatesEditorMessageEditImageAdd
                },
                'replace': {
                    'label': {
                        'ru': 'Заменить',
                        'en': 'Replace'
                    },
                    'callback_data': 'editor:message:edit:image:replace' # Callback to StatesEditorMessageEditImageReplace
                },
                'delete': {
                    'label': {
                        'ru': 'Удалить',
                        'en': 'Delete'
                    },
                    'callback_data': 'editor:message:edit:image:delete' # Callback to StatesEditorMessageEditImageDelete
                }
            }
        }
    },
    'role': {
        'action': {
            'assing': {
                'label': {
                    'ru': 'Назначить',
                    'en': 'Assing'
                },
                'callback_data': 'editor:role:assing' # Callback to StatesEditorRolesAssign
            },
            'remove': {
                'label': {
                    'ru': 'Убрать',
                    'en': 'Remove'
                },
                'callback_data': 'editor:role:remove' # Callback to StatesEditorRolesRemove
            }
        }
    }
}
