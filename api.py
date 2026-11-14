from fastapi import FastAPI, Depends
from models import Product
from schemas import ProductCreate
from sqlalchemy.orm import Session
from session import get_db
from sqlalchemy import select


app = FastAPI()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    stmt = select(Product)
    products = db.execute(stmt).scalars().all()
    return products

@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(
        name=product.name,
        current_price=product.current_price,
        target_price=product.target_price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {
     "message": "Product received","id": db_product.id, "name": db_product.name
}