import logging

from logger_config import setup_logger
from RecipeController import RecipeController
from RecipeService import RecipeService
from RecipeRepository import RecipeRepository
from RecipeCreateRequest import RecipeCreateRequest
from RecipeType import RecipeType
from RecipeCuisine import RecipeCuisine

# Налаштовуємо кольорне логування один раз
setup_logger()

logger = logging.getLogger(__name__)


request = RecipeCreateRequest(
    name="Pasta Carbonara",
    author="Mario Rossi",
    type=RecipeType.MAINCOURSE,
    description="Classic Italian pasta dish",
    video_url="https://example.com/recipe1",
    ingredients=["pasta", "eggs", "bacon", "parmesan"],
    cuisine=RecipeCuisine.ITALIAN,
)

logger.info("Starting application")
controller = RecipeController(RecipeService(RecipeRepository()))
response = controller.create_recipe(request)

logger.info(f"Final result: {response}")
print(f"\nRecipe created: {response}")