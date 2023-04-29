from service.world_visualizer import WorldVisualizer


class World:
    def __init__(self):
        self.day = 0
        self.humans = []
        self.dead_humans = []
        self.visualizer = WorldVisualizer(self)

    def add_human(self, human):
        self.humans.append(human)

    def update_dead(self):
        new_dead = filter(
            lambda human: human.dead,
            self.humans
        )
        self.dead_humans.extend(new_dead)
        self.humans = list(filter(
            lambda human: not human.dead,
            self.humans,
        ))

    def run_day(self):
        self.visualizer.display()
        for human in self.humans:
            human.run_day()
        self.update_dead()
