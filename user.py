from storage import StorageUsers
import exceptions


class User:
    '''
    A class to represent a user.

    Upon initialization, it creates a new user with the specified data or uses data from persistent 
    storage if the user ID is found.
    '''

    def __init__(self, stg_users: StorageUsers, user_id: int, user_language: str) -> None:
        self.user_id = user_id

        try:
            user_data = stg_users.get_user(user_id)
            self.user_language = user_data.get('user_language', user_language)

        except exceptions.UserNotFoundError:
            self.user_language = user_language
