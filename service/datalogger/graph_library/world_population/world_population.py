from service.datalogger.logic.graph import Graph


class WorldPopulation(Graph):
    TITLE = "World Population"
    X_LABEL = "Days"
    Y_LABEL = "Human Number"
    FILE_ADDRESS = "world_population"

    ALIVE_LABEL = "Alive"
    DEAD_LABEL = "Dead"

    def fetch_data(self):
        self.add_point(self.ALIVE_LABEL, self.day(), len(self.world.humans))
        self.add_point(self.DEAD_LABEL, self.day(), len(self.world.dead_humans))
