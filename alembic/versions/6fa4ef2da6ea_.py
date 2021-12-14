"""empty message

Revision ID: 6fa4ef2da6ea
Revises: 1f11aae009bf
Create Date: 2021-12-14 00:26:01.956308

"""
from datetime import timezone
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer
from sqlalchemy.sql.traversals import COMPARE_FAILED


# revision identifiers, used by Alembic.
revision = '6fa4ef2da6ea'
down_revision = '1f11aae009bf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('owners', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(32), nullable=False),
                    sa.Column('mobile', sa.String(10), nullable=False),
                    sa.Column('email', sa.String(32), nullable=False, unique=True),
                    sa.Column('password', sa.String(60), nullable=False),
                    sa.Column('verified', sa.Integer(), server_default=sa.text("0")),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False)
                    )


def downgrade():
    op.drop_table('owners')
