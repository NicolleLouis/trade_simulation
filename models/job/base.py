from abc import ABC, abstractmethod
from math import floor, log2


class BaseJob(ABC):
    NAME = None
    ACTIONS = None

    def __init__(
            self,
            human,
            experience=0
    ):
        self.human = human
        self.experience = experience
        self.level = 0
        self.actions = []
        self.compute_action()

    def __str__(self):
        if self.NAME is None:
            raise "Name should be defined at class level"

        return self.NAME

    def copy(self, human_copy):
        return self.__class__(
            human=human_copy,
            experience=self.experience
        )

    def update_level(self):
        self.level = min(
            floor(log2(self.experience)),
            10
        )

    def level_impact(self):
        return self.level

    def gain_experience(self, experience):
        self.experience += experience
        self.update_level()

    def compute_action(self):
        for action in self.ACTIONS:
            self.actions.append(action(self))
