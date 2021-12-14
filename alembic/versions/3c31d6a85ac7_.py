"""empty message

Revision ID: 3c31d6a85ac7
Revises: 7fe59ebc3c2a
Create Date: 2021-12-14 20:37:53.319063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c31d6a85ac7'
down_revision = '7fe59ebc3c2a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('flats', sa.Column('images', sa.String(250), server_default=sa.text(" 'NA' ")))
    op.add_column('flats', sa.Column('saxx_preference', sa.Integer(), server_default=sa.text("0")))
    op.add_column('flats', sa.Column('furnishing', sa.Integer(), server_default=sa.text('0')))
    op.add_column('flats', sa.Column('electricity', sa.Integer(), server_default=sa.text('0')))
    op.add_column('flats', sa.Column('water', sa.Integer(), server_default=sa.text('0')))


def downgrade():
    op.drop_column('flats', 'images')
    op.drop_column('flats', 'saxx_preference')
    op.drop_column('flats', 'furnishing')
    op.drop_column('flats', 'electricity')
    op.drop_column('flats', 'water')
