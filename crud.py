from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Product

def create_product(session: Session, name: str, current_price: float, target_price: float, url: str) -> Product:
    new_product = Product(name=name, current_price=current_price, target_price=target_price, url=url)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product

def get_all_products(session: Session) -> list[Product]:
    return list(session.scalars(select(Product)).all())

def get_product_by_id(session: Session, product_id: int) -> Product | None:
    return session.get(Product, product_id)

def update_product_target_price(session: Session, product_id: int, new_price: float) -> Product | None:
    product = session.get(Product, product_id)
    if product:
        product.target_price = new_price
        session.commit()
        session.expire(product)
        return session.get(Product, product_id)
    return None

def delete_product_by_id(session: Session, product_id: int) -> bool:
    product = session.get(Product, product_id)
    if product:
        session.delete(product)
        session.commit()
        return True
    return False
