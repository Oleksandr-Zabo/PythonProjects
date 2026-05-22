import logging

from RecipeEntity import RecipeEntity
from RecipeCreateRequest import RecipeCreateRequest
from RecipeResponse import RecipeResponse

logger = logging.getLogger(__name__)


class RecipeMapper:
    @staticmethod
    def map_create_to_entity(request: RecipeCreateRequest, recipe_id: int = 0) -> RecipeEntity:
        logger.info(f"Mapping RecipeCreateRequest to RecipeEntity: name={request.name}")
        entity = RecipeEntity(
            id=recipe_id,
            name=request.name,
            author=request.author,
            type=request.type,
            description=request.description,
            video_url=request.video_url,
            ingredients=request.ingredients,
            cuisine=request.cuisine,
        )
        logger.debug(f"RecipeEntity created: {entity}")
        return entity

    @staticmethod
    def map_entity_to_response(entity: RecipeEntity) -> RecipeResponse:
        logger.info(f"Mapping RecipeEntity to RecipeResponse: id={entity.id}, name={entity.name}")
        response = RecipeResponse(
            id=entity.id,
            name=entity.name,
            author=entity.author,
            type=entity.type,
            description=entity.description,
            video_url=entity.video_url,
            ingredients=entity.ingredients,
            cuisine=entity.cuisine,
        )
        logger.debug(f"RecipeResponse created: {response}")
        return response