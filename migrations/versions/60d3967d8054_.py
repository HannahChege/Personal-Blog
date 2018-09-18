"""empty message

Revision ID: 60d3967d8054
Revises: 95de292e7114
Create Date: 2018-09-18 20:15:35.409867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d3967d8054'
down_revision = '95de292e7114'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blog_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_admin_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'blog', ['blog_id'], ['id'])
    op.drop_column('comments', 'admin_id')
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('admin_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'blog', ['pitch_id'], ['id'])
    op.create_foreign_key('comments_admin_id_fkey', 'comments', 'users', ['admin_id'], ['id'])
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'blog_id')
    # ### end Alembic commands ###