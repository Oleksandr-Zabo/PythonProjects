import logging

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
        try:
            response = self._recipe_service.create_recipe(request)
            logger.info(f"Recipe creation successful: {response.id}")
            return response
        except Exception as e:
            logger.error(f"Error in RecipeController.create_recipe: {e}", exc_info=True)
            raise