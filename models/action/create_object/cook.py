import random

from models.action.base import BaseAction
from models.object.edible.fruit import Fruit


class Cook(BaseAction):
    NAME = "COOK"
    RANDOM = True
    OBJECT = Fruit
    EXPERIENCE_GAIN = 1
    BASE_PROBABILITY = 8

    def __init__(self, job):
        super().__init__(job)
        self.fruit_found = False

    def clean_data(self):
        self.fruit_found = False

    def make(self):
        if random.random() <= self.probability():
            self.get_fruit()

    def probability(self):
        return (self.BASE_PROBABILITY + self.job.level_impact())/100

    def get_fruit(self):
        self.fruit_found = True
        self.human.gain_item(self.OBJECT())
        self.improve_job()

    def expected_happiness(self):
        return self.probability() * self.OBJECT().utility(self.human)

    def describe_lite(self):
        if self.fruit_found:
            print("Found a fruit")

    def describe_full(self):
        if not self.fruit_found:
            print("Found nothing")
            return

        print(f"Fruit Found, proba was: {self.probability()}")
