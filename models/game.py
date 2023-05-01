from models.human import Human
from models.job.gatherer import Gatherer
from models.world import World
from service.graph.library.world_population import WorldPopulation


class Game:
    WORLD_DISPLAY_LEVEL = 0
    DAY_NUMBER = 1000
    DISPLAY_GRAPH = False

    def __init__(self):
        self.world = World(display_level=self.WORLD_DISPLAY_LEVEL)
        self.add_humans()
        self.graphs = []
        self.add_graphs()

    def display_final_state(self):
        self.world.visualizer.display(2)
        self.world.market.visualizer.display(2)

    def display_graph(self):
        for graph in self.graphs:
            if self.DISPLAY_GRAPH:
                graph.display()
            graph.save()

    def add_humans(self):
        for _ in range(25):
            self.world.add_human(
                Human(
                    jobs=[Gatherer],
                    world=self.world
                )
            )

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

    def add_graphs(self):
        self.add_graph(WorldPopulation(self.world))
