"""empty message

Revision ID: 56b2e1509bd3
Revises: 356031728057
Create Date: 2020-02-17 13:55:09.923137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b2e1509bd3'
down_revision = '356031728057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('ordered_on', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('order_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('order_id', sa.String(length=100), nullable=False),
    sa.Column('item_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.public_id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.user_id'], ),
    sa.PrimaryKeyConstraint('id', 'order_id', 'item_id'),
    sa.UniqueConstraint('item_id'),
    sa.UniqueConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    op.drop_table('order')
    # ### end Alembic commands ###
