"""create currency_rates table

Revision ID: b1077370bb2d
Revises: 089364fcefcf

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b1077370bb2d"
down_revision: Union[str, None] = "089364fcefcf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = ["089364fcefcf"]  # create fetchers


def upgrade():
    op.create_table(
        "currency_rates",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("fetcher_id", sa.Integer, nullable=False),
        sa.Column("base_currency_id", sa.Integer(), nullable=False),
        sa.Column("target_currency_id", sa.Integer(), nullable=False),
        sa.Column("rate", sa.Numeric(18, 10), nullable=False),
        sa.Column("fetched_at", sa.DateTime(), nullable=False, index=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")
        ),
        sa.UniqueConstraint(
            "fetcher_id",
            "base_currency_id",
            "target_currency_id",
            "fetched_at",
            name="uq_rate",
        ),
        sa.Index("idx_base_target", "base_currency_id", "target_currency_id"),
        sa.ForeignKeyConstraint(
            ["fetcher_id"],
            ["fetchers.id"],
            name="fk_fetcher_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["base_currency_id"],
            ["currencies.id"],
            name="fk_base_currency",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["target_currency_id"],
            ["currencies.id"],
            name="fk_target_currency",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
        mysql_charset="utf8",
        mysql_collate="utf8_unicode_ci",
    )


def downgrade():
    op.drop_table("currency_rates")
