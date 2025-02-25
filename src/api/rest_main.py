from fastapi import FastAPI
from src.api import router


app = FastAPI()

app.include_router(router, prefix="/my-service-suffix")
