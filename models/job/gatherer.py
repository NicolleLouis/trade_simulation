from models.action.gather import Gather
from models.job.base_job import BaseJob


class Gatherer(BaseJob):
    NAME = "Gatherer"
    ACTIONS = [Gather]

    def level_impact(self):
        return self.level