from models.object.edible.base import BaseEdible


class Fish(BaseEdible):
    NAME = "Fish"
    EDIBLE = True
    FOOD_RETURN = 25
