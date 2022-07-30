"""create likes

Revision ID: 47a576a593ea
Revises: 6c8bcf3080a9
Create Date: 2022-07-27 21:01:45.485522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47a576a593ea'
down_revision = '6c8bcf3080a9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('likes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )


def downgrade():
    op.drop_table('likes')
