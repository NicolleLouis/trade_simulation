from models.action.cook import Cook
from models.job.base import BaseJob


class Chef(BaseJob):
    NAME = "Chef"
    ACTIONS = [Cook]
