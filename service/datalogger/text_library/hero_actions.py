from service.datalogger.logic.text import Text


class HeroAction(Text):
    TITLE = "Hero Actions"
    FILE_ADDRESS = "hero_actions"

    def hero(self):
        return self.world.hero

    def should_be_deleted(self):
        return self.game.world.hero is None

    def fetch_data(self):
        hero = self.hero()
        if hero.dead:
            return
        self.add_point(hero.last_action.describe(2))
