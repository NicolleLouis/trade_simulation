import random

from models.action.base import BaseAction


class Theft(BaseAction):
    NAME = "THEFT"
    RANDOM = True
    EXPERIENCE_GAIN = 1
    BASE_PROBABILITY = 30

    def __init__(self, job):
        super().__init__(job)
        self.theft_successful = False
        self.theft_target = None
        self.amount_stolen = None

    def clean_data(self):
        self.theft_successful = False
        self.amount_stolen = None
        self.theft_target = None
        self.find_target()

    def make(self):
        if self.theft_target is None:
            return
        if random.random() < self.probability():
            self.amount_stolen = min(self.theft_amount(), self.theft_target.money)
            self.theft_target.money -= self.amount_stolen
            self.human.money += self.amount_stolen
            self.improve_job()
            self.theft_successful = True

    def find_target(self):
        target = random.choice(self.human.world.humans)
        if target != self.human:
            self.theft_target = target

    def theft_amount(self):
        return 30 + 3 * self.job.level_impact()

    def probability(self):
        return (self.BASE_PROBABILITY + 5 * self.job.level_impact()) / 100

    def expected_happiness(self):
        return self.theft_amount() * self.probability()

    def describe_lite(self):
        if self.theft_successful:
            return "Theft successful"

    def describe_full(self):
        if self.theft_successful:
            return f'Theft successful ({self.amount_stolen}€) with proba {self.probability()} from {self.theft_target}'
