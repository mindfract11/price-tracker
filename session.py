from sqlalchemy.orm import Session
from typing import Generator
from sqlalchemy.orm import sessionmaker
from database import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
def get_db() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
