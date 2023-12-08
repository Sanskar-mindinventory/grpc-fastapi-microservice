from database.database import get_db
from src.api.v1.UserAuthentication.server_files import user_service_pb2, user_service_pb2_grpc
from src.api.v1.UserAuthentication.services.user_services import UserServices as us


db = get_db()

class UserServices(user_service_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        user = us.register(request=request, db_session=db)
        return user_service_pb2.CreateUserResponse(user_id=str(user.get('data').user_id), username=user.get('data').username, email=user.get('data').email)

    def AuthenticateUser(self, request, context):
        user_token = us.login(request=request, db_session=db)
        return user_service_pb2.LoginUserResponse(access_token=user_token.get('access_token'), token_type=user_token.get('token_type'))
    
    def ValidateToken(self, request, context):
        user_token = us.validate_token(access_token=request.access_token, db_session=db)
        if user_token.get('active'):
            user = user_service_pb2.User()
            user_obj = user_token.get('user')
            user.user_id = user_obj.user_id
            user.username = user_obj.username
            user.email = user_obj.email        
            return user_service_pb2.TokenValidationResponse(user=user, token_status=user_token.get('active'))
        return user_service_pb2.TokenValidationResponse(message=user_token.get('message'), token_status=user_token.get('active'))