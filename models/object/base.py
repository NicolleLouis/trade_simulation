from abc import ABC, abstractmethod


class BaseObject(ABC):
    NAME = None

    def __str__(self):
        if self.NAME is None:
            raise "Name should be defined at class level"

        return self.NAME

    @abstractmethod
    def utility(self, human):
        raise NotImplementedError
