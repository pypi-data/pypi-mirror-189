# type: ignore
"""content

Revision ID: bf20242a238f
Revises: 7c1c6e101059
Create Date: 2021-06-20 12:42:35.578665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bf20242a238f"
down_revision = "7c1c6e101059"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("medias", schema=None) as batch_op:
        batch_op.add_column(sa.Column("api_type", sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("medias", schema=None) as batch_op:
        batch_op.drop_column("api_type")

    # ### end Alembic commands ###
