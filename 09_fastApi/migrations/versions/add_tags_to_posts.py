"""Add tags to posts

Revision ID: add_tags_to_posts
Revises: b2c3d4e5f6a1
Create Date: 2026-05-29 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add_tags_to_posts'
down_revision: Union[str, None] = 'b2c3d4e5f6a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Міграція для додавання підтримки тегів до постів.

    Створює:
    1. Таблицю tags з полями: id, name, color, created_at, updated_at
    2. Асоціативну таблицю post_tags дляMany-to-Many зв'язку
    """

    # Створюємо таблицю tags
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('color', sa.String(length=7), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Створюємо індекс для пошуку по назві тега
    op.create_index(op.f('ix_tags_name'), 'tags', ['name'], unique=True)

    # Створюємо асоціативну таблицю post_tags
    op.create_table(
        'post_tags',
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )

    # Індекси для асоціативної таблиці (опціонально покращує performance)
    op.create_index(op.f('ix_post_tags_post_id'), 'post_tags', ['post_id'])
    op.create_index(op.f('ix_post_tags_tag_id'), 'post_tags', ['tag_id'])


def downgrade() -> None:
    """
    Відкат міграції - видаляємо теги.
    """

    # Видаляємо індекси
    op.drop_index(op.f('ix_post_tags_tag_id'), table_name='post_tags')
    op.drop_index(op.f('ix_post_tags_post_id'), table_name='post_tags')

    # Видаляємо асоціативну таблицю
    op.drop_table('post_tags')

    # Видаляємо індекс тегів
    op.drop_index(op.f('ix_tags_name'), table_name='tags')

    # Видаляємо таблицю тегів
    op.drop_table('tags')

