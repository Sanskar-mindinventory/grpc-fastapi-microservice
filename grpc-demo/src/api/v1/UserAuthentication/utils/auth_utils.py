from jose import jwt, JWTError
from sqlalchemy.orm import Session
from src.api.v1.UserAuthentication.models.user_models import User
from src.api.v1.UserAuthentication.schemas.user_schemas import UserResponseSchema
from database.database import get_db
from config.config import JWTSettings
from src.api.v1.UserAuthentication.utils.custom_exceptions import CredentialsException, InActiveUserException

secret_key = JWTSettings().authjwt_secret_key
algorithm = JWTSettings().JWT_ALGORITHM


def get_current_user(db, token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise CredentialsException("There is nothing inside payload. It might be possible that token is expired already.")
    except JWTError as error:
        raise CredentialsException(f"Something went wrong - JWTError : {error}")
    user = User.get_user_by_username(db_session=db, username=username)
    if user is None:
        raise CredentialsException(f"There is no user in database with same username {username}")
    return user


def get_current_active_user(current_user):
    if current_user.disabled:
        raise InActiveUserException("User is disabled")        
    return current_user
