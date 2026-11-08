"""set price precision

Revision ID: a0d2f63c4b69
Revises: 6ebc3a790f0c
Create Date: 2026-11-08 10:00:30.130433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0d2f63c4b69'
down_revision: Union[str, Sequence[str], None] = '6ebc3a790f0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "product",
        "current_price",
        existing_type=sa.Numeric(),
        type_=sa.Numeric(precision=10, scale=2),
        existing_nullable=False
    )

    op.alter_column(
        "product",
        "target_price",
        existing_type=sa.Numeric(),
        type_=sa.Numeric(precision=10, scale=2),
        existing_nullable=False
    )


def downgrade() -> None:
    op.alter_column(
        "product",
        "target_price",
        existing_type=sa.Numeric(precision=10, scale=2),
        type_=sa.Numeric(),
        existing_nullable=False
    )

    op.alter_column(
        "product",
        "current_price",
        existing_type=sa.Numeric(precision=10, scale=2),
        type_=sa.Numeric(),
        existing_nullable=False
    )