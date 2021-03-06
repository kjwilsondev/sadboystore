"""empty message

Revision ID: 1c0a4c677aa0
Revises: ebddc701daf1
Create Date: 2020-02-09 02:33:52.526116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c0a4c677aa0'
down_revision = 'ebddc701daf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('cart_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('cart_id', sa.String(length=100), nullable=False),
    sa.Column('item_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.user_id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.public_id'], ),
    sa.PrimaryKeyConstraint('id', 'cart_id', 'item_id'),
    sa.UniqueConstraint('item_id')
    )
    op.add_column('user', sa.Column('cart_id', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'user', ['public_id'])
    op.create_foreign_key(None, 'user', 'cart', ['cart_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'cart_id')
    op.drop_table('cart_item')
    op.drop_table('cart')
    # ### end Alembic commands ###
