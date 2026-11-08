"""initial schema

Revision ID: 6ebc3a790f0c
Revises: 
Create Date: 2026-11-07 15:56:03.290033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ebc3a790f0c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("current_price", sa.Numeric(), nullable=False),
        sa.Column("target_price", sa.Numeric(), nullable=False),
        sa.Column("url", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    op.drop_table("product")

