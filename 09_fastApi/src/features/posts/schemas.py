from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.features.comments.schemas import CommentRead
    from src.features.tags.schemas import TagRead

class UserShort(BaseModel):
    id: int
    email: str
    
    model_config = ConfigDict(from_attributes=True)

class TagShort(BaseModel):
    """Коротке представлення тега."""
    id: int
    name: str
    color: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class PostBase(BaseModel):
    content: str
    image_url: Optional[str] = None

class PostCreate(PostBase):
    tags: Optional[List[int]] = []  # Список ID тегів

class PostRead(PostBase):
    id: int
    author_id: int
    author: UserShort
    created_at: datetime
    updated_at: datetime
    likes_count: int = 0
    tags: List[TagShort] = []

    model_config = ConfigDict(from_attributes=True)

class PostDetailRead(PostRead):
    comments: List["CommentRead"] = []
    is_liked: bool = False

# Імпортуємо для рантайму
from src.features.comments.schemas import CommentRead
PostDetailRead.model_rebuild()
