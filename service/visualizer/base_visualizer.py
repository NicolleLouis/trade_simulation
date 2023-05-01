from abc import ABC, abstractmethod


class BaseVisualizer(ABC):
    # Display Level: choose the level of detail displayed
    # 0 -> Nothing
    # 1 -> Lite
    # 2 -> Full
    DISPLAY_LEVEL = 0

    def __init__(self, display_level=DISPLAY_LEVEL):
        self.display_level = display_level

    def config(self, display_level):
        match display_level:
            case 0:
                return None
            case 1:
                return self.config_lite()
            case 2:
                return self.config_full()

    def display(self, display_level=None):
        if display_level is None:
            display_level = self.display_level

        config = self.config(display_level)
        if config is None:
            return

        for display_function in config:
            display_function()

        self.end_of_display()

    @staticmethod
    def end_of_display():
        print("#######")

    @abstractmethod
    def config_lite(self):
        raise NotImplementedError

    @abstractmethod
    def config_full(self):
        raise NotImplementedError
