import logging

from RecipeRepository import RecipeRepository
from RecipeCreateRequest import RecipeCreateRequest
from RecipeMapper import RecipeMapper
from RecipeResponse import RecipeResponse

logger = logging.getLogger(__name__)


class RecipeService:
    def __init__(self, recipe_repository: RecipeRepository):
        self._recipe_repository = recipe_repository
        logger.info("RecipeService initialized")

    def create_recipe(self, request: RecipeCreateRequest) -> RecipeResponse:
        logger.info(f"RecipeService.create_recipe called: name={request.name}")
        try:
            entity = RecipeMapper.map_create_to_entity(request)
            saved_entity = self._recipe_repository.create_recipe(entity)
            response = RecipeMapper.map_entity_to_response(saved_entity)
            logger.info(f"Recipe created successfully: id={response.id}")
            return response
        except Exception as e:
            logger.error(f"Error creating recipe: {e}", exc_info=True)
            raise