import random

from constants.profile_type import ProfileType
from models.human import Human
from models.job.chef import Chef
from models.job.fisherman import Fisherman
from models.world import World
from service.graph.library.human_money import HumanMoney
from service.graph.library.market_price import MarketPrice
from service.graph.library.world_population import WorldPopulation


class Game:
    WORLD_DISPLAY_LEVEL = 0
    DAY_NUMBER = 300
    DISPLAY_GRAPH = False

    def __init__(self):
        self.world = World(display_level=self.WORLD_DISPLAY_LEVEL)
        self.add_humans()
        self.graphs = []
        self.add_graphs()

    def display_final_state(self):
        for human in self.world.humans:
            human.visualizer.display(2)
        self.world.visualizer.display(2)
        self.world.market.visualizer.display(2)

    def add_graphs(self):
        self.add_graph(WorldPopulation(self.world))
        self.add_graph(MarketPrice(self.world))
        self.add_graph(
            HumanMoney(
                self.world,
                hide_dead=True,
                only_richest=2,
                only_poorest=0,
            )
        )

    def add_humans(self):
        for _ in range(10):
            self.add_human([Fisherman], ProfileType.CAREFUL)
            self.add_human([Chef], ProfileType.CAREFUL)
            self.add_human([Fisherman], ProfileType.NORMAL)
            self.add_human([Chef], ProfileType.NORMAL)
            self.add_human([Fisherman], ProfileType.ADVENTUROUS)
            self.add_human([Chef], ProfileType.ADVENTUROUS)

    def add_human(self, jobs, profile):
        self.world.add_human(
            Human(
                jobs=jobs,
                world=self.world,
                display_level=0,
                profile=profile,
            )
        )

    def display_graph(self):
        for graph in self.graphs:
            if self.DISPLAY_GRAPH:
                graph.display()
            graph.save()

    def run(self):
        for _ in range(self.DAY_NUMBER):
            self.run_day()
        self.display_final_state()
        self.display_graph()

    def run_day(self):
        self.world.run_day()
        for graph in self.graphs:
            graph.fetch_data()

    def add_graph(self, data_logger):
        self.graphs.append(data_logger)
