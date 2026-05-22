from dataclasses import dataclass

from ShoesTypes import ShoesType
from ShoesStyle import ShoesStyle


@dataclass
class ShoesResponse:
    type: ShoesType
    style: ShoesStyle
    color: str
    manufacturer: str
    size: float

    def __str__(self):
        return (
            f"ShoesResponse(type={self.type.name}, "
            f"style={self.style.name}, "
            f"color='{self.color}', "
            f"manufacturer='{self.manufacturer}', "
            f"size={self.size})"
        )