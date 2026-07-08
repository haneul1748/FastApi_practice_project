from fastapi import APIRouter

from app.api.routes import health
from app.customer.controller import customer_controller

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(customer_controller.router) # customer
