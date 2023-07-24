from service.datalogger.logic.plot_data import PlotData


class GraphData:
    def __init__(self, x_label, y_label, title):
        # dataset: {
        #     label = PlotData
        # }
        self.dataset = {}
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def add_point(self, label, x, y):
        if label not in self.dataset:
            self.dataset[label] = PlotData(label)
        self.dataset[label].add_point(x, y)

    def remove_plot_data(self, label):
        self.dataset.pop(label, None)
