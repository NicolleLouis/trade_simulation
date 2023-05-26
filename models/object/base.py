from abc import ABC, abstractmethod


class BaseObject(ABC):
    NAME = None
    JOB_CREATING = None
    JOB_USING = None

    def __init__(self):
        self.sanitize()

    def __str__(self):
        return self.NAME

    def sanitize(self):
        if self.NAME is None:
            raise "NAME should be defined at class level"
        if self.JOB_CREATING is None:
            raise "JOB_CREATING should be defined at class level"
        if self.JOB_USING is None:
            raise "JOB_USING should be defined at class level"
        self.hook_post_sanitize()

    def hook_post_sanitize(self):
        pass

    @abstractmethod
    def utility(self, human):
        raise NotImplementedError
