from session import SessionLocal
from models import Product
from sqlalchemy import select

session = SessionLocal()

try:
    product_id_to_find = 1
    new_target_price = 1100.00
    product_id_to_delete = 1
    product = session.get(Product, product_id_to_delete)
    product = session.get(Product, product_id_to_find)
    if product:
        print(f"We found a product with name: {product.name}(has been deleted)")
        session.delete(product)
        session.commit()
        print(f"Recorded commit in database")
        deleted_product_check = session.get(Product, product_id_to_delete)
        if deleted_product_check is None:
            print("Database check === The record is indeed missing.")
        else:
            print("Error")

    else:
        print(f"Product with id: {product_id_to_delete} the record does not exist in the database.")

    if product:
        print(f"We found the product, name: {product.name}, price: {product.target_price}")
        product.target_price = new_target_price
        session.commit()
        print("Recorded commit in database")
        session.expire(product)

        updated_product = session.get(Product, product_id_to_find)
        print(f"Database check === New target price: {updated_product.target_price}")
    else:
        print(f"Product ID: {product_id_to_find} no found")
    new_product = Product(
        name="",
        current_price=1500.00,
        target_price=1200.00,
        url=""
    )
    session.add(new_product)
    session.commit()
    query = select(Product)
    products = session.scalars(query).all()
    print("--------- Products ---------")
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.current_price}")

finally:
    session.close()
