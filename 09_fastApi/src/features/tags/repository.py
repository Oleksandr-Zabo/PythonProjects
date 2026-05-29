from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from src.features.tags.models import Tag
from typing import List, Optional, Tuple


class TagRepository:
    """Repository для операцій з тегами у БД."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_tag(self, tag_data: dict) -> Tag:
        """Створити новий тег."""
        new_tag = Tag(**tag_data)
        self.db.add(new_tag)
        await self.db.commit()
        await self.db.refresh(new_tag)
        return new_tag

    async def get_tags(self, skip: int = 0, limit: int = 10) -> Tuple[List[Tag], int]:
        """Отримати список тегів з пагінацією."""
        # Загальна кількість
        total_query = select(func.count(Tag.id))
        total_result = await self.db.execute(total_query)
        total = total_result.scalar() or 0

        # Самі теги
        query = (
            select(Tag)
            .options(selectinload(Tag.posts))
            .order_by(Tag.name)
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(query)
        return result.scalars().all(), total

    async def get_tag_by_id(self, tag_id: int) -> Optional[Tag]:
        """Отримати тег за ID."""
        query = (
            select(Tag)
            .where(Tag.id == tag_id)
            .options(selectinload(Tag.posts))
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_tag_by_name(self, name: str) -> Optional[Tag]:
        """Отримати тег за назвою."""
        query = select(Tag).where(Tag.name.ilike(name))
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def update_tag(self, tag_id: int, update_data: dict) -> Optional[Tag]:
        """Оновити тег."""
        tag = await self.get_tag_by_id(tag_id)
        if not tag:
            return None

        for key, value in update_data.items():
            if value is not None:
                setattr(tag, key, value)

        await self.db.commit()
        await self.db.refresh(tag)
        return tag

    async def delete_tag(self, tag_id: int) -> bool:
        """Видалити тег."""
        tag = await self.get_tag_by_id(tag_id)
        if not tag:
            return False

        await self.db.delete(tag)
        await self.db.commit()
        return True

    async def get_all_tags(self) -> List[Tag]:
        """Отримати всі теги без пагінації."""
        query = select(Tag).order_by(Tag.name)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def search_tags(self, query: str) -> List[Tag]:
        """Пошук тегів за назвою."""
        search_query = select(Tag).where(Tag.name.ilike(f"%{query}%"))
        result = await self.db.execute(search_query)
        return result.scalars().all()

