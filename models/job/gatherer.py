from models.action.create_object.gather import Gather
from models.job.base import BaseJob


class Gatherer(BaseJob):
    NAME = "Gatherer"
    ACTIONS = [Gather]
