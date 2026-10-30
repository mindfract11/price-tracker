from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from database import engine
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
def get_db():
    session = SessionLocal()
    try:
        # "CRUD"
        pass
    finally:
        session.close()
