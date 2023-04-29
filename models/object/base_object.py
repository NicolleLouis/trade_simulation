class BaseObject:
    NAME = None
    COOKABLE = False
    EDIBLE = False
    FOOD_RETURN = 0
    ESTIMATED_VALUE = 0

    def __init__(self):
        self.cookable = self.COOKABLE
        self.edible = self.EDIBLE

    def __str__(self):
        if self.NAME is None:
            raise "Name should be defined at class level"

        return self.NAME

    def cook(self):
        if not self.COOKABLE:
            raise f"{self} is not cookable"

        self.edible = True
        self.cookable = False
