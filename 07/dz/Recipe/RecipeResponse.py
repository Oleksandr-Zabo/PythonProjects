from dataclasses import dataclass

from RecipeType import RecipeType
from RecipeCuisine import RecipeCuisine


@dataclass
class RecipeResponse:
    id: int
    name: str
    author: str
    type: RecipeType
    description: str
    video_url: str
    ingredients: list[str]
    cuisine: RecipeCuisine

    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return (
            f"RecipeResponse(id={self.id}, name='{self.name}', "
            f"author='{self.author}', type={self.type.name}, "
            f"description='{self.description}', video_url='{self.video_url}', "
            f"ingredients=[{ingredients_str}], cuisine={self.cuisine.name})"
        )