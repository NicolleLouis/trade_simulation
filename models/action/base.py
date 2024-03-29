from abc import ABC, abstractmethod


class BaseAction(ABC):
    NAME = None
    RANDOM = None
    EXPERIENCE_GAIN = 1
    OBJECT = None

    def __init__(self, job):
        self.job = job
        self.human = job.human
        self.display_level = job.human.display_level
        if self.RANDOM is None:
            raise BaseException("RANDOM not specified")
        self.random = self.RANDOM

    def run(self):
        self.clean_data()
        try:
            self.make()
            self.describe()
        except:
            if self.display_level > 0:
                print(f"{self.job.human}: {self} failed")

    def describe(self, display_level=None):
        if display_level is None:
            display_level = self.display_level
        match display_level:
            case 1:
                return [self.NAME, self.describe_lite()]
            case 2:
                return [self.NAME, self.describe_full()]

    @abstractmethod
    def expected_happiness(self):
        raise NotImplementedError

    @abstractmethod
    def clean_data(self):
        raise NotImplementedError

    @abstractmethod
    def make(self):
        raise NotImplementedError

    @abstractmethod
    def describe_lite(self):
        raise NotImplementedError

    @abstractmethod
    def describe_full(self):
        raise NotImplementedError

    def improve_job(self):
        self.job.gain_experience(self.EXPERIENCE_GAIN)

    def __str__(self):
        if self.NAME is None:
            raise BaseException('NAME not specified')

        return f'{self.NAME}'
