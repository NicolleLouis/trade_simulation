from matplotlib import pyplot as plt


class PlotService:
    def __init__(self, graph_data):
        self.graph_data = graph_data
        self.fig, self.ax = plt.subplots()
        self.add_graph()
        self.add_labels()

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def save(file_address):
        plt.savefig(file_address)

    def add_graph(self):
        for dataset_label in self.graph_data.dataset:
            plot_data = self.graph_data.dataset[dataset_label]
            self.ax.plot(
                plot_data.x,
                plot_data.y,
                label=plot_data.label
            )

    def add_labels(self):
        self.ax.set_xlabel(self.graph_data.x_label)
        self.ax.set_ylabel(self.graph_data.y_label)
        self.ax.set_title(self.graph_data.title)
        self.ax.legend()
