"""update starting schema

Revision ID: 23dc2b732614
Revises: 
Create Date: 2021-08-30 16:57:21.560517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "23dc2b732614"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "golinks",
        sa.Column("short_link", sa.String(length=64), nullable=False),
        sa.Column("full_link", sa.Text(), nullable=False),
        sa.Column("public", sa.Boolean(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("short_link"),
    )
    op.create_table(
        "memberships",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("rit_dce", sa.String(length=32), nullable=False),
        sa.Column("reason", sa.String(length=256), nullable=False),
        sa.Column("given_by", sa.String(length=32), nullable=False),
        sa.Column("given", sa.DateTime(), nullable=False),
        sa.Column("expires", sa.DateTime(), nullable=False),
        sa.Column("approved", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "officers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("committee", sa.String(length=64), nullable=False),
        sa.Column("rit_dce", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=128), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("bio", sa.Text(), nullable=True),
        sa.Column("is_primary", sa.Boolean(), nullable=True),
        sa.Column("start_date", sa.DateTime(), nullable=False),
        sa.Column("end_date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("officers")
    op.drop_table("memberships")
    op.drop_table("golinks")
    # ### end Alembic commands ###