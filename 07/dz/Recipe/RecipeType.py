from enum import Enum


class RecipeType(Enum):
    STARTERS = "starters"
    MAINCOURSE = "main course"
    DESERTS = "deserts"
    DRINKS = "drinks"
    OTHER = "other"