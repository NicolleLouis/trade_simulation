import random

from models.action.base import BaseAction


class BaseCreateObjectAction(BaseAction):
    OBJECT = None
    BASE_PROBABILITY = None

    def __init__(self, job):
        super().__init__(job)
        self.object_created = False

    def clean_data(self):
        self.object_created = False

    def make(self):
        if random.random() <= self.probability():
            self.get_object()

    def probability(self):
        return (self.BASE_PROBABILITY + self.job.level_impact())/100

    def get_object(self):
        self.object_created = True
        self.human.gain_item(self.OBJECT())
        self.improve_job()

    def expected_happiness(self):
        return self.probability() * self.OBJECT().utility(self.human)

    def describe_lite(self):
        if self.object_created:
            print(f"Created {str(self.OBJECT())}")

    def describe_full(self):
        if not self.object_created:
            print("Nothing created")
            return

        print(f"Object created, probability was: {self.probability()}")
