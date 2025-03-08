class StorageError(Exception):
    '''The base class for all exceptions related to storage'''

    pass


class StorageUsersError(StorageError):
    '''The parent class for all exceptions related to users storage'''

    pass


class UserNotFoundError(StorageUsersError):
    '''Exception raised when a user is not found in persistent storage'''

    def __init__(self, user_id):
        self.user_id = user_id
        self.error_message = f'User with ID {self.user_id} is not found'
        super().__init__(self.error_message)


class UserAlreadyExistsError(StorageUsersError):
    '''Exception raised when a user already exists in persistent storage'''
    
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        self.error_message = f'User with ID {self.user_id} already exists'
        super().__init__(self.error_message)
