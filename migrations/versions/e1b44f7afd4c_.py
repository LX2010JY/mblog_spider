"""empty message

Revision ID: e1b44f7afd4c
Revises: 330c5d3bef40
Create Date: 2016-12-07 15:08:11.277744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1b44f7afd4c'
down_revision = '330c5d3bef40'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'mblog', 'user', ['author_id'], ['id'])
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'mblog', type_='foreignkey')
    ### end Alembic commands ###
