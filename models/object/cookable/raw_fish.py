from models.job.fisherman import Fisherman
from models.object.cookable.base import BaseCookable
from models.object.edible.fish import Fish


class RawFish(BaseCookable):
    NAME = "RAW FISH"
    JOB_CREATING = [Fisherman]
    TRANSFORM_INTO = Fish
