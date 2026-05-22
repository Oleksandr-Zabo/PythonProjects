from ShoesEntity import ShoesEntity


class ShoesRepository:
    def __init__(self):
        self._db = []
        self._next_id = 1

    def create_shoes(self, shoes: ShoesEntity) -> ShoesEntity:
        shoes.id = self._next_id
        self._next_id += 1
        self._db.append(shoes)
        return shoes