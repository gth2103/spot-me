"""empty message

Revision ID: a567c8c13c2f
Revises: 0b5b55ab34ef
Create Date: 2018-03-08 16:18:59.412451

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a567c8c13c2f'
down_revision = '0b5b55ab34ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'birthday')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthday', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
