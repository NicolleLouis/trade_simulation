from models.job.chef import Chef
from models.object.edible.base import BaseEdible


class Fish(BaseEdible):
    NAME = "Fish"
    EDIBLE = True
    FOOD_RETURN = 25
    JOB_USING = []
    JOB_CREATING = [Chef]
