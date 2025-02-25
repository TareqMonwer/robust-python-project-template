from pydantic import BaseModel


class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float


class OrderDTO(BaseModel):
    id: str
    user_id: str
    items: list[OrderItem]
