from service.datalogger.graph_library.hero.hero_job_experience import HeroJobExperience
from service.datalogger.graph_library.hero.hero_money import HeroMoney
from service.datalogger.text_library.hero_actions import HeroAction


class HeroSwitchService:
    RESET_GRAPH_CLASS = [
        HeroMoney,
        HeroJobExperience,
        HeroAction,
    ]

    def __init__(self, game, hero):
        self.game = game
        self.world = game.world
        self.hero = hero

        self.reset_all_graphs()
        self.set_hero()

    def set_hero(self):
        if self.hero not in self.world.humans:
            raise BaseException("Hero should be an alive human")
        self.world.hero = self.hero

    def reset_all_graphs(self):
        for graph_class in self.RESET_GRAPH_CLASS:
            self.reset_graph(graph_class)

    def reset_graph(self, graph_class):
        for datalogger in self.game.graph_service.data_loggers:
            if isinstance(datalogger, graph_class):
                datalogger.reset_data()
