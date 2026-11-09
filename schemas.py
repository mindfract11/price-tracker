from decimal import Decimal

from pydantic import BaseModel,Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length = 1,description = "Product Name")
    current_price: Decimal = Field(..., ge=0,description = "Current Price")
    target_price: Decimal = Field(..., ge=0,description = "Target Price")

