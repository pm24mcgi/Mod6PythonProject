"""create_users_table

Revision ID: ffdc0a98111c
Revises:
Create Date: 2020-11-20 15:06:02.230689

"""
from email.policy import default
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffdc0a98111c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=20)),
    sa.Column('last_name', sa.String(length=20)),
    sa.Column('host', sa.Boolean(), nullable=False, default=False ),
    sa.Column('bio', sa.String(1000)),
    sa.Column('photo', sa.String(255)),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    op.create_table('spots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=25), nullable=False),
    sa.Column('description', sa.String(1000)),
    sa.Column('city', sa.String(length=25), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('bedrooms', sa.Integer(), nullable=False),
    sa.Column('bathrooms', sa.Integer(), nullable=False),
    sa.Column('sqFt', sa.Integer(), nullable=False),
    sa.Column('design_type', sa.String(length=25), nullable=False),
    sa.Column('price_per_day', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spot_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['spot_id'], ['spots.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spot_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rating',sa.Float(), nullable=False),
    sa.Column('review',sa.String(length=1000), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['spot_id'], ['spots.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('saves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spot_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['spot_id'], ['spots.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spot_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['spot_id'], ['spots.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('amenities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(25), nullable=False),
    sa.Column('image', sa.String(255), nullable=False),
    sa.PrimaryKeyConstraint('id')

    )

    op.create_table('amenity_spots_join',
    sa.Column('spots', sa.Integer(), nullable=False),
    sa.Column('amenities', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['spots'], ['spots.id'], ),
    sa.ForeignKeyConstraint(['amenities'], ['amenities.id'], ),
    sa.PrimaryKeyConstraint('spots', 'amenities')
    )


    # ### end Alembic commands ###qqqqqqqqq


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('reviews')
    op.drop_table('saves')
    op.drop_table('images')
    op.drop_table('amenity_spots_join')
    op.drop_table('amenities')
    op.drop_table('spots')
    op.drop_table('users')

    # ### end Alembic commands ###
