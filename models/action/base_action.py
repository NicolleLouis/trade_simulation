

class BaseAction:
    NAME = None

    def __init__(self, human):
        self.human = human

    def run(self, display=False):
        try:
            self.make()
            if display:
                self.describe()
        except:
            if display:
                print(f"{self.human}: {self} failed")
            pass

    def make(self):
        raise NotImplementedError

    def describe(self):
        raise NotImplementedError

    def __str__(self):
        if self.NAME is None:
            raise f'Name was not specified'

        return f'{self.NAME}'
