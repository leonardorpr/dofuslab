"""empty message

Revision ID: 5d82cc266963
Revises: cc130c42e0e1
Create Date: 2020-03-24 20:19:57.518332

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5d82cc266963'
down_revision = 'cc130c42e0e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_custom_stat')
    op.drop_table('set_custom_bonus')
    op.add_column('item_stat_translation', sa.Column('custom_stat', sa.String(), nullable=False))
    op.add_column('set_bonus_translation', sa.Column('custom_stat', sa.String(), nullable=False))
    op.add_column('set_bonus_translation', sa.Column('set_bonus_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.drop_constraint('fk_set_bonus_translation_set_translation_id_set_bonus', 'set_bonus_translation', type_='foreignkey')
    op.create_foreign_key(op.f('fk_set_bonus_translation_set_bonus_id_set_bonus'), 'set_bonus_translation', 'set_bonus', ['set_bonus_id'], ['uuid'], ondelete='CASCADE')
    op.drop_column('set_bonus_translation', 'set_translation_id')
    op.alter_column('weapon_stat', 'base_crit_chance',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('weapon_stat', 'crit_bonus_damage',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('weapon_stat', 'crit_bonus_damage',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('weapon_stat', 'base_crit_chance',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('set_bonus_translation', sa.Column('set_translation_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(op.f('fk_set_bonus_translation_set_bonus_id_set_bonus'), 'set_bonus_translation', type_='foreignkey')
    op.create_foreign_key('fk_set_bonus_translation_set_translation_id_set_bonus', 'set_bonus_translation', 'set_bonus', ['set_translation_id'], ['uuid'], ondelete='CASCADE')
    op.drop_column('set_bonus_translation', 'set_bonus_id')
    op.drop_column('set_bonus_translation', 'custom_stat')
    op.drop_column('item_stat_translation', 'custom_stat')
    op.create_table('set_custom_bonus',
    sa.Column('uuid', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('set_bonus_translation_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('custom_stat', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['set_bonus_translation_id'], ['set_bonus_translation.uuid'], name='fk_set_custom_bonus_set_bonus_translation_id_set_bonus__4ad7', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid', name='pk_set_custom_bonus')
    )
    op.create_table('item_custom_stat',
    sa.Column('uuid', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('item_stat_translation_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('custom_stat', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['item_stat_translation_id'], ['item_stat_translation.uuid'], name='fk_item_custom_stat_item_stat_translation_id_item_stat__a26f', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid', name='pk_item_custom_stat')
    )
    # ### end Alembic commands ###