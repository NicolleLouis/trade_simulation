import random

from models.human.sentimental_life import SentimentalLife
from models.job.basic import Basic
from service.human import HumanService
from service.market.market import MarketService
from service.visualizer.human_visualizer import HumanVisualizer


class Human:
    def __init__(
            self,
            world,
    ):
        self.world = world
        self.display_level = 0

        self.name = HumanService.random_name()
        self.is_male = bool(random.getrandbits(1))
        self.age = 0
        self.dead = False

        self.money = 300
        self.inventory = []
        self.stomach_level = 30
        self.happiness = 0
        self.jobs = [job(self) for job in self.BASE_JOB]
        self.profile = None

        self.sentimental_life = SentimentalLife(
            human=self
        )
        self.market_service = MarketService(
            market=self.world.market,
            human=self,
        )

        self.last_action = None
        self.visualizer = HumanVisualizer(self)

    MAXIMUM_STOMACH_LEVEL = 30
    BASE_JOB = [Basic]

    def run_day(self):
        # Aging
        self.happiness = 0
        self.age += 1
        self.stomach_level -= 1

        # Events
        self.run_events()

        # Market Morning
        self.market_service.buy()

        # Active Action
        best_action = self.find_best_action()
        self.last_action = best_action
        best_action.run()

        # Item destruction check
        self.item_destruction()

        # Market Evening
        self.market_service.sell()

        # Death
        if self.should_die():
            self.death()

        # Display
        self.visualizer.display()

    def run_events(self):
        if self.sentimental_life.events is not None:
            for event in self.sentimental_life.events:
                event.run()

    def death(self):
        self.dead = True
        self.sentimental_life.death()

    def add_job(self, job):
        if len(
                list(
                    filter(
                        lambda known_job: known_job.__class__ == job.__class__,
                        self.jobs
                    )
                )
        ) == 0:
            self.jobs.append(job)

    def __str__(self):
        return self.name

    def compute_happiness(self):
        self.happiness = 0
        self.happiness += self.money
        self.happiness += 10 * self.stomach_level
        for item in self.inventory:
            if item.utility(self) is not None:
                self.happiness += item.utility(self)

    def should_die(self):
        if self.stomach_level <= 0:
            return True
        return False

    def find_best_action(self):
        best_action = None
        best_action_happiness = None
        for job in self.jobs:
            for action in job.actions:
                happiness = self.compute_action_happiness(action.__class__, job)
                if best_action_happiness is None or happiness > best_action_happiness:
                    best_action = action
                    best_action_happiness = happiness
        return best_action

    def compute_action_happiness(self, action, job):
        human_copy = self.copy()
        job_copy = job.copy(human_copy)
        happiness = action(job_copy).expected_happiness()
        if not action.RANDOM:
            action(job_copy).run()
        if human_copy.should_die():
            return -100
        human_copy.compute_happiness()
        happiness += human_copy.happiness

        return happiness

    def copy(self):
        from service.human_creation import HumanCreationService

        return HumanCreationService(
            money=self.money,
            stomach_level=self.stomach_level,
            inventory=self.inventory,
            world=self.world,
        ).human

    def gain_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            raise f"{item} not in {self} possession"

    def item_destruction(self):
        deleted_items = []
        for item in self.inventory:
            if item.DESTROYABLE:
                if random.random() < item.destroy_probability():
                    deleted_items.append(item)
        for item in deleted_items:
            self.remove_item(item)
