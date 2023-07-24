from abc import ABC, abstractmethod


class Datalogger(ABC):
    TITLE = None
    FILE_ADDRESS = None

    def __init__(self, game):
        self.sanitize()
        self.game = game
        self.world = game.world

    def sanitize(self):
        if self.TITLE is None:
            raise BaseException("TITLE not implemented")
        if self.FILE_ADDRESS is None:
            raise BaseException("FILE_ADDRESS not implemented")

    @abstractmethod
    def file_address(self):
        raise NotImplementedError

    @abstractmethod
    def display(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def add_point(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def fetch_data(self):
        raise NotImplementedError

    # Hook called before saving/displaying the graph, useful to filter some dataset for example
    def hook_pre_save(self):
        pass

    # Hook called at the init, if true, it removes the graph from the game
    def should_be_deleted(self):
        return False

    def day(self):
        return self.world.day
