from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from src.api.v1.UserAuthentication.validations.user_validations import username_validation, password_validation


class UserRegistrationRequestSchema(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra='forbid')
    username: str
    password: str
    email: EmailStr

    # validators
    @field_validator('username')
    def username_validation_option(cls, value):
        return username_validation(username=value)

    @field_validator('password')
    def password_validation_option(cls, value):
        return password_validation(password=value)


class UserLoginRequestSchema(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra='forbid')
    username: str
    password: str

    # validators
    @field_validator('username')
    def username_validation_option(cls, value):
        return username_validation(username=value)


class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    username: str
    email: str


