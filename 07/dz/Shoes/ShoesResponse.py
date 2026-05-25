from dataclasses import dataclass

try:
    from .ShoesTypes import ShoesType
    from .ShoesStyle import ShoesStyle
except ImportError:
    from ShoesTypes import ShoesType
    from ShoesStyle import ShoesStyle


@dataclass
class ShoesResponse:
    id: int
    type: ShoesType
    style: ShoesStyle
    color: str
    manufacturer: str
    size: float

    def __str__(self):
        return (
            f"ShoesResponse(id={self.id}, type={self.type.name}, "
            f"style={self.style.name}, "
            f"color='{self.color}', "
            f"manufacturer='{self.manufacturer}', "
            f"size={self.size})"
        )