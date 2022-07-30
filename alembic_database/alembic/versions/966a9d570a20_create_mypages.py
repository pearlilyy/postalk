"""create mypages

Revision ID: 966a9d570a20
Revises: 0108a2aaf1e5
Create Date: 2022-07-27 20:57:11.155287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '966a9d570a20'
down_revision = '0108a2aaf1e5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('mypages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('introduction', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('mypages')
