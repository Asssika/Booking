from fastapi import APIRouter, HTTPException, status, Response, Depends


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code,
                         detail=self.detail)


class UserAlreadyExistException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exist"


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Email or Password"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is run of time"


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token doesnt exist"


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class UserIsNotExistException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User doesnt exist"


class RoomCannotBeBooked(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No free rooms left"
