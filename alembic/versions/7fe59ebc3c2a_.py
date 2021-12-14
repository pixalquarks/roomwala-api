"""empty message

Revision ID: 7fe59ebc3c2a
Revises: 6fa4ef2da6ea
Create Date: 2021-12-14 00:44:28.254557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fe59ebc3c2a'
down_revision = '6fa4ef2da6ea'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('flats', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('flat_owner_fk', source_table="flats", referent_table="owners",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('flat_owner_fk', table_name="flats")
    op.drop_column('flats', 'owner_id')
