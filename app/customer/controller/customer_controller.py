
from typing import Annotated

from fastapi import APIRouter, Depends

from app.customer.dto.customer_dto import CustomerResponse
from app.customer.service.customer_service import CustomerService, get_customer_service

CustomerServiceDep = Annotated[CustomerService, Depends(get_customer_service)]

router = APIRouter(prefix="/customers", tags=["customer"])

@router.get("", response_model=list[CustomerResponse])
def list_customers(service: CustomerServiceDep):
    return service.get_all()