from abc import ABC, abstractmethod

from service.graph.logic.graph_data import GraphData
from service.graph.logic.plot_service import PlotService


class DataLogger(ABC):
    TITLE = None
    X_LABEL = None
    Y_LABEL = None
    FILE_ADDRESS = None

    def __init__(self):
        self.sanitize()
        self.graph_data = GraphData(
            title=self.TITLE,
            x_label=self.X_LABEL,
            y_label=self.Y_LABEL,
        )

    def sanitize(self):
        if self.TITLE is None:
            raise BaseException("TITLE not implemented")
        if self.X_LABEL is None:
            raise BaseException("X_LABEL not implemented")
        if self.Y_LABEL is None:
            raise BaseException("Y_LABEL not implemented")
        if self.FILE_ADDRESS is None:
            raise BaseException("FILE_ADDRESS not implemented")

    def file_address(self):
        return f"graph/{self.FILE_ADDRESS}.png"

    def display(self):
        PlotService(
            graph_data=self.graph_data
        ).show()

    def save(self):
        PlotService(
            graph_data=self.graph_data
        ).save(self.file_address())

    def add_point(self, label, x, y):
        self.graph_data.add_point(
            label=label,
            x=x,
            y=y,
        )

    @abstractmethod
    def fetch_data(self):
        raise NotImplementedError
