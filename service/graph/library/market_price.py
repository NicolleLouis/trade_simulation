
from service.graph.logic.datalogger import DataLogger


class MarketPrice(DataLogger):
    TITLE = "Average Running Market Price"
    X_LABEL = "Days"
    Y_LABEL = "Price"
    FILE_ADDRESS = "market_price"

    def __init__(self, game):
        super().__init__(game)
        self.tracker = self.world.market.trade_book.detailed_book_service

    def fetch_data(self):
        average_prices = self.tracker.average_prices(is_accepted=True)

        for item_class in average_prices:
            mean_price = average_prices[item_class]
            if mean_price is not None:
                self.add_point(item_class.NAME, self.day(), average_prices[item_class])
