"""empty message

Revision ID: fd21f5a4b9bb
Revises: fae3f287414e
Create Date: 2020-01-11 23:04:07.711222

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = 'fd21f5a4b9bb'
down_revision = 'fae3f287414e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created', sa.DateTime(), nullable=False, server_default=sa.func.current_timestamp()))
    op.alter_column('users', 'is_admin', nullable=False, new_column_name="admin")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'admin', nullable=False, new_column_name="is_admin")
    op.drop_column('users', 'created')
    # ### end Alembic commands ###
