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


class StorageViewsError(StorageError):
    '''The parent class for all exceptions related to views storage'''

    pass

class ViewNotFoundError(StorageViewsError):
    '''Exception raised when a view name is not found in persistent storage'''

    def __init__(self, view_name: str) -> None:
        self.view_name = view_name
        self.error_message = f'View with name {view_name} is not found'
        super().__init__(self.error_message)
        