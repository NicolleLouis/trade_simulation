from models.job.basic import Basic
from service.human import HumanService
from service.market.market import MarketService
from service.visualizer.human_visualizer import HumanVisualizer


class Human:
    def __init__(
            self,
            world,
            money=300,
            stomach_level=30,
            happiness=0,
            inventory=None,
            jobs=None,
            display_level=0
    ):
        if jobs is None:
            jobs = []
        if inventory is None:
            inventory = []

        self.world = world

        self.name = HumanService.random_name()
        self.age = 0
        self.dead = False

        self.money = money
        self.stomach_level = stomach_level
        self.happiness = happiness
        self.jobs = []
        self.inventory = inventory

        self.market_service = MarketService(
            market=self.world.market,
            human=self,
        )

        self.display_level = display_level
        self.last_action = None
        self.visualizer = HumanVisualizer(self)

        self.update_jobs(jobs)
    MAXIMUM_STOMACH_LEVEL = 30

    BASE_JOB = [Basic]

    def run_day(self):
        # Aging
        self.happiness = 0
        self.age += 1
        self.stomach_level -= 1

        # Market morning
        self.market_service.buy()

        # Active Action
        best_action = self.find_best_action()
        self.last_action = best_action
        best_action.run()

        # Market Evening
        self.market_service.sell()

        # Death
        if self.should_die():
            self.dead = True

        # Display
        self.visualizer.display()

    def update_jobs(self, jobs):
        for job in self.BASE_JOB:
            self.jobs.append(job(self))
        for job in jobs:
            self.jobs.append(job(self))

    def __str__(self):
        return self.name

    def compute_happiness(self):
        self.happiness = 0
        self.happiness += self.money
        self.happiness += 10*self.stomach_level
        for item in self.inventory:
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
        return Human(
            money=self.money,
            stomach_level=self.stomach_level,
            happiness=self.happiness,
            inventory=self.inventory.copy(),
            world=self.world
        )

    def gain_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            raise f"{item} not in {self} possession"
