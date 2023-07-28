import random
from typing import List

from constants.sentimental_status import SentimentalStatus
from models.event.base import Event


class Childbirth(Event):
    NAME = "Childbirth"
    BASE_PROBA = 10
    COOLDOWN = 100

    def __init__(self, sentimental_life):
        if sentimental_life.status != SentimentalStatus.COUPLE:
            raise BaseException('Should be in couple')

        super().__init__()

        self.child = None
        self.world = sentimental_life.human.world
        self.sentimental_life = sentimental_life
        self.parent_a = sentimental_life.human
        self.parent_b = sentimental_life.soulmate

    def activation(self):
        self.child = self.generate_child()
        self.send_child_to_world()
        self.recognize_child()
        self.give_children_money()

    def send_child_to_world(self):
        self.world.add_human(self.child)

    def recognize_child(self):
        self.parent_a.sentimental_life.add_child(self.child)
        self.parent_b.sentimental_life.add_child(self.child)

    def give_children_money(self):
        # State help
        self.child.money += 100

        for parent in [self.parent_a, self.parent_b]:
            money_given = min(100, parent.money)
            parent.money -= money_given
            self.child.money += money_given

    def generate_child(self):
        from service.human_creation import HumanCreationService

        jobs = self.get_parents_jobs()
        profiles = self.get_parent_profile()
        return HumanCreationService(
            world=self.world,
            jobs=jobs,
            profile=profiles,
            money=0,
            parents=[self.parent_a, self.parent_b]
        ).human

    def get_parent_profile(self):
        return list({self.parent_a.profile, self.parent_b.profile})

    def get_parents_jobs(self):
        jobs = self.get_parent_jobs(self.parent_a)
        jobs.extend(self.get_parent_jobs(self.parent_b))
        unique_job = set(jobs)
        return [job for job in unique_job if random.random() < 0.5]

    @staticmethod
    def get_parent_jobs(parent) -> List:
        from models.human.human import Human

        jobs = []
        for job in parent.jobs:
            job_class = job.__class__
            if job_class not in Human.BASE_JOB:
                jobs.append(job_class)
        return jobs

    def activation_condition(self):
        return self.parent_a.money + self.parent_b.money > 800
