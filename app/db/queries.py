import aiosql

queries = aiosql.from_path("sql/mappers/", "pymysql", encoding="utf-8")

def get_queries():
    return queries