from service.datalogger.graph_library.hero.hero_job_experience import HeroJobExperience
from service.datalogger.graph_library.hero.hero_money import HeroMoney
from service.datalogger.graph_library.item import Item
from service.datalogger.graph_library.market_price import MarketPrice
from service.datalogger.graph_library.world_population.world_population import WorldPopulation
from service.datalogger.graph_library.world_population.world_population_job import WorldPopulationJob
from service.datalogger.graph_library.world_population.world_population_profile import WorldPopulationProfile
from service.datalogger.text_library.hero_actions import HeroAction


class GameGraphService:
    def __init__(self, game):
        self.game = game
        self.data_loggers = []
        self.add_all_data_loggers()
        self.sanitize_graph()

    def add_all_data_loggers(self):
        self.add_datalogger(WorldPopulation(self.game))
        self.add_datalogger(MarketPrice(self.game))
        self.add_datalogger(WorldPopulationProfile(self.game))
        self.add_datalogger(WorldPopulationJob(self.game))
        self.add_datalogger(Item(self.game))
        self.add_datalogger(HeroMoney(self.game))
        self.add_datalogger(HeroJobExperience(self.game))
        self.add_datalogger(HeroAction(self.game))
        # self.add_datalogger(HumanMoney(self.game, hide_dead=True, only_richest=2, only_poorest=2))

    def add_datalogger(self, data_logger):
        self.data_loggers.append(data_logger)

    def sanitize_graph(self):
        self.data_loggers = [
            graph for graph in self.data_loggers if not graph.should_be_deleted()
        ]

    def export(self, display):
        for graph in self.data_loggers:
            if display:
                graph.display()
            graph.save()

    def fetch_data(self):
        for graph in self.data_loggers:
            graph.fetch_data()
