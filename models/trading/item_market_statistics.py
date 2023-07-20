from models.trading.market_statistic import MarketStatistic


class ItemMarketStatistic:
    def __init__(
            self,
            item_class,
            accepted_statistics: MarketStatistic,
            rejected_statistics: MarketStatistic,
    ):
        self.item_class = item_class
        self.accepted_statistics = accepted_statistics
        self.rejected_statistics = rejected_statistics

    def display(self):
        print(f"Item: {self.item_class()}")
        print(f"Successful trades:")
        self.accepted_statistics.display()
        print(f"Refused trades:")
        self.rejected_statistics.display()
