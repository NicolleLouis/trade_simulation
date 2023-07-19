from models.action.create_object.base import BaseCreateObjectAction
from models.object.cookable.raw_fish import RawFish


class Fish(BaseCreateObjectAction):
    NAME = "FISH"
    RANDOM = True
    OBJECT = RawFish
    EXPERIENCE_GAIN = 1
    BASE_PROBABILITY = 8
