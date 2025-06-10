"""add currencies

Revision ID: b8171dd50a04
Revises: 755d04011b62

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b8171dd50a04"
down_revision: Union[str, None] = "755d04011b62"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    currency_table = sa.table(
        "currencies",
        sa.column("code", sa.String),
        sa.column("id", sa.Integer),
    )

    op.bulk_insert(
        currency_table,
        [
            {"code": "CAD", "id": 1},
            {"code": "USD", "id": 2},
            {"code": "EUR", "id": 3},
            {"code": "UAH", "id": 4},
        ],
    )


def downgrade() -> None:
    op.execute("TRUNCATE TABLE currencies;")
