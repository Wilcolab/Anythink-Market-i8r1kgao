import pathlib

import aiosql

queries = aiosql.from_path(pathlib.Path(__file__).parent / "queries/sql", "asyncpg")


for _ in range(100):
    queries.create_new_user
    queries.create_new_comment
    queries.create_new_item
