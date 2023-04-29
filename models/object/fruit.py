from models.object.edible import BaseEdible


class Fruit(BaseEdible):
    NAME = "Fruit"
    EDIBLE = True
    FOOD_RETURN = 10
