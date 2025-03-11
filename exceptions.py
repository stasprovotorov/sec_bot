class StorageError(Exception):
    '''The base class for all exceptions related to storage'''
    pass


class StorageUsersError(StorageError):
    '''The parent class for all exceptions related to users storage'''
    pass


class UserNotFoundError(StorageUsersError):
    '''Exception raised when a user is not found in persistent storage'''
    def __init__(self, user_id: int) -> None:
        super().__init__(f'User with ID {user_id} is not found')


class UserAlreadyExistsError(StorageUsersError):
    '''Exception raised when a user already exists in persistent storage'''    
    def __init__(self, user_id: int) -> None:
        super().__init__(f'User with ID {user_id} already exists')


class StorageViewsError(StorageError):
    '''The parent class for all exceptions related to views storage'''
    pass

class ViewNotFoundError(StorageViewsError):
    '''Exception raised when a view name is not found in persistent storage'''
    def __init__(self, view_name: str) -> None:
        super().__init__(f'View with name {view_name} is not found')


class ViewAlreadyExistsError(StorageViewsError):
    '''Exception raised when a view with the given name already exists in persistent storage'''
    def __init__(self, view_name: str) -> None:
        super().__init__(f'View with name {view_name} already exists')


class StorageTextsError(StorageError):
    '''The parent class for all exceptions related to texts storage'''
    pass


class TextNotFoundError(StorageTextsError):
    '''Exception raised when a text name is not found in persistent storage'''
    def __init__(self, text_name):
        super().__init__(f'View with name {text_name} is not found')
        