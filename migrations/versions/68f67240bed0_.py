"""empty message

Revision ID: 68f67240bed0
Revises: 0099ba8ef7c1
Create Date: 2020-08-22 17:37:45.315650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68f67240bed0'
down_revision = '0099ba8ef7c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('artists', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('artists', 'seeking_venue')
    # ### end Alembic commands ###
