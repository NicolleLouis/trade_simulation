from service.manual.hero_switch import HeroSwitchService


class SwitchHero:
    def __init__(self, game):
        self.game = game
        self.world = game.world

    def switch_hero_with_highest_job_number(self):
        human = self.get_human_highest_job_number()
        HeroSwitchService(game=self.game, hero=human)

    def get_human_highest_job_number(self):
        humans = self.world.humans
        if len(humans) == 0:
            raise BaseException("No alive human to become heroic")
        hero = humans[0]
        for human in humans:
            if len(human.jobs) < len(hero.jobs):
                continue
            if len(human.jobs) > len(hero.jobs):
                hero = human
                continue
            if human.money > hero.money:
                hero = human
        return hero
