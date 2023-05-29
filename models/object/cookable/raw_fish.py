from models.object.cookable.base import BaseCookable
from models.object.edible.fish import Fish


class RawFish(BaseCookable):
    NAME = "Raw Fish"
    TRANSFORM_INTO = Fish
