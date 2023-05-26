from models.action.create_object.gather import Gather
from models.job.base import BaseJob


class Fisherman(BaseJob):
    NAME = "Fisherman"
    ACTIONS = [Gather]
