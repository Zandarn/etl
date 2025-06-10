"""create fetchers table

Revision ID: 089364fcefcf
Revises: b8171dd50a04

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "089364fcefcf"
down_revision: Union[str, None] = "b8171dd50a04"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "fetchers",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.Unicode(32), nullable=False),
        mysql_charset="utf8",
        mysql_collate="utf8_unicode_ci",
    )


def downgrade():
    op.drop_table("fetchers")
    pass
