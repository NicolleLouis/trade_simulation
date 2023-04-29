from models.action.eat import Eat
from models.action.idle import Idle
from models.object.fruit import Fruit
from service.human import HumanService
from service.human_visualizer import HumanVisualizer


class Human:
    MAXIMUM_STOMACH_LEVEL = 30

    def __init__(
            self,
            money=10,
            stomach_level=1,
            happiness=0,
            possible_action=[Idle, Eat],
            inventory=[Fruit()],
            display=False
    ):
        self.name = HumanService.random_name()
        self.age = 0
        self.dead = False
        self.last_action = None

        self.money = money
        self.stomach_level = stomach_level
        self.happiness = happiness
        self.possible_action = possible_action

        self.inventory = inventory

        self.display = display
        self.visualizer = HumanVisualizer(self)

    def run_day(self):
        self.happiness = 0
        self.age += 1
        self.stomach_level -= 1

        best_action = self.find_best_action()(self)
        self.last_action = best_action
        best_action.make()

        if self.should_die():
            self.dead = True

        if self.display:
            self.visualizer.display()

    def compute_happiness(self):
        if self.should_die():
            self.happiness = -100
            return

        self.happiness += 10 * self.stomach_level
        self.happiness += self.money
        for item in self.inventory:
            self.happiness += item.ESTIMATED_VALUE

    def __str__(self):
        return self.name

    def should_die(self):
        if self.stomach_level < 0:
            return True
        return False

    def find_best_action(self):
        return max(
            self.possible_action,
            key=lambda action: self.compute_action_happiness(action)
        )

    def compute_action_happiness(self, action):
        copy = self.copy()
        action(copy).run()
        copy.compute_happiness()
        return copy.happiness

    def copy(self):
        return Human(
            money=self.money,
            stomach_level=self.stomach_level,
            happiness=self.happiness,
            possible_action=self.possible_action.copy(),
            inventory=self.inventory.copy()
        )

    def gain_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            raise f"{item} not in {self} possession"
