from database import engine
from sqlalchemy import text
with engine.connect() as conn:
    query = text("SELECT 1")
    result = conn.execute(query)
    print(result.scalar_one())