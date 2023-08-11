"""empty message

Revision ID: 3e8e18c0bebe
Revises: 8b5bc48e1d4c
Create Date: 2023-08-07 15:52:49.656233

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e8e18c0bebe'
down_revision = '8b5bc48e1d4c'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket_holders', sa.Column('is_registered', sa.Boolean(), server_default='False', nullable=True))
    op.add_column('ticket_holders', sa.Column('register_times', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket_holders', 'register_times')
    op.drop_column('ticket_holders', 'is_registered')
    # ### end Alembic commands ###