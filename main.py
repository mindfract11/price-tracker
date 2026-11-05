from session import SessionLocal
from decimal import Decimal
from crud import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product_target_price,
    delete_product_by_id
)

session = SessionLocal()

try:
    print("=== STEP 1: Creating initial product ===")
    p1 = create_product(session, "Product 1", Decimal("1000.0"), Decimal("900.0"), "http://link1")
    print(f"Product created successfully with ID: {p1.id}")

    print("\n=== STEP 2: Updating target price ===")
    updated = update_product_target_price(session, product_id=p1.id, new_price=Decimal("1100.0"))
    if updated:
        print(f"New target price for ID {p1.id} is: {updated.target_price}")

    print("\n=== STEP 3: Deleting the product ===")
    if delete_product_by_id(session, product_id=p1.id):
        print(f"Product with ID {p1.id} has been deleted.")

        if get_product_by_id(session, p1.id) is None:
            print("Database check === The record is indeed missing.")

    print("\n=== STEP 4: Creating an empty product and fetching the list ===")
    create_product(session, name="test_product", current_price=Decimal("1500.0"), target_price=Decimal("1200.0"), url="https://example.com/product-1")

    all_products = get_all_products(session)
    print("--------- Products ---------")
    for p in all_products:
        product_name = p.name if p.name else "No Name"
        print(f"ID: {p.id} | Name: {product_name} | Price: {p.current_price}")

finally:
    session.close()
    print("\nSession successfully closed in finally block.")
