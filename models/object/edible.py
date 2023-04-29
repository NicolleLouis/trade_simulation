from abc import ABC

from models.object.base_object import BaseObject


class BaseEdible(BaseObject, ABC):
    EDIBLE = True
    FOOD_RETURN = 0

    def __init__(self):
        self.edible = self.EDIBLE
        self.food_return = self.FOOD_RETURN

    # 10 utility per consumable food + 5 utility per non consumbale food
    def utility(self, human):
        utility = 5 * self.FOOD_RETURN
        utility += 5 * min([
            human.MAXIMUM_STOMACH_LEVEL - human.stomach_level,
            self.FOOD_RETURN
        ])
        return utility
