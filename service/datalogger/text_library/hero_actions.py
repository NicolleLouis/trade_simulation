
from service.datalogger.logic.text import Text


class HeroAction(Text):
    TITLE = "Hero Actions"
    FILE_ADDRESS = "hero_actions"

    def __init__(self, game):
        super().__init__(game)
        self.hero = self.world.hero

    def should_be_deleted(self):
        return self.game.world.hero is None

    def fetch_data(self):
        if self.hero.dead:
            return
        self.add_point(self.hero.last_action.describe(2))
