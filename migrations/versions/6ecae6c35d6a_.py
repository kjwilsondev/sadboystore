"""empty message

Revision ID: 6ecae6c35d6a
Revises: adc7f56ec6c4
Create Date: 2020-02-07 05:32:15.169827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ecae6c35d6a'
down_revision = 'adc7f56ec6c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_phone_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_phone_key', 'user', ['phone'])
    # ### end Alembic commands ###