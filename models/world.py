class World:
    def __init__(self):
        self.day = 0
        self.humans = []
        self.dead_humans = []

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)
        self.dead_humans.append(human)

    def run_day(self):
        for human in self.humans:
            human.run_day()
            if human.dead:
                self.remove_human(human)
