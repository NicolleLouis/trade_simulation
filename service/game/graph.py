from service.graph.library.hero.hero_job_experience import HeroJobExperience
from service.graph.library.hero.hero_money import HeroMoney
from service.graph.library.item import Item
from service.graph.library.market_price import MarketPrice
from service.graph.library.world_population.world_population import WorldPopulation
from service.graph.library.world_population.world_population_job import WorldPopulationJob
from service.graph.library.world_population.world_population_profile import WorldPopulationProfile


class GameGraphService:
    def __init__(self, game):
        self.game = game
        self.graphs = []
        self.add_all_graphs()
        self.sanitize_graph()

    def add_all_graphs(self):
        self.add_graph(WorldPopulation(self.game))
        self.add_graph(MarketPrice(self.game))
        self.add_graph(WorldPopulationProfile(self.game))
        self.add_graph(WorldPopulationJob(self.game))
        self.add_graph(Item(self.game))
        self.add_graph(HeroMoney(self.game))
        self.add_graph(HeroJobExperience(self.game))
        # self.add_graph(HumanMoney(self.game, hide_dead=True, only_richest=2, only_poorest=2))

    def add_graph(self, data_logger):
        self.graphs.append(data_logger)

    def sanitize_graph(self):
        self.graphs = [
            graph for graph in self.graphs if not graph.should_be_deleted()
        ]

    def export(self, display):
        for graph in self.graphs:
            if display:
                graph.display()
            graph.save()

    def fetch_data(self):
        for graph in self.graphs:
            graph.fetch_data()
