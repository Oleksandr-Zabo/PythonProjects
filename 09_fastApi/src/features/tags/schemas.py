from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional, List


class TagBase(BaseModel):
    """Базова схема для тега."""
    name: str = Field(..., min_length=1, max_length=50, description="Назва тега")
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$", description="HEX колір (наприклад, #FF5733)")


class TagCreate(TagBase):
    """Схема для створення тега."""
    pass


class TagUpdate(BaseModel):
    """Схема для оновлення тега."""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")


class TagRead(TagBase):
    """Схема для читання тега."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TagWithPostsCount(TagRead):
    """Тег з кількістю постів."""
    posts_count: int = 0

