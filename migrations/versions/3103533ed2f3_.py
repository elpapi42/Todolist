"""empty message

Revision ID: 3103533ed2f3
Revises: a777e96bdd97
Create Date: 2019-12-18 13:25:49.970888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3103533ed2f3'
down_revision = 'a777e96bdd97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=32),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=16),
               existing_nullable=False)
    # ### end Alembic commands ###
