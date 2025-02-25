from infrastructure.repositories.order_repository import OrderRepository


class GetOrderQuery:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id):
        return self.repository.get_order(order_id)
