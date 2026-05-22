from ShoesController import ShoesController
from ShoesService import ShoesService
from ShoesRepository import ShoesRepository
from ShoesCreateRequest import ShoesCreateRequest
from ShoesTypes import ShoesType
from ShoesStyle import ShoesStyle


request = ShoesCreateRequest(
    type=ShoesType.MEN,
    style=ShoesStyle.BOOTS,
    color="Black",
    manufacturer="Nike",
    size=42.5,
)

controller = ShoesController(ShoesService(ShoesRepository()))
response = controller.create_shoes(request)

print(f"Shoes created: {response}")