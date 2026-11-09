from fastapi import FastAPI
from schemas import ProductCreate


app = FastAPI()

@app.get("/products")
async def get_products():
    return {"message": "Products List" }

@app.post("/products")
async def create_product(product: ProductCreate):
    return {
     "message": "Product received", "name": product.name
}