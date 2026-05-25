import logging
from dataclasses import asdict

from fastapi import APIRouter, HTTPException, status

try:
    from .RecipeController import RecipeController
    from .RecipeCreateRequest import RecipeCreateRequest
    from .RecipeRepository import RecipeRepository
    from .RecipeService import RecipeService
    from .schemas import RecipeCreateSchema, RecipeResponseSchema
except ImportError:
    from RecipeController import RecipeController
    from RecipeCreateRequest import RecipeCreateRequest
    from RecipeRepository import RecipeRepository
    from RecipeService import RecipeService
    from schemas import RecipeCreateSchema, RecipeResponseSchema

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/recipes", tags=["Recipes"])
controller = RecipeController(RecipeService(RecipeRepository()))


def _to_domain_request(request: RecipeCreateSchema) -> RecipeCreateRequest:
    return RecipeCreateRequest(**request.model_dump())


@router.post("", summary="Create a recipe", response_model=RecipeResponseSchema, status_code=status.HTTP_201_CREATED)
def create_recipe(request: RecipeCreateSchema):
    logger.info(f"Recipe router create called: {request.name}")
    return asdict(controller.create_recipe(_to_domain_request(request)))


@router.get("", summary="List all recipes", response_model=list[RecipeResponseSchema])
def get_recipes():
    logger.info("Recipe router list called")
    return [asdict(recipe) for recipe in controller.get_recipes()]


@router.get("/{recipe_id}", summary="Get recipe by id", response_model=RecipeResponseSchema)
def get_recipe(recipe_id: int):
    logger.info(f"Recipe router get by id called: {recipe_id}")
    response = controller.get_recipe(recipe_id)
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return asdict(response)


@router.put("/{recipe_id}", summary="Update recipe by id", response_model=RecipeResponseSchema)
def update_recipe(recipe_id: int, request: RecipeCreateSchema):
    logger.info(f"Recipe router update called: {recipe_id}")
    response = controller.update_recipe(recipe_id, _to_domain_request(request))
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return asdict(response)


@router.delete("/{recipe_id}", summary="Delete recipe by id", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(recipe_id: int):
    logger.info(f"Recipe router delete called: {recipe_id}")
    if not controller.delete_recipe(recipe_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return None

