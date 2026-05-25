import logging
from copy import deepcopy

try:
    from .RecipeEntity import RecipeEntity
except ImportError:
    from RecipeEntity import RecipeEntity

logger = logging.getLogger(__name__)


class RecipeRepository:
    def __init__(self):
        self._db: dict[int, RecipeEntity] = {}
        self._next_id = 1
        logger.info("RecipeRepository initialized")

    def create_recipe(self, recipe: RecipeEntity) -> RecipeEntity:
        logger.info(f"Creating recipe in repository: {recipe.name}")
        stored_recipe = deepcopy(recipe)
        stored_recipe.id = self._next_id
        self._db[stored_recipe.id] = stored_recipe
        self._next_id += 1
        logger.info(f"Recipe saved with id={stored_recipe.id}")
        logger.debug(f"Database size: {len(self._db)}")
        return deepcopy(stored_recipe)

    def get_recipes(self) -> list[RecipeEntity]:
        logger.info("Getting all recipes from repository")
        return [deepcopy(recipe) for recipe in self._db.values()]

    def get_recipe_by_id(self, recipe_id: int) -> RecipeEntity | None:
        logger.info(f"Getting recipe by id={recipe_id}")
        recipe = self._db.get(recipe_id)
        return deepcopy(recipe) if recipe else None

    def update_recipe(self, recipe_id: int, recipe: RecipeEntity) -> RecipeEntity | None:
        logger.info(f"Updating recipe id={recipe_id}")
        if recipe_id not in self._db:
            logger.warning(f"Recipe id={recipe_id} not found for update")
            return None

        updated_recipe = deepcopy(recipe)
        updated_recipe.id = recipe_id
        self._db[recipe_id] = updated_recipe
        logger.info(f"Recipe id={recipe_id} updated")
        return deepcopy(updated_recipe)

    def delete_recipe(self, recipe_id: int) -> bool:
        logger.info(f"Deleting recipe id={recipe_id}")
        removed = self._db.pop(recipe_id, None)
        if removed is None:
            logger.warning(f"Recipe id={recipe_id} not found for delete")
            return False

        logger.info(f"Recipe id={recipe_id} deleted")
        return True
