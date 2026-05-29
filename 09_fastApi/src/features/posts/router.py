from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database import get_db
from src.features.auth.dependencies import get_current_user, get_optional_current_user
from src.features.auth.models import User
from .schemas import PostCreate, PostRead, PostDetailRead
from .repository import PostRepository
from .service import PostService
from src.infrastructure.storage.base import StorageService
from src.infrastructure.storage.dependencies import get_storage_service
from src.infrastructure.schemas import PaginationParams, PaginatedResponse
from typing import Optional

router = APIRouter(prefix="/posts", tags=["Social - Posts"])

async def get_post_service(
    db: AsyncSession = Depends(get_db),
    storage: StorageService = Depends(get_storage_service)
) -> PostService:
    repository = PostRepository(db)
    return PostService(repository, storage)

@router.post("/", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(
    content: str = Form(...),
    image: Optional[UploadFile] = File(None),
    tags: Optional[str] = Form(None),  # JSON список ID тегів
    current_user: User = Depends(get_current_user),
    service: PostService = Depends(get_post_service)
):
    import json
    tag_ids = []
    if tags:
        try:
            tag_ids = json.loads(tags)
        except json.JSONDecodeError:
            tag_ids = []

    return await service.create_post(content, current_user.id, image, tag_ids)

@router.get("/", response_model=PaginatedResponse[PostRead])
async def get_posts(
    params: PaginationParams = Depends(),
    current_user: Optional[User] = Depends(get_optional_current_user),
    service: PostService = Depends(get_post_service)
):
    return await service.get_posts_paginated(params, current_user.id if current_user else None)

@router.get("/{post_id}", response_model=PostDetailRead)
async def get_post(
    post_id: int,
    current_user: Optional[User] = Depends(get_optional_current_user),
    service: PostService = Depends(get_post_service)
):
    post = await service.get_post_detail(post_id, current_user.id if current_user else None)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.post("/{post_id}/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def add_tag_to_post(
    post_id: int,
    tag_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Додати тег до поста."""
    repository = PostRepository(db)
    post = await repository.get_post_by_id(post_id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if post.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")

    await repository.add_tags_to_post(post_id, [tag_id])


@router.delete("/{post_id}/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_tag_from_post(
    post_id: int,
    tag_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Видалити тег зі поста."""
    repository = PostRepository(db)
    post = await repository.get_post_by_id(post_id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if post.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")

    await repository.remove_tag_from_post(post_id, tag_id)


@router.get("/tags/{tag_id}", response_model=PaginatedResponse[PostRead])
async def get_posts_by_tag(
    tag_id: int,
    params: PaginationParams = Depends(),
    current_user: Optional[User] = Depends(get_optional_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Отримати пости за тегом."""
    repository = PostRepository(db)
    posts, total = await repository.get_posts_by_tag(tag_id, params.offset, params.limit)

    items = []
    for post in posts:
        post_dict = {
            "id": post.id,
            "content": post.content,
            "image_url": post.image_url,
            "author_id": post.author_id,
            "author": post.author,
            "created_at": post.created_at,
            "updated_at": post.updated_at,
            "likes_count": len(post.likes),
            "tags": post.tags,
        }
        items.append(post_dict)

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
