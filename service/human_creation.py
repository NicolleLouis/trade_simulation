import random

from constants.profile_type import ProfileType
from models.human.human import Human


class HumanCreationService:
    def __init__(
            self,
            world,
            jobs=None,
            inventory=None,
            money=None,
            stomach_level=None,
            profile=None,
            display_level=None,
            parents=None,
    ):
        self.human = Human(world)
        self.jobs = jobs
        self.inventory = inventory
        self.money = money
        self.stomach_level = stomach_level
        self.profile = profile
        self.display_level = display_level
        self.parents = parents

        self.add_jobs()
        self.add_inventory()
        self.set_money()
        self.set_stomach_level()
        self.set_display_level()
        self.set_profile()
        self.set_parents()

    def add_jobs(self):
        if self.jobs is None:
            return
        [self.human.jobs.append(job_class(self.human)) for job_class in self.jobs]

    def add_inventory(self):
        if self.inventory is None:
            return
        [self.human.gain_item(item) for item in self.inventory]

    def set_money(self):
        if self.money is None:
            return
        self.human.money = self.money

    def set_stomach_level(self):
        if self.stomach_level is None:
            return
        self.human.stomach_level = self.stomach_level

    def set_display_level(self):
        if self.display_level is None:
            return
        self.human.display_level = self.display_level

    def set_profile(self):
        if isinstance(self.profile, ProfileType):
            self.human.profile = self.profile
            return
        elif self.profile is None:
            profile = random.choice(
                [ProfileType.CAREFUL,
                 ProfileType.NORMAL,
                 ProfileType.ADVENTUROUS]
            )
            self.human.profile = profile
            return
        elif isinstance(self.profile, list):
            self.human.profile = random.choice(self.profile)

    def set_parents(self):
        if self.parents is None:
            return
        if not isinstance(self.parents, list):
            raise BaseException("Parents should be a list")
        if len(self.parents) != 2:
            raise BaseException("2 Parents only")

        self.human.sentimental_life.parent_a = self.parents[0]
        self.human.sentimental_life.parent_b = self.parents[1]
