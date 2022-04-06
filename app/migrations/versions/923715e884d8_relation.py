"""relation

Revision ID: 923715e884d8
Revises: 046311ef16d9
Create Date: 2022-04-04 22:18:37.089409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '923715e884d8'
down_revision = '046311ef16d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###