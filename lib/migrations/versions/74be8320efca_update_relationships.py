"""Update relationships

Revision ID: 74be8320efca
Revises: 4903a38e7cd8
Create Date: 2023-04-04 08:34:43.906618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74be8320efca'
down_revision = '4903a38e7cd8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('freebie_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_companies_freebie_id_freebies'), 'freebies', ['freebie_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_companies_freebie_id_freebies'), type_='foreignkey')
        batch_op.drop_column('freebie_id')

    # ### end Alembic commands ###
