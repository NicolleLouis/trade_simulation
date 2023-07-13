from statistics import mean

from service.market.tracker import MarketTrackerService
from service.visualizer.base_visualizer import BaseVisualizer


class MarketVisualizer(BaseVisualizer):
    def __init__(self, market):
        super().__init__(market.world.display_level)
        self.market = market
        self.trade_book = market.trade_book
        self.tracker_service = MarketTrackerService(self.market)

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
            print(f"{str(item_class())}:")
            print(self.tracker_service.item_analysis(item_class))
