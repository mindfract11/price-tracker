import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,text
load_dotenv()
DB_URL = (f"postgresql+psycopg://{os.getenv('DB_USER')}:"
          f"{os.getenv('DB_PASSWORD')}"
          f"@{os.getenv('DB_HOST')}:"
          f"{os.getenv('DB_PORT')}"
          f"/{os.getenv('DB_NAME')}"
)
engine=create_engine(DB_URL, echo=True)
with engine.connect() as conn:
    query = text("SELECT 1")
    result = conn.execute(query)
    print(result.scalar_one())