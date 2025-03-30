'''
This is a module for retrieving text that is sent in a dialogue with the user when they are editing the bot.
'''


def get_message(callback_data: str) -> str:
    '''A function to get a message from callback_messages using callback_data.'''

    _, *callback_keys = callback_data.split(':')
    index = 0

    def recursion(callback_messages: dict, callback_key: str) -> str:
        nonlocal index

        result = callback_messages[callback_key]

        if isinstance(result, str):
            return result
        elif isinstance(result, dict):
            index += 1
            return recursion(result, callback_keys[index])

    return recursion(callback_messages, callback_keys[0])


callback_messages = {}
