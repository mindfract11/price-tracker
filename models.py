from decimal import Decimal
from sqlalchemy import BigInteger,Numeric,Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    current_price: Mapped[Decimal] = mapped_column(Numeric)
    target_price: Mapped[Decimal] = mapped_column(Numeric)
    url: Mapped[str | None] = mapped_column(Text, nullable=True)