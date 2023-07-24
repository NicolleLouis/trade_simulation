
from service.datalogger.logic.graph import Graph


class HeroMoney(Graph):
    TITLE = "Hero Money"
    X_LABEL = "Days"
    Y_LABEL = "Money"
    FILE_ADDRESS = "hero_money"

    def __init__(self, game):
        super().__init__(game)
        self.hero = self.world.hero

    def should_be_deleted(self):
        return self.game.world.hero is None

    def fetch_data(self):
        if self.hero.dead:
            return
        self.add_point("Money", self.day(), self.hero.money)
