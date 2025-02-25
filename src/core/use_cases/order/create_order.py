from src.infrastructure.repositories.order_repository import OrderRepository


class CreateOrderUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_data):
        if not order_data["items"]:
            raise ValueError("Order must contain items")
        return self.repository.save(order_data)
