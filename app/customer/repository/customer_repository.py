from pymysql.connections import Connection

from app.db.queries import queries

def find_all(conn: Connection) -> list[dict]:
    """전체 조회"""
    return queries.customer.get_all(conn)

def find_by_id(conn: Connection, customer_id: int) -> dict | None:
    """id로 일치하는 고객 조회 (없으면 None)."""
    return queries.customer.get_by_id(conn, id=customer_id)

