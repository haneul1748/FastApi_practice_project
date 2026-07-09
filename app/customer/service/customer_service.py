from fastapi import Depends, HTTPException

from app.customer.dto.customer_dto import CustomerResponse
from app.customer.repository.customer_repository import (CustomerRepository, get_customer_repository,)

class CustomerService:

    def __init__(self, repo: CustomerRepository): # repository 주입
        self.customerRepository = repo

    def get_all(self) -> list[CustomerResponse]:
        rows = self.customerRepository.find_all()
        return [CustomerResponse(**row) for row in rows]
    
    def get_by_id(self, customer_id: int) -> CustomerResponse | None:
        row = self.customerRepository.find_by_id(customer_id)
        if row is None:
            return HTTPException(status_code=404, detail="customer not found")
        return CustomerResponse(**row)

def get_customer_service(
        repo: CustomerRepository = Depends(get_customer_repository),
) -> CustomerService:
    return CustomerService(repo)