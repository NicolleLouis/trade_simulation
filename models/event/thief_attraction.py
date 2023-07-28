from models.event.base import Event
from models.job.thief import Thief
from service.human_creation import HumanCreationService


class ThiefAttraction(Event):
    NAME = "Thief Attraction"
    BASE_PROBA = 10
    COOLDOWN = 100

    def __init__(self, world, **kwargs):
        super().__init__(**kwargs)
        self.world = world

    def activation(self):
        thief = HumanCreationService(
            jobs=[Thief],
            world=self.world,
        ).human
        self.world.add_human(thief)

    def activation_condition(self):
        return len(self.world.humans) > 50
