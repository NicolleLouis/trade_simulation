from service.datalogger.logic.graph import Graph


class WorldPopulationJob(Graph):
    TITLE = "World Population By Profile"
    X_LABEL = "Days"
    Y_LABEL = "Human Number"
    FILE_ADDRESS = "world_population_job"

    def fetch_data(self):
        human_by_job = {}

        for human in self.world.humans:
            for job in human.jobs:
                job_name = job.NAME
                if job_name == "BASIC":
                    continue
                if job_name not in human_by_job:
                    human_by_job[job_name] = 0
                human_by_job[job_name] += 1

        for job, number_of_human in human_by_job.items():
            self.add_point(job, self.day(), number_of_human)
