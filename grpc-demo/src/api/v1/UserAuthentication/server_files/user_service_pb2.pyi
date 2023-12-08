from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserRequest(_message.Message):
    __slots__ = ["username", "password", "email"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    email: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ["user_id", "username", "email"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    username: str
    email: str
    def __init__(self, user_id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class LoginUserRequest(_message.Message):
    __slots__ = ["username", "password"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginUserResponse(_message.Message):
    __slots__ = ["access_token", "token_type"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ...) -> None: ...

class TokenRequest(_message.Message):
    __slots__ = ["access_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["username", "user_id", "email"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    username: str
    user_id: int
    email: str
    def __init__(self, username: _Optional[str] = ..., user_id: _Optional[int] = ..., email: _Optional[str] = ...) -> None: ...

class TokenValidationResponse(_message.Message):
    __slots__ = ["user", "message", "token_status"]
    USER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_STATUS_FIELD_NUMBER: _ClassVar[int]
    user: User
    message: str
    token_status: bool
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., message: _Optional[str] = ..., token_status: bool = ...) -> None: ...
