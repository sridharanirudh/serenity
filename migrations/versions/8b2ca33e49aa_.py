"""empty message

Revision ID: 8b2ca33e49aa
Revises: 
Create Date: 2020-09-27 08:31:45.846891

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8b2ca33e49aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=mysql.VARCHAR(length=60),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=mysql.VARCHAR(length=60),
               nullable=True)
    # ### end Alembic commands ###
