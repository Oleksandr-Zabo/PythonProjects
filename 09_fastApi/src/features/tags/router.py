from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database import get_db
from src.features.tags.schemas import TagCreate, TagRead, TagUpdate, TagWithPostsCount
from src.features.tags.repository import TagRepository
from src.features.tags.service import TagService
from src.infrastructure.schemas import PaginationParams, PaginatedResponse
from typing import List

router = APIRouter(prefix="/tags", tags=["Tags"])


async def get_tag_service(db: AsyncSession = Depends(get_db)) -> TagService:
    """Dependency для отримання TagService."""
    repository = TagRepository(db)
    return TagService(repository)


@router.post("/", response_model=TagRead, status_code=status.HTTP_201_CREATED)
async def create_tag(
    request: TagCreate,
    service: TagService = Depends(get_tag_service)
):
    """Створити новий тег.

    - **name**: Назва тега (унікальна, 1-50 символів)
    - **color**: Опціональний HEX колір (наприклад, #FF5733)
    """
    try:
        tag = await service.create_tag(request)
        return tag
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=PaginatedResponse[TagWithPostsCount])
async def get_tags(
    params: PaginationParams = Depends(),
    service: TagService = Depends(get_tag_service)
):
    """Отримати список тегів з пагінацією.

    Параметри пагінації:
    - **page**: Сторінка (за замовчуванням 1)
    - **size**: Розмір сторінки (за замовчуванням 10)
    """
    return await service.get_tags_paginated(params)


@router.get("/search/", response_model=List[TagRead])
async def search_tags(
    q: str,
    service: TagService = Depends(get_tag_service)
):
    """Пошук тегів за назвою.

    - **q**: Пошукова строка
    """
    return await service.search_tags(q)


@router.get("/all/", response_model=List[TagRead])
async def get_all_tags(
    service: TagService = Depends(get_tag_service)
):
    """Отримати всі теги без пагінації."""
    return await service.get_all_tags()


@router.get("/{tag_id}", response_model=TagWithPostsCount)
async def get_tag(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    """Отримати тег за ID.

    - **tag_id**: ID тега
    """
    tag = await service.get_tag(tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не знайдений"
        )
    return tag


@router.put("/{tag_id}", response_model=TagRead)
async def update_tag(
    tag_id: int,
    request: TagUpdate,
    service: TagService = Depends(get_tag_service)
):
    """Оновити тег.

    - **tag_id**: ID тега
    - **name**: Новa назва (опціонально)
    - **color**: Новий колір (опціонально)
    """
    try:
        tag = await service.update_tag(tag_id, request)
        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Тег не знайдений"
            )
        return tag
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(
    tag_id: int,
    service: TagService = Depends(get_tag_service)
):
    """Видалити тег.

    - **tag_id**: ID тега
    """
    success = await service.delete_tag(tag_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не знайдений"
        )

