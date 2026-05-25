import logging
from copy import deepcopy

try:
    from .ShoesEntity import ShoesEntity
except ImportError:
    from ShoesEntity import ShoesEntity

logger = logging.getLogger(__name__)


class ShoesRepository:
    def __init__(self):
        self._db: dict[int, ShoesEntity] = {}
        self._next_id = 1
        logger.info("ShoesRepository initialized")

    def create_shoes(self, shoes: ShoesEntity) -> ShoesEntity:
        logger.info(f"Creating shoes in repository: {shoes.color} {shoes.manufacturer}")
        stored_shoes = deepcopy(shoes)
        stored_shoes.id = self._next_id
        self._db[stored_shoes.id] = stored_shoes
        self._next_id += 1
        logger.info(f"Shoes saved with id={stored_shoes.id}")
        return deepcopy(stored_shoes)

    def get_shoes(self) -> list[ShoesEntity]:
        logger.info("Getting all shoes from repository")
        return [deepcopy(shoes) for shoes in self._db.values()]

    def get_shoes_by_id(self, shoes_id: int) -> ShoesEntity | None:
        logger.info(f"Getting shoes by id={shoes_id}")
        shoes = self._db.get(shoes_id)
        return deepcopy(shoes) if shoes else None

    def update_shoes(self, shoes_id: int, shoes: ShoesEntity) -> ShoesEntity | None:
        logger.info(f"Updating shoes id={shoes_id}")
        if shoes_id not in self._db:
            logger.warning(f"Shoes id={shoes_id} not found for update")
            return None

        updated_shoes = deepcopy(shoes)
        updated_shoes.id = shoes_id
        self._db[shoes_id] = updated_shoes
        logger.info(f"Shoes id={shoes_id} updated")
        return deepcopy(updated_shoes)

    def delete_shoes(self, shoes_id: int) -> bool:
        logger.info(f"Deleting shoes id={shoes_id}")
        removed = self._db.pop(shoes_id, None)
        if removed is None:
            logger.warning(f"Shoes id={shoes_id} not found for delete")
            return False

        logger.info(f"Shoes id={shoes_id} deleted")
        return True
