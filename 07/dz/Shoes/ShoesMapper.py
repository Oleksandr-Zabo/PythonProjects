try:
    from .ShoesEntity import ShoesEntity
    from .ShoesCreateRequest import ShoesCreateRequest
    from .ShoesResponse import ShoesResponse
except ImportError:
    from ShoesEntity import ShoesEntity
    from ShoesCreateRequest import ShoesCreateRequest
    from ShoesResponse import ShoesResponse


class ShoesMapper:
    @staticmethod
    def map_create_to_entity(request: ShoesCreateRequest, shoes_id: int = 0) -> ShoesEntity:
        return ShoesEntity(
            id=shoes_id,
            type=request.type,
            style=request.style,
            color=request.color,
            manufacturer=request.manufacturer,
            size=request.size,
        )

    @staticmethod
    def map_entity_to_response(entity: ShoesEntity) -> ShoesResponse:
        return ShoesResponse(
            id=entity.id,
            type=entity.type,
            style=entity.style,
            color=entity.color,
            manufacturer=entity.manufacturer,
            size=entity.size,
        )