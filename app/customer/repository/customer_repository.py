
from fastapi import Depends

from app.db.connection import get_connection
from app.db.queries import get_queries


class CustomerRepository:
    def __init__(self, conn, q):
        self.conn = conn
        self.q = q

    def find_all(self) -> list[dict]:
        return self.q.customer.get_all(self.conn)
    
    def find_by_id(self, customer_id: int) -> dict | None:
        return self.q.customer.get_by_id(self.conn, id=customer_id)
    
def get_customer_repository( # q는 쿼리를 게터 메서드로 가져와서 의존성주입받기
                             # conn은 커넥션을 주입받기
        conn = Depends(get_connection),
        q = Depends(get_queries),
) -> CustomerRepository:
    return CustomerRepository(conn, q)