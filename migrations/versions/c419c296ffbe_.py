"""empty message

Revision ID: c419c296ffbe
Revises: ec74040ff677
Create Date: 2021-07-07 16:37:00.309795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c419c296ffbe'
down_revision = 'ec74040ff677'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))
    op.add_column('venues', sa.Column('website', sa.String(length=200), nullable=True))
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.drop_column('venues', 'website')
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###
