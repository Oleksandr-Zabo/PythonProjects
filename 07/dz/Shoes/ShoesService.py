from ShoesRepository import ShoesRepository
from ShoesCreateRequest import ShoesCreateRequest
from ShoesMapper import ShoesMapper
from ShoesResponse import ShoesResponse


class ShoesService:
    def __init__(self, shoes_repository: ShoesRepository):
        self._shoes_repository = shoes_repository

    def create_shoes(self, request: ShoesCreateRequest) -> ShoesResponse:
        entity = ShoesMapper.map_create_to_entity(request)
        saved_entity = self._shoes_repository.create_shoes(entity)
        return ShoesMapper.map_entity_to_response(saved_entity)