"""empty message

Revision ID: 7ac0ceb4aa3c
Revises: 
Create Date: 2018-02-05 07:47:11.266455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ac0ceb4aa3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('initiative',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('initiative_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['initiative_id'], ['initiative.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personname', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('employeeID', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donation')
    op.drop_table('event')
    op.drop_table('user')
    op.drop_table('initiative')
    # ### end Alembic commands ###
