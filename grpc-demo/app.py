"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import grpc
from src.api.v1.UserAuthentication.server_files import user_service_pb2_grpc
from src.api.v1.UserAuthentication.views.user_views import UserServices





def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServices(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()