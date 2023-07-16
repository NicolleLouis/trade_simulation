
from service.graph.logic.datalogger import DataLogger


class MarketPrice(DataLogger):
    TITLE = "Average Market Price"
    X_LABEL = "Days"
    Y_LABEL = "Price"
    FILE_ADDRESS = "market_price"

    def __init__(self, world):
        super().__init__()
        self.world = world
        self.tracker = world.market.tracker

    def fetch_data(self):
        day = self.world.day
        average_prices = self.tracker.average_prices(is_accepted=True)

        for item_class in average_prices:
            mean_price = average_prices[item_class]
            if mean_price is not None:
                self.add_point(item_class.NAME, day, average_prices[item_class])
