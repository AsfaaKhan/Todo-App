"""Initial tasks table

Revision ID: 0001
Revises:
Create Date: 2026-01-04 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('completed', sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.CheckConstraint("length(title) > 0", name="check_title_not_empty")
    )

    # Create index on completed column for efficient filtering
    op.create_index('ix_tasks_completed', 'tasks', ['completed'])

    # Create index on created_at for efficient sorting
    op.create_index('ix_tasks_created_at', 'tasks', ['created_at'])


def downgrade() -> None:
    # Drop the tasks table
    op.drop_index('ix_tasks_completed', table_name='tasks')
    op.drop_index('ix_tasks_created_at', table_name='tasks')
    op.drop_table('tasks')