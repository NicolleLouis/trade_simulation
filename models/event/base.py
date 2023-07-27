import random
from abc import ABC, abstractmethod


class Event(ABC):
    NAME = None
    COOLDOWN = None
    BASE_PROBA = None

    def __init__(self):
        self.sanitize()
        self.time_since_activation = 0

    @abstractmethod
    def activation_condition(self):
        return True

    @abstractmethod
    def activation(self):
        raise NotImplementedError

    def run(self):
        self.time_since_activation += 1
        if self.time_since_activation < self.COOLDOWN:
            return False
        elif not self.activation_condition():
            return False
        elif not random.random() < self.BASE_PROBA:
            return False

        # Case everything is valid
        self.time_since_activation = 0
        self.activation()
        return True

    def sanitize(self):
        if self.NAME is None:
            raise BaseException('NAME not specified')
        if self.COOLDOWN is None:
            raise BaseException('COOLDOWN not specified')
        if self.BASE_PROBA is None:
            raise BaseException('BASE_PROBA not specified')
