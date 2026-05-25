from pydantic import BaseModel

try:
    from .ShoesStyle import ShoesStyle
    from .ShoesTypes import ShoesType
except ImportError:
    from ShoesStyle import ShoesStyle
    from ShoesTypes import ShoesType


class ShoesCreateSchema(BaseModel):
    type: ShoesType
    style: ShoesStyle
    color: str
    manufacturer: str
    size: float


class ShoesResponseSchema(BaseModel):
    id: int
    type: ShoesType
    style: ShoesStyle
    color: str
    manufacturer: str
    size: float

