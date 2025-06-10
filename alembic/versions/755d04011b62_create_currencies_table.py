"""create currencies table

Revision ID: 755d04011b62

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "755d04011b62"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "currencies",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("code", sa.Unicode(3), nullable=False),
        mysql_charset="utf8",
        mysql_collate="utf8_unicode_ci",
    )


def downgrade():
    op.drop_table("currencies")
    pass
