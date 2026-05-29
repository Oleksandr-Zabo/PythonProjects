from src.features.tags.repository import TagRepository
from src.features.tags.schemas import TagCreate, TagRead, TagUpdate
from src.features.tags.models import Tag
from src.infrastructure.schemas import PaginationParams, PaginatedResponse
from typing import List, Optional, Dict, Any


class TagService:
    """Service для бізнес-логіки тегів."""

    def __init__(self, repository: TagRepository):
        self.repository = repository

    async def create_tag(self, request: TagCreate) -> Tag:
        """Створити новий тег."""
        # Перевіримо, чи не існує вже такого тега
        existing = await self.repository.get_tag_by_name(request.name)
        if existing:
            raise ValueError(f"Тег '{request.name}' вже існує")

        tag_data = {
            "name": request.name,
            "color": request.color
        }
        return await self.repository.create_tag(tag_data)

    async def get_tags_paginated(self, params: PaginationParams) -> PaginatedResponse[Dict]:
        """Отримати теги з пагінацією."""
        tags, total = await self.repository.get_tags(params.offset, params.limit)

        items = []
        for tag in tags:
            tag_dict = self._tag_to_dict(tag)
            tag_dict["posts_count"] = len(tag.posts) if tag.posts else 0
            items.append(tag_dict)

        pages = (total + params.size - 1) // params.size

        return PaginatedResponse(
            items=items,
            total=total,
            page=params.page,
            size=params.size,
            pages=pages,
            next_page=params.page + 1 if params.page < pages else None,
            prev_page=params.page - 1 if params.page > 1 else None
        )

    async def get_tag(self, tag_id: int) -> Optional[Dict]:
        """Отримати тег за ID."""
        tag = await self.repository.get_tag_by_id(tag_id)
        if not tag:
            return None

        tag_dict = self._tag_to_dict(tag)
        tag_dict["posts_count"] = len(tag.posts) if tag.posts else 0
        return tag_dict

    async def get_all_tags(self) -> List[Dict]:
        """Отримати всі теги."""
        tags = await self.repository.get_all_tags()
        return [self._tag_to_dict(tag) for tag in tags]

    async def update_tag(self, tag_id: int, request: TagUpdate) -> Optional[Dict]:
        """Оновити тег."""
        update_data = request.model_dump(exclude_unset=True)

        # Якщо змінюємо назву, перевіримо унікальність
        if "name" in update_data and update_data["name"]:
            existing = await self.repository.get_tag_by_name(update_data["name"])
            if existing and existing.id != tag_id:
                raise ValueError(f"Тег '{update_data['name']}' вже існує")

        tag = await self.repository.update_tag(tag_id, update_data)
        if not tag:
            return None

        return self._tag_to_dict(tag)

    async def delete_tag(self, tag_id: int) -> bool:
        """Видалити тег."""
        return await self.repository.delete_tag(tag_id)

    async def search_tags(self, query: str) -> List[Dict]:
        """Пошук тегів."""
        tags = await self.repository.search_tags(query)
        return [self._tag_to_dict(tag) for tag in tags]

    def _tag_to_dict(self, tag: Tag) -> Dict:
        """Конвертувати тег у словник."""
        return {
            "id": tag.id,
            "name": tag.name,
            "color": tag.color,
            "created_at": tag.created_at,
            "updated_at": tag.updated_at,
        }

