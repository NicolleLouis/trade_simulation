from models.action.base import BaseAction


class Idle(BaseAction):
    NAME = "CHILLING"
    RANDOM = False

    def make(self):
        pass

    def clean_data(self):
        pass

    def describe_lite(self):
        pass

    def describe_full(self):
        return f"{str(self.job.human)} is peace chilling"

    def expected_happiness(self):
        return 1
