import logging

try:
    from .ShoesRepository import ShoesRepository
    from .ShoesCreateRequest import ShoesCreateRequest
    from .ShoesMapper import ShoesMapper
    from .ShoesResponse import ShoesResponse
except ImportError:
    from ShoesRepository import ShoesRepository
    from ShoesCreateRequest import ShoesCreateRequest
    from ShoesMapper import ShoesMapper
    from ShoesResponse import ShoesResponse

logger = logging.getLogger(__name__)


class ShoesService:
    def __init__(self, shoes_repository: ShoesRepository):
        self._shoes_repository = shoes_repository
        logger.info("ShoesService initialized")

    def create_shoes(self, request: ShoesCreateRequest) -> ShoesResponse:
        logger.info(f"ShoesService.create_shoes called: color={request.color}")
        entity = ShoesMapper.map_create_to_entity(request)
        saved_entity = self._shoes_repository.create_shoes(entity)
        response = ShoesMapper.map_entity_to_response(saved_entity)
        logger.info(f"Shoes created successfully: id={response.id}")
        return response

    def get_shoes(self) -> list[ShoesResponse]:
        logger.info("ShoesService.get_shoes called")
        shoes = self._shoes_repository.get_shoes()
        return [ShoesMapper.map_entity_to_response(shoe) for shoe in shoes]

    def get_shoes_by_id(self, shoes_id: int) -> ShoesResponse | None:
        logger.info(f"ShoesService.get_shoes_by_id called: id={shoes_id}")
        shoes = self._shoes_repository.get_shoes_by_id(shoes_id)
        return ShoesMapper.map_entity_to_response(shoes) if shoes else None

    def update_shoes(self, shoes_id: int, request: ShoesCreateRequest) -> ShoesResponse | None:
        logger.info(f"ShoesService.update_shoes called: id={shoes_id}, color={request.color}")
        entity = ShoesMapper.map_create_to_entity(request, shoes_id)
        updated_shoes = self._shoes_repository.update_shoes(shoes_id, entity)
        return ShoesMapper.map_entity_to_response(updated_shoes) if updated_shoes else None

    def delete_shoes(self, shoes_id: int) -> bool:
        logger.info(f"ShoesService.delete_shoes called: id={shoes_id}")
        return self._shoes_repository.delete_shoes(shoes_id)
