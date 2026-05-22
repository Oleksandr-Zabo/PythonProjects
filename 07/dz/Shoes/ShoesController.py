from ShoesService import ShoesService
from ShoesCreateRequest import ShoesCreateRequest
from ShoesResponse import ShoesResponse


class ShoesController:
    def __init__(self, shoes_service: ShoesService):
        self._shoes_service = shoes_service

    def create_shoes(self, request: ShoesCreateRequest) -> ShoesResponse:
        return self._shoes_service.create_shoes(request)