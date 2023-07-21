import random

from models.action.base import BaseAction
from models.object.cookable.base import BaseCookable
from models.object.cookable.raw_fish import RawFish


class Cook(BaseAction):
    NAME = "COOK"
    RANDOM = True
    OBJECT = RawFish
    EXPERIENCE_GAIN = 1
    BASE_PROBABILITY = 50
    FAILURE_PROBABILITY = 10

    def __init__(self, job):
        super().__init__(job)
        self.fish_cooked = False
        self.fish_burned = False
        self.cook_target = None

    def clean_data(self):
        self.find_object()
        self.fish_cooked = False
        self.fish_burned = False

    def make(self):
        if self.is_doable():
            if random.random() <= self.probability():
                self.cook_fish()
            elif random.random() <= self.failure_probability():
                self.burn_fish()

    def find_object(self):
        cookable = filter(
            lambda item: isinstance(item, BaseCookable),
            self.human.inventory
        )
        self.cook_target = next(cookable, None)

    def is_doable(self):
        return self.cook_target is not None

    def probability(self):
        return (self.BASE_PROBABILITY + self.job.level_impact()) / 100

    def failure_probability(self):
        return (self.FAILURE_PROBABILITY - self.job.level_impact()) / 100

    def cook_fish(self):
        self.fish_cooked = True
        self.human.gain_item(self.cook_target.TRANSFORM_INTO())
        self.human.remove_item(self.cook_target)
        self.improve_job()

    def burn_fish(self):
        self.fish_burned = True
        self.human.remove_item(self.cook_target)

    def expected_happiness(self):
        if self.is_doable():
            success_happiness = self.probability() * self.OBJECT().TRANSFORM_INTO().utility(self.human)
            failure_happiness = -(self.failure_probability() * self.OBJECT().utility(self.human))
            return success_happiness + failure_happiness
        return 0

    def describe_lite(self):
        if self.fish_cooked:
            print("Cooked a fish")
        if self.fish_burned:
            print("Burned a fish")

    def describe_full(self):
        if self.fish_cooked:
            print(f"Cooked a fish, proba was: {self.probability()}")
        elif self.fish_burned:
            print(f"Burned a fish, proba was: {self.failure_probability()}")
