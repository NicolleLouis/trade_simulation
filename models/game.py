import random

from constants.profile_type import ProfileType
from models.human import Human
from models.job.chef import Chef
from models.job.fisherman import Fisherman
from models.job.gatherer import Gatherer
from models.world import World
from service.graph.library.human_money import HumanMoney
from service.graph.library.market_price import MarketPrice
from service.graph.library.world_population import WorldPopulation
from service.graph.library.world_population_job import WorldPopulationJob
from service.graph.library.world_population_profile import WorldPopulationProfile


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
        # for human in self.world.humans:
        #     human.visualizer.display(2)
        self.world.visualizer.display(2)
        self.world.market.visualizer.display(2)
        self.world.market.visualizer.display(2)

    def add_graphs(self):
        self.add_graph(WorldPopulation(self.world))
        self.add_graph(MarketPrice(self.world))
        self.add_graph(WorldPopulationProfile(self.world))
        self.add_graph(WorldPopulationJob(self.world))

    def add_humans(self):
        for _ in range(15):
            self.add_human([Fisherman])
            self.add_human([Chef])
            self.add_human([Gatherer])

    def add_human(self, jobs):
        profile = random.choice(
            [ProfileType.CAREFUL,
             ProfileType.NORMAL,
             ProfileType.ADVENTUROUS]
        )
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
