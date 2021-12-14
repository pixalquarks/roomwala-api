"""creating owner and flat table

Revision ID: 1f11aae009bf
Revises: 
Create Date: 2021-12-14 00:04:01.954753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f11aae009bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('flats', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address', sa.String(100), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('bhk', sa.Integer(), nullable=False),
                    sa.Column('locality', sa.String(20), nullable=False),
                    sa.Column('description', sa.String(300), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))


def downgrade():
    op.drop_table('flats')
