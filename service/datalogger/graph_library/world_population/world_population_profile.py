from service.datalogger.logic.graph import Graph


class WorldPopulationProfile(Graph):
    TITLE = "World Population By Profile"
    X_LABEL = "Days"
    Y_LABEL = "Human Number"
    FILE_ADDRESS = "world_population_profile"

    def fetch_data(self):
        human_by_profile = {}

        for human in self.world.humans:
            profile = human.profile.name
            if profile not in human_by_profile:
                human_by_profile[profile] = 0
            human_by_profile[profile] += 1

        for profile, number_of_human in human_by_profile.items():
            self.add_point(profile, self.day(), number_of_human)
