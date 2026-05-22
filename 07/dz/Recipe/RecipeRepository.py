import logging

from RecipeEntity import RecipeEntity

logger = logging.getLogger(__name__)


class RecipeRepository:
    def __init__(self):
        self._db = []
        self._next_id = 1
        logger.info("RecipeRepository initialized")

    def create_recipe(self, recipe: RecipeEntity) -> RecipeEntity:
        logger.info(f"Creating recipe in repository: {recipe.name}")
        recipe.id = self._next_id
        self._next_id += 1
        self._db.append(recipe)
        logger.info(f"Recipe saved with id={recipe.id}")
        logger.debug(f"Database size: {len(self._db)}")
        return recipe