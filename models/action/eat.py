from models.action.base_action import BaseAction
from models.object.base_object import BaseObject


class Eat(BaseAction):
    NAME = "EATING"
    RANDOM = False

    def __init__(self, job):
        super().__init__(job)
        self.owned_food = None
        self.initial_stomach_level = self.human.stomach_level
        self.food_eaten = []
        self.maximum_optimal_food = None
        self.has_eaten = False
        self.has_eaten_suboptimally = False

    def make(self):
        self.detect_food()
        self.clean()
        self.detect_maximum_optimal_food()

        self.eat_until_full()
        if not self.has_eaten:
            self.suboptimal_eating()

    def describe(self):
        food_eaten_description = ", ".join([str(food) for food in self.food_eaten])
        print(f"{self.human} has eaten: {food_eaten_description}")
        print(f"He went from {self.initial_stomach_level} to {self.human.stomach_level}")
        if self.has_eaten_suboptimally:
            print("This consumption was suboptimal")

    def clean(self):
        self.food_eaten = []
        self.initial_stomach_level = self.human.stomach_level

    def detect_food(self):
        self.owned_food = list(
            filter(
                lambda item: item.edible,
                self.human.inventory
            )
        )
        if len(self.owned_food) == 0:
            raise BaseException(f"No edible food owned by {self.human}")

    def detect_maximum_optimal_food(self):
        self.maximum_optimal_food = self.human.MAXIMUM_STOMACH_LEVEL - self.human.stomach_level

    def eat(self, item: BaseObject):
        if not item.edible:
            raise f"{item} not edible"

        self.has_eaten = True
        self.human.stomach_level = min([
            self.human.stomach_level + item.FOOD_RETURN,
            self.human.MAXIMUM_STOMACH_LEVEL
        ])
        self.human.remove_item(item)
        self.food_eaten.append(item)

    def eat_until_full(self):
        for food in self.owned_food:
            if food.FOOD_RETURN <= self.maximum_optimal_food:
                self.eat(food)
                self.detect_maximum_optimal_food()

    def suboptimal_eating(self):
        smallest_food = min(
            self.owned_food,
            key=lambda food: food.FOOD_RETURN
        )
        self.eat(smallest_food)
        self.has_eaten_suboptimally = True

    def expected_happiness(self):
        return 0
