"""empty message

Revision ID: 59a8e5112071
Revises: 8b76c6c6609b
Create Date: 2019-05-01 14:04:27.588611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59a8e5112071'
down_revision = '8b76c6c6609b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('estabelecimento', sa.Column('fotoPerfil', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('estabelecimento', 'fotoPerfil')
    # ### end Alembic commands ###
