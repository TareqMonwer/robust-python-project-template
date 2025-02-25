import grpc
from src.core.protos import order_pb2, order_pb2_grpc
from src.domain.use_cases.create_order import CreateOrderUseCase
from src.infrastructure.databases.mongo_client import get_mongo_client
from src.domain.repositories.order_repository import OrderRepository
from src.domain.constants import ORDER_CREATION_SUCCESS, ORDER_CREATION_FAILED


class OrderService(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        try:
            mongo_client = get_mongo_client()
            order_repo = OrderRepository(mongo_client)
            use_case = CreateOrderUseCase(order_repo)

            order_data = {
                "customer_id": request.customer_id,
                "product_ids": list(request.product_ids),
                "total_price": request.total_price,
            }

            order_id = use_case.execute(order_data)

            if not order_id:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(ORDER_CREATION_FAILED)
                return order_pb2.CreateOrderResponse(
                    order_id="", message=ORDER_CREATION_FAILED
                )

            return order_pb2.CreateOrderResponse(
                order_id=order_id, message=ORDER_CREATION_SUCCESS
            )

        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return order_pb2.CreateOrderResponse(
                order_id="", message="Internal Server Error"
            )
