"""add exchangerate fetcher

Revision ID: eb1ee3605f02
Revises: 192f3aeb6420

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "eb1ee3605f02"
down_revision: Union[str, None] = "192f3aeb6420"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    fetchers_table = sa.table(
        "fetchers",
        sa.column("name", sa.String),
        sa.column("id", sa.Integer),
    )

    op.bulk_insert(
        fetchers_table,
        [
            {"name": "Exchangerate", "id": 2},
        ],
    )


def downgrade():
    op.execute("DELETE FROM fetchers WHERE id=2;")
