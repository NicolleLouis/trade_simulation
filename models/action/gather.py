import random

from models.action.base_action import BaseAction
from models.object.fruit import Fruit


class Gather(BaseAction):
    NAME = "GATHER"
    RANDOM = True
    OBJECT = Fruit

    def __init__(self, job):
        super().__init__(job)
        self.fruit_found = False

    def probability(self):
        return (8 + self.job.level_impact())/100

    def get_fruit(self):
        self.fruit_found = True
        self.human.gain_item(self.OBJECT())

    def get_nothing(self):
        self.fruit_found = False

    def make(self):
        if random.random() <= self.probability():
            self.get_fruit()
        else:
            self.get_nothing()

    def expected_happiness(self):
        return self.probability() * self.OBJECT().utility(self.human)

    def describe(self):
        if self.fruit_found:
            print("Found a fruit")
        else:
            print("Found nothing")
