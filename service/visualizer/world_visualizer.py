from service.visualizer.base_visualizer import BaseVisualizer


class WorldVisualizer(BaseVisualizer):
    DISPLAY_LEVEL = 2

    def __init__(self, world, display_level=DISPLAY_LEVEL):
        super().__init__(display_level)
        self.world = world

    def config_lite(self):
        return [
            self.display_time_info,
            self.display_humans
        ]

    def config_full(self):
        return [
            self.display_time_info,
            self.display_humans,
        ]

    def display_humans(self):
        print(f'{len(self.world.humans)} humans alive')
        print(f'{len(self.world.dead_humans)} humans dead')

        if self.display_level == 2:
            self.display_detail_humans()

    def display_time_info(self):
        print(f'Day Number: {self.world.day}')

    def display_detail_humans(self):
        print("Human details")
        for human in self.world.humans:
            human.visualizer.display()

    def display_detail_dead(self):
        print("Dead details")
        for human in self.world.dead_humans:
            human.visualizer.display()
