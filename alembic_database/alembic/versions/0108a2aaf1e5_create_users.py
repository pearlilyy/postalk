"""create users

Revision ID: 0108a2aaf1e5
Revises: 
Create Date: 2022-07-27 20:52:15.779917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0108a2aaf1e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=15), nullable=False),
    sa.Column('first_name', sa.String(length=15), nullable=False),
    sa.Column('last_name', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('reg_date', sa.DateTime(), nullable=False),
    sa.Column('picture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('users')
