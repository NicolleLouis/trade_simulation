from models.action.create_object.base import BaseCreateObjectAction


class Gather(BaseCreateObjectAction):
    from models.object.edible.fruit import Fruit

    NAME = "GATHER"
    RANDOM = True
    OBJECT = Fruit
    EXPERIENCE_GAIN = 1
    BASE_PROBABILITY = 8
