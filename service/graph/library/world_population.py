from service.graph.logic.datalogger import DataLogger


class WorldPopulation(DataLogger):
    TITLE = "World Population"
    X_LABEL = "Days"
    Y_LABEL = "Human Number"
    FILE_ADDRESS = "world_population"

    ALIVE_LABEL = "Alive"
    DEAD_LABEL = "Dead"

    def __init__(self, world):
        super().__init__()
        self.world = world

    def fetch_data(self):
        day = self.world.day

        self.add_point(self.ALIVE_LABEL, day, len(self.world.humans))
        self.add_point(self.DEAD_LABEL, day, len(self.world.dead_humans))
