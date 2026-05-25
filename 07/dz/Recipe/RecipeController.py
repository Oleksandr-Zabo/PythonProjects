import logging

try:
    from .RecipeService import RecipeService
    from .RecipeCreateRequest import RecipeCreateRequest
    from .RecipeResponse import RecipeResponse
except ImportError:
    from RecipeService import RecipeService
    from RecipeCreateRequest import RecipeCreateRequest
    from RecipeResponse import RecipeResponse

logger = logging.getLogger(__name__)


class RecipeController:
    def __init__(self, recipe_service: RecipeService):
        self._recipe_service = recipe_service
        logger.info("RecipeController initialized")

    def create_recipe(self, request: RecipeCreateRequest) -> RecipeResponse:
        logger.info(f"RecipeController.create_recipe called: {request.name}")
        response = self._recipe_service.create_recipe(request)
        logger.info(f"Recipe creation successful: {response.id}")
        return response

    def get_recipes(self) -> list[RecipeResponse]:
        logger.info("RecipeController.get_recipes called")
        return self._recipe_service.get_recipes()

    def get_recipe(self, recipe_id: int) -> RecipeResponse | None:
        logger.info(f"RecipeController.get_recipe called: id={recipe_id}")
        return self._recipe_service.get_recipe(recipe_id)

    def update_recipe(self, recipe_id: int, request: RecipeCreateRequest) -> RecipeResponse | None:
        logger.info(f"RecipeController.update_recipe called: id={recipe_id}, name={request.name}")
        return self._recipe_service.update_recipe(recipe_id, request)

    def delete_recipe(self, recipe_id: int) -> bool:
        logger.info(f"RecipeController.delete_recipe called: id={recipe_id}")
        return self._recipe_service.delete_recipe(recipe_id)
