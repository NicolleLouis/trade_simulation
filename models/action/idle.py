from models.action.base_action import BaseAction


class ActionIdle(BaseAction):
    def make(self):
        print(f"{self.human.name} is peach chilling")
