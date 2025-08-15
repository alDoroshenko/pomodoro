class UserNotFoundException(Exception):
    detail = "User not found"


class UserNotCorrectPasswordException(Exception):
    detail = "Wrong password"


class TokenExpired(Exception):
    detail = 'Token Expired'


class TokenNotCorrect(Exception):
    detail = 'Token Not Correct'


class TaskNotFound(Exception):
    detail = 'Task Not Found'
