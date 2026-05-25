import logging
from dataclasses import asdict

from fastapi import APIRouter, HTTPException, status

try:
    from .ShoesController import ShoesController
    from .ShoesCreateRequest import ShoesCreateRequest
    from .ShoesRepository import ShoesRepository
    from .ShoesService import ShoesService
    from .schemas import ShoesCreateSchema, ShoesResponseSchema
except ImportError:
    from ShoesController import ShoesController
    from ShoesCreateRequest import ShoesCreateRequest
    from ShoesRepository import ShoesRepository
    from ShoesService import ShoesService
    from schemas import ShoesCreateSchema, ShoesResponseSchema

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/shoes", tags=["Shoes"])
controller = ShoesController(ShoesService(ShoesRepository()))


def _to_domain_request(request: ShoesCreateSchema) -> ShoesCreateRequest:
    return ShoesCreateRequest(**request.model_dump())


@router.post("", summary="Create shoes", response_model=ShoesResponseSchema, status_code=status.HTTP_201_CREATED)
def create_shoes(request: ShoesCreateSchema):
    logger.info(f"Shoes router create called: {request.color}")
    return asdict(controller.create_shoes(_to_domain_request(request)))


@router.get("", summary="List all shoes", response_model=list[ShoesResponseSchema])
def get_shoes():
    logger.info("Shoes router list called")
    return [asdict(shoe) for shoe in controller.get_shoes()]


@router.get("/{shoes_id}", summary="Get shoes by id", response_model=ShoesResponseSchema)
def get_shoes_by_id(shoes_id: int):
    logger.info(f"Shoes router get by id called: {shoes_id}")
    response = controller.get_shoes_by_id(shoes_id)
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shoes not found")
    return asdict(response)


@router.put("/{shoes_id}", summary="Update shoes by id", response_model=ShoesResponseSchema)
def update_shoes(shoes_id: int, request: ShoesCreateSchema):
    logger.info(f"Shoes router update called: {shoes_id}")
    response = controller.update_shoes(shoes_id, _to_domain_request(request))
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shoes not found")
    return asdict(response)


@router.delete("/{shoes_id}", summary="Delete shoes by id", status_code=status.HTTP_204_NO_CONTENT)
def delete_shoes(shoes_id: int):
    logger.info(f"Shoes router delete called: {shoes_id}")
    if not controller.delete_shoes(shoes_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shoes not found")
    return None

