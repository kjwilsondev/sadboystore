"""empty message

Revision ID: fa959beb9898
Revises: 99bf2b6b909b
Create Date: 2020-02-17 13:59:56.378889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa959beb9898'
down_revision = '99bf2b6b909b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('selling', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('size', sa.String(length=10), nullable=False),
    sa.Column('available', sa.Integer(), nullable=False),
    sa.Column('picture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.Column('fname', sa.String(length=100), nullable=True),
    sa.Column('lname', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('zip_code', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
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
    op.create_table('cart_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('cart_id', sa.String(length=100), nullable=False),
    sa.Column('item_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.user_id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.public_id'], ),
    sa.PrimaryKeyConstraint('id', 'cart_id', 'item_id')
    )
    op.create_table('order_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('order_id', sa.String(length=100), nullable=False),
    sa.Column('item_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.public_id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.public_id'], ),
    sa.PrimaryKeyConstraint('id', 'order_id', 'item_id'),
    sa.UniqueConstraint('item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    op.drop_table('cart_item')
    op.drop_table('order')
    op.drop_table('cart')
    op.drop_table('user')
    op.drop_table('item')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
