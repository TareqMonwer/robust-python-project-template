from fastapi import APIRouter, Depends, HTTPException
from domain.constants import ORDER_CREATION_FAILED, ORDER_CREATION_SUCCESS
from domain.schema.oder_dto import OrderDTO
from domain.schema.order_response import OrderCreatedResponse
from src.core.use_cases.create_order import CreateOrderUseCase
from src.infrastructure.repositories.order_repository import OrderRepository
from src.infrastructure.database.mongo_client import get_mongo_client

router = APIRouter()


@router.post("/orders/")
async def create_order(
    order: OrderDTO, mongo_client=Depends(get_mongo_client)
):
    order_repo = OrderRepository(mongo_client)
    use_case = CreateOrderUseCase(order_repo)
    result = use_case.execute(dict(order))

    if not result:
        raise HTTPException(status_code=400, detail=ORDER_CREATION_FAILED)
    return OrderCreatedResponse(
        message=ORDER_CREATION_SUCCESS, order_id=result
    )
