class WeddingService:
    def __init__(self, world):
        self.potential_brides = None
        self.potential_male = None
        self.potential_female = None

        self.world = world

    def run(self):
        self.get_potential_brides()
        self.match_everyone()

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

    def match_everyone(self):
        while len(self.potential_male) > 0 and len(self.potential_female) > 0:
            male = self.potential_male.pop()
            female = self.potential_female.pop()
            male.sentimental_life.wed(female)
