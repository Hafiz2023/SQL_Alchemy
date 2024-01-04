from dotenv import load_dotenv
from sqlalchemy import create_engine,text

import os 

load_dotenv()

key = os.getenv("db_key")

conn_str = f'{key}'

engine = create_engine(conn_str)



with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM my_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")