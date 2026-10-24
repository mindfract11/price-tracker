import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()
DB_URL = (f"postgresql+psycopg://{os.getenv('DB_USER')}:"
          f"{os.getenv('DB_PASSWORD')}"
          f"@{os.getenv('DB_HOST')}:"
          f"{os.getenv('DB_PORT')}"
          f"/{os.getenv('DB_NAME')}"
)
engine=create_engine(DB_URL, echo=True)
