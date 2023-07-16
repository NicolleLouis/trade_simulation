from service.graph.logic.datalogger import DataLogger


class WorldPopulationProfile(DataLogger):
    TITLE = "World Population By Profile"
    X_LABEL = "Days"
    Y_LABEL = "Human Number"
    FILE_ADDRESS = "world_population_profile"

    def __init__(self, world):
        super().__init__()
        self.world = world

    def fetch_data(self):
        day = self.world.day

        human_by_profile = {}

        for human in self.world.humans:
            profile = human.profile.name
            if profile not in human_by_profile:
                human_by_profile[profile] = 0
            human_by_profile[profile] += 1

        for profile, number_of_human in human_by_profile.items():
            self.add_point(profile, day, number_of_human)
