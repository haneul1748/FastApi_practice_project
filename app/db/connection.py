import pymysql
from pymysql.connections import Connection

from app.core.config import settings

def get_connection() -> Connection:
    """MySQL 커넥션 하나를 새로 만들어서 반환."""
    return pymysql.connect(
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor, # MyBatis 느낌의 핵심으로 { "id" : 1 , "name" : "홍길동" }
        # 처럼 컬럼명 - 값 딕셔너리로 돌려줌 이거 안할시 -> (1, "홍길동") 이런식으로 튜플로 나옴
    )
