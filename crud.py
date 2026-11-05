from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from models import Product
from decimal import Decimal

def create_product(session: Session, name: str, current_price: Decimal, target_price: Decimal, url: str) -> Product:
    if not name or not name.strip():
        raise ValueError("Title cannot be empty")

    if current_price < 0:
        raise ValueError("current_price cannot be negative")

    if target_price < 0:
        raise ValueError("target_price cannot be negative")
    try:
        new_product = Product(name=name, current_price=current_price, target_price=target_price, url=url)
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
        return new_product
    except (ValueError, IntegrityError):
        session.rollback()
        raise

def get_all_products(session: Session) -> list[Product]:
    return list(session.scalars(select(Product)).all())

def get_product_by_id(session: Session, product_id: int) -> Product | None:
    return session.get(Product, product_id)

def update_product_target_price(session: Session, product_id: int, new_price: Decimal) -> Product | None:
    if new_price < 0:
        raise ValueError("new_price cannot be negative")
    product = session.get(Product, product_id)
    if product:
        try:
            product.target_price = new_price
            session.commit()
            session.refresh(product)
            return product
        except (ValueError, IntegrityError):
            session.rollback()
            raise
    return None

def delete_product_by_id(session: Session, product_id: int) -> bool:
    product = session.get(Product, product_id)
    if product:
        try:
            session.delete(product)
            session.commit()
            return True
        except (ValueError, IntegrityError):
            session.rollback()
            raise
    return False
