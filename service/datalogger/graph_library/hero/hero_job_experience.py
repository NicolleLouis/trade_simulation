
from service.datalogger.logic.graph import Graph


class HeroJobExperience(Graph):
    TITLE = "Hero Experience"
    X_LABEL = "Days"
    Y_LABEL = "Money"
    FILE_ADDRESS = "hero_job_experience"

    def hero(self):
        return self.world.hero

    def should_be_deleted(self):
        return self.game.world.hero is None

    def fetch_data(self):
        hero = self.hero()
        if hero.dead:
            return
        for job in hero.jobs:
            job_name = job.NAME
            if job_name == "BASIC":
                continue
            self.add_point(job_name, self.day(), job.experience)
