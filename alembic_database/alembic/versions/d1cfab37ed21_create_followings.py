"""create followings

Revision ID: d1cfab37ed21
Revises: 3eba6931fc0f
Create Date: 2022-07-27 20:59:36.226851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1cfab37ed21'
down_revision = '3eba6931fc0f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('followings',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('following_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['following_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('user_id', 'following_id')
                    )


def downgrade():
    op.drop_table('followings')
