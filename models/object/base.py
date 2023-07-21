from abc import ABC, abstractmethod


class BaseObject(ABC):
    NAME = None
    DESTROYABLE = False
    DESTROY_PROBABILITY = None

    def __init__(self):
        self.edible = False
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

    def destroy_probability(self):
        if not self.DESTROYABLE:
            return None
        else:
            return self.DESTROY_PROBABILITY/100
