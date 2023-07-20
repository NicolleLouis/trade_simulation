import random

from constants.profile_type import ProfileType
from models.human import Human
from models.job.chef import Chef
from models.job.fisherman import Fisherman
from models.world import World
from service.game.graph import GameGraphService


class Game:
    WORLD_DISPLAY_LEVEL = 0
    DAY_NUMBER = 300
    DISPLAY_GRAPH = False

    def __init__(self):
        self.world = World(display_level=self.WORLD_DISPLAY_LEVEL)
        self.add_humans()
        self.add_hero()
        self.graph_service = GameGraphService(self)

    def display_final_state(self):
        # for human in self.world.humans:
        #     human.visualizer.display(2)
        self.world.visualizer.display(2)
        self.world.market.visualizer.display(2)

    def add_hero(self):
        hero = self.random_human([Chef], 2)
        self.world.add_hero(hero)

    def add_humans(self):
        for _ in range(5):
            self.add_human([Fisherman])
        # for _ in range(1):
        #     self.add_human([Chef])

    def add_human(self, jobs):
        self.world.add_human(self.random_human(jobs))

    def random_human(self, jobs, display_level=0):
        profile = random.choice(
            [ProfileType.CAREFUL,
             ProfileType.NORMAL,
             ProfileType.ADVENTUROUS]
        )
        return Human(
            jobs=jobs,
            world=self.world,
            display_level=display_level,
            profile=profile,
        )

    def run(self, day_number=None):
        if day_number is None:
            day_number = self.DAY_NUMBER
        for _ in range(day_number):
            self.run_day()
        self.display_final_state()
        self.graph_service.export(self.DISPLAY_GRAPH)

    def run_day(self):
        self.world.run_day()
        self.graph_service.fetch_data()
