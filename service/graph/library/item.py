from service.graph.logic.datalogger import DataLogger


class Item(DataLogger):
    TITLE = "Item"
    X_LABEL = "Days"
    Y_LABEL = "Item Number"
    FILE_ADDRESS = "item"

    def __init__(self, world):
        super().__init__()
        self.world = world

    def fetch_data(self):
        day = self.world.day

        item_number = {}

        for human in self.world.humans:
            for item in human.inventory:
                item_name = item.NAME
                if item_name not in item_number:
                    item_number[item_name] = 0
                item_number[item_name] += 1

        for item, number_of_item in item_number.items():
            self.add_point(item, day, number_of_item)
