"""create comments

Revision ID: 6c8bcf3080a9
Revises: d1cfab37ed21
Create Date: 2022-07-27 21:00:44.293009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c8bcf3080a9'
down_revision = 'd1cfab37ed21'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('comments',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('content', sa.String(length=50), nullable=False),
                    sa.Column('post_date', sa.DateTime(), nullable=False),
                    sa.Column('commenter_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['commenter_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('comments')
