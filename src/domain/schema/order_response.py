from pydantic import BaseModel


class OrderCreatedResponse(BaseModel):
    message: str
    order_id: str
