from src.api.v1.UserAuthentication.utils.custom_exceptions import CredentialsException, InActiveUserException
from src.api.v1.UserAuthentication.utils.hash_utils import Hasher
from src.api.v1.UserAuthentication.utils.token_utils import Token
from src.api.v1.UserAuthentication.models.user_models import User
from src.api.v1.UserAuthentication.utils.auth_utils import get_current_active_user, get_current_user
from src.api.v1.UserAuthentication.utils.constants import ERR_USERNAME_EXISTS, ERR_EMAIL_EXISTS, ERR_SQLALCHEMY_ERROR, \
    MSG_USER_REGISTER_SUCCESSFULLY, ERR_INVALID_USERNAME, ERR_INVALID_PASSWORD, MSG_LOG_IN_SUCCESSFULLY, \
    ERR_INVALID_TOKEN, MSG_RETRIEVE_USER, INVALID_CREDENTIALS, TEST_API_RESPONSE_DATA, SUCCESS_EXECUTED
from src.api.v1.UserAuthentication.utils.response_utils import Response


class UserServices:

    @staticmethod
    def register(request, db_session):
        """
        This function is used for registration of user.
        :param request: request body
        :param db_session: Database Session
        :return: registered User.
        """
        username = request.username
        email = request.email
        if User.get_user_by_email(db_session, email):
            return Response(status_code=400,
                            message=ERR_EMAIL_EXISTS.format(email)).send_error_response()
        if User.get_user_by_username(db_session, username):
            return Response(status_code=400,
                            message=ERR_USERNAME_EXISTS.format(username)).send_error_response()
        is_saved, data_or_error = User.save(db_session, {"username":username, "password":request.password, "email":email})
        if is_saved is False:
            return Response(status_code=400,
                            message=ERR_SQLALCHEMY_ERROR.format(data_or_error)).send_error_response()
        return Response(status_code=201,
                        message=MSG_USER_REGISTER_SUCCESSFULLY.format(username), data=data_or_error). \
            send_success_response()

    @staticmethod
    def login(request, db_session):
        """
        This function is used by the login API.
        :param request: request body
        :param db_session: Database Session
        :return: access token and type of token
        """
        stored_user = User.get_user_by_username(db_session, request.username)
        if stored_user is None or not Hasher.verify_password(request.password, stored_user.password):
            raise Response(status_code=401, message=INVALID_CREDENTIALS).send_error_response()
        access_token = Token().create_access_token(
            data={"sub": stored_user.username})
        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    def get_token(form_data, db_session):
        """
        This function is used by the Authorize button of the OpenAPI doc.
        :param form_data: Authentication Form
        :param db_session: Database Session
        :return: access token and type of token
        """
        stored_user = User.get_user_by_username(db_session, form_data.username)
        if stored_user is None or not Hasher.verify_password(form_data.password, stored_user.password):
            raise Response(status_code=401, message=INVALID_CREDENTIALS).send_error_response()
        access_token = Token().create_access_token(
            data={"sub": stored_user.username}
        )
        return {"access_token": access_token, "token_type": 'bearer'}

    @staticmethod
    def test_api(current_user):
        """
        This is a testing function
        :param current_user: Current User
        :return: response for testing API
        """
        return Response(status_code=200,
                        message=SUCCESS_EXECUTED.format(username=current_user.username),
                        data=TEST_API_RESPONSE_DATA)

    @staticmethod
    def validate_token(db_session, access_token):
        try:
            user = get_current_user(db=db_session, token=access_token)
            if user:
                user_status =  get_current_active_user(current_user=user)
        except CredentialsException as error:
            print(f"Error - CredentialsException : {error}")
            return {"message": "Credentials are Incorrect", "active":False}
        except InActiveUserException as err: 
            print(f"Error - InActiveUserException : {err}")
            return {"message": "User is inacitve", "active":False}
        return {"user":user, "active": True}