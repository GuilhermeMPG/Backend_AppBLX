"""Inicial

Revision ID: 4f5c44e435a5
Revises: 080cfa6e9650
Create Date: 2023-02-02 16:42:23.309875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f5c44e435a5'
down_revision = '080cfa6e9650'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanho', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanho')
    # ### end Alembic commands ###
