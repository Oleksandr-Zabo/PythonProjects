from ProductDataClass import ProductDataClass

from classProduct import ProductClass

pc1 = ProductClass("name", 100)
pc2 = ProductDataClass("name", 100)

ps1 = ProductClass("name", 100)
ps2 = ProductDataClass("name", 100)

print(f"Product class: {pc1}")
print(f"Product data class: {pc2}")

print(f"Product class == : {pc1==ps1}")
print(f"Product data class == : {pc2==ps2}")



