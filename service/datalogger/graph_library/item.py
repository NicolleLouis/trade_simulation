from service.datalogger.logic.graph import Graph


class Item(Graph):
    TITLE = "Item"
    X_LABEL = "Days"
    Y_LABEL = "Item Number"
    FILE_ADDRESS = "item"

    def fetch_data(self):
        item_number = {}

        for human in self.world.humans:
            for item in human.inventory:
                item_name = item.NAME
                if item_name not in item_number:
                    item_number[item_name] = 0
                item_number[item_name] += 1

        for item, number_of_item in item_number.items():
            self.add_point(item, self.day(), number_of_item)
