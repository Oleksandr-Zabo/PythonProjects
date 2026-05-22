from dataclasses import dataclass

from ShoesTypes import ShoesType
from ShoesStyle import ShoesStyle

@dataclass
class ShoesEntity:
    id: int
    type: ShoesType
    style: ShoesStyle
    color: str
    manufacturer: str
    size: float

