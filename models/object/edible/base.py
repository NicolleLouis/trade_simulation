from abc import ABC
from math import inf

from models.object.base import BaseObject


class BaseEdible(BaseObject, ABC):
    EDIBLE = True
    FOOD_RETURN = 0
    DESTROYABLE = True
    DESTROY_PROBABILITY = 1

    def __init__(self):
        super().__init__()

        self.edible = self.EDIBLE
        self.food_return = self.FOOD_RETURN

    # 10 utility per consumable food + 5 utility per non-consumable food
    # Infinite value if the human is starving
    def utility(self, human):
        if human.stomach_level == 0:
            return inf
        utility = 5 * self.FOOD_RETURN
        utility += 5 * min([
            human.MAXIMUM_STOMACH_LEVEL - human.stomach_level,
            self.FOOD_RETURN
        ])
        return utility
