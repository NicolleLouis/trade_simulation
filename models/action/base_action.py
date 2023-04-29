from abc import ABC, abstractmethod


class BaseAction(ABC):
    NAME = None
    RANDOM = None

    def __init__(self, job):
        self.job = job
        self.human = job.human
        self.display = job.human.display
        if self.RANDOM is None:
            raise BaseException("Specify randomness")
        self.random = self.RANDOM

    def run(self):
        try:
            self.make()
            if self.display:
                self.describe()
        except:
            if self.display:
                print(f"{self.job.human}: {self} failed")
            pass

    @abstractmethod
    def expected_happiness(self):
        raise NotImplementedError

    @abstractmethod
    def make(self):
        raise NotImplementedError

    @abstractmethod
    def describe(self):
        raise NotImplementedError

    def __str__(self):
        if self.NAME is None:
            raise f'Name was not specified'

        return f'{self.NAME}'
