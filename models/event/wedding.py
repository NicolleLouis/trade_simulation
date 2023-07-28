from models.event.base import Event


class Wedding(Event):
    NAME = "Wedding"
    BASE_PROBA = 50
    COOLDOWN = 5

    def __init__(self, world, **kwargs):
        super().__init__(**kwargs)

        self.potential_brides = []
        self.potential_male = []
        self.potential_female = []

        self.world = world

    def activation(self):
        if not self.can_match():
            raise BaseException("Should not have reached this")
        male = self.potential_male.pop()
        female = self.potential_female.pop()
        male.sentimental_life.wed(female)

    def activation_condition(self):
        if self.can_match():
            return True
        self.get_potential_brides()
        return False

    def get_potential_brides(self):
        self.potential_brides = [
            human for human in self.world.humans if human.sentimental_life.can_wed()
        ]
        self.potential_male = [
            human for human in self.potential_brides if human.is_male
        ]
        self.potential_female = [
            human for human in self.potential_brides if not human.is_male
        ]

    def can_match(self):
        return len(self.potential_male) > 0 and len(self.potential_female) > 0
