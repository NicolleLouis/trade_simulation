from models.action.eat import Eat
from models.action.idle import Idle
from models.object.fruit import Fruit
from service.human import HumanService
from service.human_visualizer import HumanVisualizer


class Human:
    MAXIMUM_STOMACH_LEVEL = 30

    def __init__(self):
        self.name = HumanService.random_name()
        self.age = 0
        self.dead = False

        self.money = 10
        self.stomach_level = 10
        self.possible_action = [Idle, Eat]

        self.inventory = [Fruit()]

        self.visualizer = HumanVisualizer(self)

    def __str__(self):
        return self.name

    def death_checker(self):
        if self.stomach_level < 0:
            self.dead = True

    def find_best_action(self):
        if self.stomach_level < 2:
            return Eat
        return Idle

    def gain_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            raise f"{item} not in {self} possession"

    def run_day(self):
        self.age += 1
        self.stomach_level -= 1
        self.death_checker()
        best_action = self.find_best_action()(self)
        try:
            best_action.make()
        except:
            print(f"{str(best_action)} failed")
        self.visualizer.display()
