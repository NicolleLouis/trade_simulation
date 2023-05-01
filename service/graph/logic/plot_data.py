class PlotData:
    def __init__(self, label: str):
        self.x = []
        self.y = []
        self.label = label

    def add_point(self, x, y):
        self.x.append(x)
        self.y.append(y)
