from models.action.create_object.fish import Fish
from models.job.base import BaseJob


class Fisherman(BaseJob):
    NAME = "Fisherman"
    ACTIONS = [Fish]
