from models.action.base_action import BaseAction


class Idle(BaseAction):
    def make(self):
        print(f"{self.human.name} is peace chilling")
