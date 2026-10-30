from database import engine
from models import Base
from models import Product

Base.metadata.create_all(bind=engine)

