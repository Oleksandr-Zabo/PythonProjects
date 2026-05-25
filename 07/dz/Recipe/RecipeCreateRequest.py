from dataclasses import dataclass

try:
    from .RecipeType import RecipeType
    from .RecipeCuisine import RecipeCuisine
except ImportError:
    from RecipeType import RecipeType
    from RecipeCuisine import RecipeCuisine


@dataclass
class RecipeCreateRequest:
    name: str
    author: str
    type: RecipeType
    description: str
    video_url: str
    ingredients: list[str]
    cuisine: RecipeCuisine