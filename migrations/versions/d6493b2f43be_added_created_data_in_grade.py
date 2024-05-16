"""Added Created data in Grade

Revision ID: d6493b2f43be
Revises: d0e4e55ba173
Create Date: 2024-05-16 18:11:54.171731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6493b2f43be'
down_revision = 'd0e4e55ba173'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('father_name', sa.String(length=100), nullable=False),
    sa.Column('mother_name', sa.String(length=100), nullable=False),
    sa.Column('father_mobile', sa.String(length=15), nullable=False),
    sa.Column('mother_mobile', sa.String(length=15), nullable=False),
    sa.Column('address1', sa.String(length=200), nullable=False),
    sa.Column('address2', sa.String(length=200), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=50), nullable=False),
    sa.Column('pin_code', sa.String(length=10), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('blood_group_id', sa.Integer(), nullable=False),
    sa.Column('religious_id', sa.Integer(), nullable=False),
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('section_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.String(length=100), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['blood_group_id'], ['blood_group.id'], ),
    sa.ForeignKeyConstraint(['grade_id'], ['grades.id'], ),
    sa.ForeignKeyConstraint(['religious_id'], ['religious.id'], ),
    sa.ForeignKeyConstraint(['section_id'], ['sections.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###