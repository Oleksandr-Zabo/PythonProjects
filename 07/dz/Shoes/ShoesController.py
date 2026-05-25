import logging

try:
    from .ShoesService import ShoesService
    from .ShoesCreateRequest import ShoesCreateRequest
    from .ShoesResponse import ShoesResponse
except ImportError:
    from ShoesService import ShoesService
    from ShoesCreateRequest import ShoesCreateRequest
    from ShoesResponse import ShoesResponse

logger = logging.getLogger(__name__)


class ShoesController:
    def __init__(self, shoes_service: ShoesService):
        self._shoes_service = shoes_service
        logger.info("ShoesController initialized")

    def create_shoes(self, request: ShoesCreateRequest) -> ShoesResponse:
        logger.info(f"ShoesController.create_shoes called: color={request.color}")
        return self._shoes_service.create_shoes(request)

    def get_shoes(self) -> list[ShoesResponse]:
        logger.info("ShoesController.get_shoes called")
        return self._shoes_service.get_shoes()

    def get_shoes_by_id(self, shoes_id: int) -> ShoesResponse | None:
        logger.info(f"ShoesController.get_shoes_by_id called: id={shoes_id}")
        return self._shoes_service.get_shoes_by_id(shoes_id)

    def update_shoes(self, shoes_id: int, request: ShoesCreateRequest) -> ShoesResponse | None:
        logger.info(f"ShoesController.update_shoes called: id={shoes_id}, color={request.color}")
        return self._shoes_service.update_shoes(shoes_id, request)

    def delete_shoes(self, shoes_id: int) -> bool:
        logger.info(f"ShoesController.delete_shoes called: id={shoes_id}")
        return self._shoes_service.delete_shoes(shoes_id)
