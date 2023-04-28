from models.action.idle import ActionIdle
from service.human import HumanService


class Human:
    def __init__(self):
        self.name = HumanService.random_name()
        self.age = 0
        self.money = 10
        self.stomach_level = 25
        self.possible_action = [ActionIdle]
        self.dead = False

    def death_checker(self):
        if self.stomach_level < 0:
            self.dead = True

    def find_best_action(self):
        return self.possible_action[0](self)

    def run_day(self):
        self.age += 1
        self.stomach_level -= 1
        self.death_checker()
        best_action = self.find_best_action()
        best_action.make()
