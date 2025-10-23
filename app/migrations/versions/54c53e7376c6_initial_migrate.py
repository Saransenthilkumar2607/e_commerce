"""initial migrate

Revision ID: 54c53e7376c6
Revises: 
Create Date: 2025-10-13 12:20:55.734944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54c53e7376c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_db',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False, unique=True),
        sa.Column('email', sa.String(length=120), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False)
    )


def downgrade():
    op.drop_table('user_db')