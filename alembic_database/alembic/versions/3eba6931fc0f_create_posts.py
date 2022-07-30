"""create posts

Revision ID: 3eba6931fc0f
Revises: 966a9d570a20
Create Date: 2022-07-27 20:58:24.228916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eba6931fc0f'
down_revision = '966a9d570a20'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('note', sa.String(), nullable=False),
                    sa.Column('photo', sa.String(), nullable=True),
                    sa.Column('location', sa.String(length=50), nullable=True),
                    sa.Column('post_date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('posts')
