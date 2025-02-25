import grpc
from concurrent import futures
from src.api.grpc.services.order_service import OrderService
from src.core.protos import order_pb2_grpc
from src.api.grpc.interceptors.logging_interceptor import LoggingInterceptor
from src.api.grpc.interceptors.exception_interceptor import (
    ExceptionInterceptor,
)
from src.core.config import GRPC_PORT


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=[LoggingInterceptor(), ExceptionInterceptor()],
    )

    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)

    server.add_insecure_port(f"[::]:{GRPC_PORT}")
    print(f"🚀 gRPC Server is running on port {GRPC_PORT}...")
    server.start()
    server.wait_for_termination()
