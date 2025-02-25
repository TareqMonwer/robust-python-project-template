from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float


class Order(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
