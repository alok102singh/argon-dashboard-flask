"""Added Created data in Grade

Revision ID: a880f79b3ba3
Revises: 
Create Date: 2024-05-16 16:39:02.708423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a880f79b3ba3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grade', sa.Column('created_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grade', 'created_date')
    # ### end Alembic commands ###