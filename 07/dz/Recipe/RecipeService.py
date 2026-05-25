import logging

try:
    from .RecipeRepository import RecipeRepository
    from .RecipeCreateRequest import RecipeCreateRequest
    from .RecipeMapper import RecipeMapper
    from .RecipeResponse import RecipeResponse
except ImportError:
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
        entity = RecipeMapper.map_create_to_entity(request)
        saved_entity = self._recipe_repository.create_recipe(entity)
        response = RecipeMapper.map_entity_to_response(saved_entity)
        logger.info(f"Recipe created successfully: id={response.id}")
        return response

    def get_recipes(self) -> list[RecipeResponse]:
        logger.info("RecipeService.get_recipes called")
        recipes = self._recipe_repository.get_recipes()
        return [RecipeMapper.map_entity_to_response(recipe) for recipe in recipes]

    def get_recipe(self, recipe_id: int) -> RecipeResponse | None:
        logger.info(f"RecipeService.get_recipe called: id={recipe_id}")
        recipe = self._recipe_repository.get_recipe_by_id(recipe_id)
        return RecipeMapper.map_entity_to_response(recipe) if recipe else None

    def update_recipe(self, recipe_id: int, request: RecipeCreateRequest) -> RecipeResponse | None:
        logger.info(f"RecipeService.update_recipe called: id={recipe_id}, name={request.name}")
        entity = RecipeMapper.map_create_to_entity(request, recipe_id)
        updated_entity = self._recipe_repository.update_recipe(recipe_id, entity)
        return RecipeMapper.map_entity_to_response(updated_entity) if updated_entity else None

    def delete_recipe(self, recipe_id: int) -> bool:
        logger.info(f"RecipeService.delete_recipe called: id={recipe_id}")
        return self._recipe_repository.delete_recipe(recipe_id)
