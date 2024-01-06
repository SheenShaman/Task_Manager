"""Initial

Revision ID: a7463e41d125
Revises: 
Create Date: 2024-01-06 19:51:29.620765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'a7463e41d125'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('position', sa.String(), nullable=False),
                    sa.Column('is_busy', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_employee_id'), 'employee', ['id'], unique=False)
    op.create_table('task',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('parent_task_id', sa.Integer(), nullable=True),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('deadline', sa.DateTime(), nullable=False),
                    sa.Column('status', sa.Enum('NOT_STARTED', 'STARTED', 'COMPLETED', 'CANCELLED', name='taskstatus',
                                                native_enum=False), nullable=True),
                    sa.Column('executor_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['executor_id'], ['employee.id'], ),
                    sa.ForeignKeyConstraint(['parent_task_id'], ['task.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_task_id'), 'task', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_id'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_employee_id'), table_name='employee')
    op.drop_table('employee')
    # ### end Alembic commands ###
