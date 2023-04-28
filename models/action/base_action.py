class BaseAction:
    def __init__(self, human):
        self.human = human

    def make(self):
        raise NotImplementedError
