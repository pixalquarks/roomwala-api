"""Added activated column in owners table

Revision ID: 14ea18c49592
Revises: 095af646402d
Create Date: 2022-01-30 19:22:35.777300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14ea18c49592'
down_revision = '095af646402d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('owners', sa.Column('activated', sa.Integer, server_default=sa.text("0")))


def downgrade():
    op.drop_column('owners', 'activated')
