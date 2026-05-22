from dataclasses import dataclass

from ShoesTypes import ShoesType
from ShoesStyle import ShoesStyle


@dataclass
class ShoesCreateRequest:
    type: ShoesType
    style: ShoesStyle
    color: str
    manufacturer: str
    size: float