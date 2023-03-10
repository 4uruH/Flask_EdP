"""empty message

Revision ID: 9e6611580a6e
Revises: 9e6adc7b4b87
Create Date: 2023-01-15 17:39:58.676915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e6611580a6e'
down_revision = '9e6adc7b4b87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=60), nullable=True))

    # ### end Alembic commands ###
