from models.object.cookable.base import BaseCookable
from models.object.edible.fish import Fish


class RawFish(BaseCookable):
    NAME = "Raw Fish"
    DESTROYABLE = True
    DESTROY_PROBABILITY = 1
    TRANSFORM_INTO = Fish
