"""empty message

Revision ID: da2f29fca445
Revises: 08979bcf4318
Create Date: 2020-07-09 14:04:46.301572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da2f29fca445'
down_revision = '08979bcf4318'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #nullable constraints changed to true so upgrade can happen without error
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    #allows completed to update when an upgrade to this version is made
    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')

    #Change constraints later
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###