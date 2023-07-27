from service.datalogger.logic.graph import Graph


class WorldPopulationSentimentalStatus(Graph):
    TITLE = "World Population By Sentimental Status"
    X_LABEL = "Days"
    Y_LABEL = "Human Number"
    FILE_ADDRESS = "world_population_sentimental_status"

    def fetch_data(self):
        human_by_sentimental_status = {}

        for human in self.world.humans:
            status = human.sentimental_life.status.name
            if status not in human_by_sentimental_status:
                human_by_sentimental_status[status] = 0
            human_by_sentimental_status[status] += 1

        for status, number_of_human in human_by_sentimental_status.items():
            self.add_point(status, self.day(), number_of_human)
