"""add fetchers

Revision ID: 192f3aeb6420
Revises: b1077370bb2d

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "192f3aeb6420"
down_revision: Union[str, None] = "b1077370bb2d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    fetchers_table = sa.table(
        "fetchers",
        sa.column("name", sa.String),
        sa.column("id", sa.Integer),
    )

    op.bulk_insert(
        fetchers_table,
        [
            {"name": "Frankfurter", "id": 1},
        ],
    )


def downgrade() -> None:
    op.execute("TRUNCATE TABLE fetchers;")
