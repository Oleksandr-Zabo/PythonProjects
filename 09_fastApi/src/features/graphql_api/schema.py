import strawberry
from typing import List, Optional
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.features.posts.models import Post
from src.features.comments.models import Comment
from src.features.tags.models import Tag
from sqlalchemy.ext.asyncio import AsyncSession

@strawberry.type
class UserType:
    id: int
    email: str

@strawberry.type
class TagType:
    id: int
    name: str
    color: Optional[str]
    created_at: datetime

@strawberry.type
class CommentType:
    id: int
    content: str
    author: UserType
    created_at: datetime

@strawberry.type
class PostType:
    id: int
    content: str
    image_url: Optional[str]
    created_at: datetime
    author: UserType
    likes_count: int
    tags: List[TagType]
    comments: List[CommentType]

@strawberry.type
class Query:
    @strawberry.field
    async def all_posts(self, info: strawberry.Info, limit: int = 10, offset: int = 0) -> List[PostType]:
        """
        Отримати список постів з усіма вкладеними даними.
        Демонструє силу GraphQL: фронтенд сам вирішує, які поля йому потрібні.
        """
        db: AsyncSession = info.context["db"]
        
        # Формуємо запит з жадібним завантаженням всіх необхідних зв'язків
        query = (
            select(Post)
            .options(
                selectinload(Post.author), 
                selectinload(Post.likes),
                selectinload(Post.tags),
                selectinload(Post.comments).selectinload(Comment.author)
            )
            .order_by(Post.created_at.desc())
            .offset(offset)
            .limit(limit)
        )

        result = await db.execute(query)
        posts = result.scalars().all()

        return [
            PostType(
                id=p.id,
                content=p.content,
                image_url=p.image_url,
                created_at=p.created_at,
                author=UserType(id=p.author.id, email=p.author.email),
                likes_count=len(p.likes),
                tags=[
                    TagType(
                        id=t.id,
                        name=t.name,
                        color=t.color,
                        created_at=t.created_at
                    ) for t in (p.tags or [])
                ],
                comments=[
                    CommentType(
                        id=c.id,
                        content=c.content,
                        created_at=c.created_at,
                        author=UserType(id=c.author.id, email=c.author.email)
                    ) for c in p.comments
                ]
            ) for p in posts
        ]

    @strawberry.field
    async def posts_by_tag(self, info: strawberry.Info, tag_id: int, limit: int = 10, offset: int = 0) -> List[PostType]:
        """Отримати пости за тегом."""
        db: AsyncSession = info.context["db"]

        query = (
            select(Post)
            .join(Post.tags)
            .where(Tag.id == tag_id)
            .options(
                selectinload(Post.author),
                selectinload(Post.likes),
                selectinload(Post.tags),
                selectinload(Post.comments).selectinload(Comment.author)
            )
            .order_by(Post.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        
        result = await db.execute(query)
        posts = result.scalars().all()
        
        return [
            PostType(
                id=p.id,
                content=p.content,
                image_url=p.image_url,
                created_at=p.created_at,
                author=UserType(id=p.author.id, email=p.author.email),
                likes_count=len(p.likes),
                tags=[
                    TagType(
                        id=t.id,
                        name=t.name,
                        color=t.color,
                        created_at=t.created_at
                    ) for t in (p.tags or [])
                ],
                comments=[
                    CommentType(
                        id=c.id,
                        content=c.content,
                        created_at=c.created_at,
                        author=UserType(id=c.author.id, email=c.author.email)
                    ) for c in p.comments
                ]
            ) for p in posts
        ]

    @strawberry.field
    async def all_tags(self, info: strawberry.Info) -> List[TagType]:
        """Отримати всі теги."""
        db: AsyncSession = info.context["db"]

        query = select(Tag).options(selectinload(Tag.posts))
        result = await db.execute(query)
        tags = result.scalars().all()

        return [
            TagType(
                id=t.id,
                name=t.name,
                color=t.color,
                created_at=t.created_at
            ) for t in tags
        ]

schema = strawberry.Schema(query=Query)
