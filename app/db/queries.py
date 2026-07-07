import aiosql

queries = aiosql.from_path("sql/mappers/", "pymysql", encoding="utf-8")