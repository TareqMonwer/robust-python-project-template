from fastapi import APIRouter
from src.api.routes.orders import router as orders_routes


router = APIRouter()

router.include_router(
    orders_routes, prefix="orders", tags=["orders", "purchases"]
)
