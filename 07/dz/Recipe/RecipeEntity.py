from dataclasses import dataclass

from RecipeType import RecipeType
from RecipeCuisine import RecipeCuisine

@dataclass
class RecipeEntity:
    id:int
    name: str
    author: str
    type: RecipeType
    description: str
    video_url: str
    ingredients: list[str]
    cuisine: RecipeCuisine