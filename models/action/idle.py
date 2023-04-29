from models.action.base_action import BaseAction


class Idle(BaseAction):
    NAME = "CHILLING"

    def make(self):
        self.human.happiness += 5

    def describe(self):
        print(f"{self.human.name} is peace chilling")
