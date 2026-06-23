from fastapi import HTTPException

class UserAlreadyExists(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="User already exists"
        )


class InvalidCredentials(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Invalid credentials"
        )


class Unauthorized(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Unauthorized"
        )


class TokenExpired(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Token expired"
        )

class InvalidAccount(Exception):
    pass


class InsufficientFunds(Exception):
    pass


class FrozenAccount(Exception):
    pass


class TransferFailed(Exception):
    pass