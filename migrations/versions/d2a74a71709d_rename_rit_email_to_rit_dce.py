"""rename rit_email to rit_dce

Revision ID: d2a74a71709d
Revises: 9c1fa448d2c3
Create Date: 2021-08-18 14:12:13.730727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d2a74a71709d"
down_revision = "9c1fa448d2c3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "memberships", sa.Column("rit_dce", sa.String(length=32), nullable=False)
    )
    op.drop_column("memberships", "rit_email")
    op.add_column(
        "officers", sa.Column("rit_dce", sa.String(length=32), nullable=False)
    )
    op.drop_column("officers", "rit_email")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "officers", sa.Column("rit_email", sa.VARCHAR(length=32), nullable=False)
    )
    op.drop_column("officers", "rit_dce")
    op.add_column(
        "memberships", sa.Column("rit_email", sa.VARCHAR(length=32), nullable=False)
    )
    op.drop_column("memberships", "rit_dce")
    # ### end Alembic commands ###
