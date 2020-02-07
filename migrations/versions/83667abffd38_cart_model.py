"""cart model

Revision ID: 83667abffd38
Revises: 78dd54d712fd
Create Date: 2020-02-07 02:45:52.361122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83667abffd38'
down_revision = '78dd54d712fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    # ### end Alembic commands ###