from abc import ABC, abstractmethod


class BaseObject(ABC):
    NAME = None

    def __init__(self):
        self.sanitize()

    def __str__(self):
        return self.NAME

    def sanitize(self):
        if self.NAME is None:
            raise "NAME should be defined at class level"
        self.hook_post_sanitize()

    def hook_post_sanitize(self):
        pass

    @abstractmethod
    def utility(self, human):
        raise NotImplementedError
