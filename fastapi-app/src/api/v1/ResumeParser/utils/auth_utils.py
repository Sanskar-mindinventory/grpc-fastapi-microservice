from fastapi import Depends, HTTPException, Header, status
import grpc
from src.api.v1.ResumeParser.server_files.user_service_pb2 import TokenRequest
from src.api.v1.ResumeParser.server_files.user_service_pb2_grpc import UserServiceStub 

def create_channel_and_client():
    channel = grpc.insecure_channel("localhost:50051")
    client = UserServiceStub(channel)
    return client


def verify_token(access_token: str = Header()):
    client = create_channel_and_client()
    request = TokenRequest(access_token=access_token)
    response = client.ValidateToken(request)
    if response.token_status:
        return response
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Token is expired or user credentials are not matching ====== ERROR FROM GRPC {response.message}')