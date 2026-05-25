from pydantic import BaseModel, HttpUrl

try:
    from .RecipeCuisine import RecipeCuisine
    from .RecipeType import RecipeType
except ImportError:
    from RecipeCuisine import RecipeCuisine
    from RecipeType import RecipeType


class RecipeCreateSchema(BaseModel):
    name: str
    author: str
    type: RecipeType
    description: str
    video_url: HttpUrl
    ingredients: list[str]
    cuisine: RecipeCuisine


class RecipeResponseSchema(BaseModel):
    id: int
    name: str
    author: str
    type: RecipeType
    description: str
    video_url: HttpUrl
    ingredients: list[str]
    cuisine: RecipeCuisine

