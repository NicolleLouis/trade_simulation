from abc import ABC, abstractmethod

from service.datalogger.logic.datalogger import Datalogger


class Text(Datalogger, ABC):
    TITLE = None
    FILE_ADDRESS = None

    def __init__(self, game):
        super().__init__(game)
        self.messages = []

    def file_address(self):
        return f"datalog/text/{self.FILE_ADDRESS}.txt"

    def display(self):
        self.clean()
        self.hook_pre_save()
        [print(message) for message in self.messages]

    def save(self):
        self.clean()
        self.hook_pre_save()
        file = open(self.file_address(), 'w')
        file.write('\n'.join(self.messages))
        file.close()

    def add_day_infos(self):
        self.messages.append("###")
        self.messages.append(f'Day: {self.day()}')

    def add_input(self, inputs):
        if inputs is None:
            return
        if isinstance(inputs, str):
            self.messages.append(inputs)
        elif isinstance(inputs, list):
            for smaller_input in inputs:
                self.add_input(smaller_input)

    def add_point(self, inputs):
        self.add_day_infos()
        self.add_input(inputs)

    def clean(self):
        self.messages = [message for message in self.messages if message is not None]

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
