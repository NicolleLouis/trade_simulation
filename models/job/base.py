from abc import ABC
from math import floor, log2


class BaseJob(ABC):
    NAME = None
    ACTIONS = None
    MAXIMUM_LEVEL = 10

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

    def is_item_produced(self, item_class):
        for action in self.actions:
            if item_class == action.OBJECT:
                return True
        return False

    def __str__(self):
        if self.NAME is None:
            raise "Name should be defined at class level"

        return self.NAME

    def copy(self, human_copy):
        job_copy = self.__class__(
            human=human_copy,
            experience=self.experience
        )
        human_copy.add_job(job_copy)
        return job_copy

    def update_level(self):
        self.level = min(
            floor(log2(self.experience)),
            self.MAXIMUM_LEVEL
        )

    def level_impact(self):
        return self.level

    def gain_experience(self, experience):
        self.experience += experience
        self.update_level()

    def compute_action(self):
        for action in self.ACTIONS:
            self.actions.append(action(self))
