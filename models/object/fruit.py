from models.object.base_object import BaseObject


class Fruit(BaseObject):
    NAME = "Blueberry"
    COOKABLE = False
    EDIBLE = True
    FOOD_RETURN = 10
    ESTIMATED_VALUE = 100
