from models.action.eat import Eat
from models.action.idle import Idle
from models.job.base_job import BaseJob


class Basic(BaseJob):
    NAME = "BASIC"
    ACTIONS = [Idle, Eat]

    def level_impact(self):
        return 0
