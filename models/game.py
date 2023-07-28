from models.event.thief_attraction import ThiefAttraction
from models.event.wedding import Wedding
from models.job.chef import Chef
from models.job.fisherman import Fisherman
from models.job.gatherer import Gatherer
from models.job.thief import Thief
from models.world import World
from service.game.graph import GameGraphService
from service.human_creation import HumanCreationService


class Game:
    WORLD_DISPLAY_LEVEL = 0
    DAY_NUMBER = 300
    DISPLAY_GRAPH = False

    def __init__(self):
        self.world = World(display_level=self.WORLD_DISPLAY_LEVEL)
        self.add_humans()
        self.add_hero()
        self.graph_service = GameGraphService(self)
        self.add_world_events()

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

    def display_final_state(self):
        self.world.visualizer.display(2)
        self.world.market.visualizer.display(0)

    def add_hero(self):
        hero = HumanCreationService(
            jobs=[Fisherman, Chef, Gatherer],
            world=self.world,
            display_level=0
        ).human
        self.world.add_hero(hero)

    def add_humans(self):
        for _ in range(10):
            self.add_human([Fisherman])
            self.add_human([Fisherman])
            self.add_human([Fisherman])
            self.add_human([Chef])
            self.add_human([Gatherer])
        pass

    def add_human(self, jobs):
        human = HumanCreationService(
            jobs=jobs,
            world=self.world,
        ).human
        self.world.add_human(human)

    def add_world_events(self):
        events = [
            Wedding(self.world),
            ThiefAttraction(self.world),
        ]
        for event in events:
            self.world.add_event(event)
