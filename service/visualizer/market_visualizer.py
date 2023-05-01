from statistics import mean

from service.visualizer.base_visualizer import BaseVisualizer


class MarketVisualizer(BaseVisualizer):
    def __init__(self, market):
        super().__init__(market.world.display_level)
        self.market = market
        self.trade_book = market.trade_book

    def config_lite(self):
        return [
            self.display_title,
            self.display_trade_book_sum
        ]

    def config_full(self):
        return [
            self.display_title,
            self.display_trade_book_statistic
        ]

    @staticmethod
    def display_title():
        print("Market:")

    def display_trade_book_sum(self):
        for item_class in self.trade_book:
            print(f"{str(item_class())}: {len(self.trade_book[item_class])} trades")

    def display_trade_book_statistic(self):
        for item_class in self.trade_book:
            trades = self.trade_book[item_class]
            prices = list(
                map(
                    lambda trade: trade.price,
                    trades
                )
            )
            print(f"{str(item_class())}:")
            print(f"{len(trades)} trades occured")
            print(f"Average price: {round(mean(prices), 2)}")
            print(f"Maximum price: {max(prices)}")
            print(f"Minimum price: {min(prices)}")
