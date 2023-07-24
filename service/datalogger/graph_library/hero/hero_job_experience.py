
from service.datalogger.logic.graph import Graph


class HeroJobExperience(Graph):
    TITLE = "Hero Money while alive"
    X_LABEL = "Days"
    Y_LABEL = "Money"
    FILE_ADDRESS = "hero_job_experience"

    def __init__(self, game):
        super().__init__(game)
        self.hero = self.world.hero

    def should_be_deleted(self):
        return self.game.world.hero is None

    def fetch_data(self):
        if self.hero.dead:
            return
        for job in self.hero.jobs:
            job_name = job.NAME
            if job_name == "BASIC":
                continue
            self.add_point(job_name, self.day(), job.experience)
