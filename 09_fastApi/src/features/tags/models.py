from sqlalchemy import String, ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.base_model import Base, TimestampMixin
from typing import List, Optional

# ============================================================================
# АСОЦІАТИВНА ТАБЛИЦЯ (Many-to-Many)
# ============================================================================
# Ця таблиця з'єднує Post ↔ Tag
# - post_id: FK на таблицю posts
# - tag_id: FK на таблицю tags
#
# Приклад у БД:
# | post_id | tag_id |
# |---------|--------|
# |    1    |   1    |  ← Post #1 має Tag #1 (Python)
# |    1    |   2    |  ← Post #1 має Tag #2 (Django)
# |    2    |   1    |  ← Post #2 має Tag #1 (Python)
# |    2    |   3    |  ← Post #2 має Tag #3 (Web)
# ============================================================================

post_tags = Table(
    "post_tags",  # Назва таблиці
    Base.metadata,  # Використовуємо базовий metadata
    Column(
        "post_id",
        ForeignKey("posts.id", ondelete="CASCADE"),  # Якщо post видаляється, видаляємо запис
        primary_key=True  # Частина первинного ключа
    ),
    Column(
        "tag_id",
        ForeignKey("tags.id", ondelete="CASCADE"),  # Якщо tag видаляється, видаляємо запис
        primary_key=True  # Частина первинного ключа
    ),
)


# ============================================================================
# МОДЕЛЬ TAG (Тег)
# ============================================================================
class Tag(Base, TimestampMixin):
    """
    Таблиця тегів (мітки/категорії для постів).

    Приклад записів:
    - id=1, name="Python", color="#3776AB" (синій)
    - id=2, name="Django", color="#092E20" (темно-зелений)
    - id=3, name="FastAPI", color="#009688" (аквамарин)
    """

    __tablename__ = "tags"

    # ========================================================================
    # КОЛОНИ
    # ========================================================================

    id: Mapped[int] = mapped_column(primary_key=True)
    # ↑ Унікальний ідентифікатор тега

    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    # ↑ Назва тега (наприклад, "Python", "Django", "FastAPI")
    #   - unique=True: кожен тег має унікальну назву (не може бути два "Python")
    #   - nullable=False: обов'язкове поле
    #   - String(50): максимум 50 символів

    color: Mapped[Optional[str]] = mapped_column(String(7), nullable=True)
    # ↑ Опціональний колір для відображення у UI
    #   - Наприклад: "#FF5733", "#3776AB"
    #   - String(7): хватит для hex-кольорів (#RRGGBB)
    #   - nullable=True: необов'язкове поле
    #   - Optional: Python-тип, який дозволяє None

    # ========================================================================
    # RELATIONSHIP (Зв'язок з Post)
    # ========================================================================

    posts: Mapped[List["Post"]] = relationship(
        secondary=post_tags,  # Використовуємо асоціативну таблицю
        back_populates="tags",  # У Post має бути "tags" relationship
        lazy="selectin"  # Завжди завантажувати теги разом з постом
    )

    # ↑ З'єднання "багато-до-багатьох":
    #   - один Tag може бути у багатьох Post
    #   - один Post може мати багато Tag-ів
    #   - back_populates синхронізує обидва боки зв'язку

    # ========================================================================
    # МЕТОДИ
    # ========================================================================

    def __repr__(self) -> str:
        """Строкове представлення для дебагу."""
        return f"Tag(id={self.id}, name={self.name})"


# ============================================================================
# ІМПОРТИ ДЛЯ TYPE CHECKING
# ============================================================================
# Імпортуємо Post у кінці, щоб уникнути циклічних імпортів
from src.features.posts.models import Post