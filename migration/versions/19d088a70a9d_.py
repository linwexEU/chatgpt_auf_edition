"""empty message

Revision ID: 19d088a70a9d
Revises: 
Create Date: 2024-01-28 10:43:55.786369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19d088a70a9d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('last_query', sa.String(), nullable=False),
    sa.Column('last_answer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('styles',
    sa.Column('style_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('style', sa.String(), nullable=False),
    sa.Column('style_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['style_user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('style_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('styles')
    op.drop_table('users')
    # ### end Alembic commands ###
