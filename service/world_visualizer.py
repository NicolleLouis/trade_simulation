class WorldVisualizer:
    def __init__(self, world):
        self.world = world

    def display_humans(self):
        print(f'{len(self.world.humans)} humans alive')
        print(f'{len(self.world.dead_humans)} humans dead')

    def display_time_info(self):
        print(f'Day Number: {self.world.day}')

    def display(self):
        self.display_time_info()
        self.display_humans()
