
from service.datalogger.logic.graph import Graph


class HeroMoney(Graph):
    TITLE = "Hero Money"
    X_LABEL = "Days"
    Y_LABEL = "Money"
    FILE_ADDRESS = "hero_money"

    def hero(self):
        return self.world.hero

    def should_be_deleted(self):
        return self.game.world.hero is None

    def fetch_data(self):
        hero = self.hero()
        if hero.dead:
            return
        self.add_point("Money", self.day(), hero.money)
