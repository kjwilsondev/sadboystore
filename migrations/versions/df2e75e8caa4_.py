"""empty message

Revision ID: df2e75e8caa4
Revises: d55472cf1d8e
Create Date: 2020-02-12 08:15:13.453662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df2e75e8caa4'
down_revision = 'd55472cf1d8e'
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
    op.create_table('item_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('piece', sa.String(length=50), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('size', sa.String(length=10), nullable=False),
    sa.Column('available', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('user_table',
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
    op.create_table('cart_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_table.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('cart_item_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('cart_id', sa.String(length=100), nullable=False),
    sa.Column('item_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart_table.user_id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item_table.public_id'], ),
    sa.PrimaryKeyConstraint('id', 'cart_id', 'item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart_item_table')
    op.drop_table('cart_table')
    op.drop_table('user_table')
    op.drop_table('item_table')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
