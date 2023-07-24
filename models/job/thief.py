from models.action.theft import Theft
from models.job.base import BaseJob


class Thief(BaseJob):
    NAME = "Thief"
    ACTIONS = [Theft]
