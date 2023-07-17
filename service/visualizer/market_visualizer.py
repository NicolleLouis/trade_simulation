from service.market.tracker import MarketTrackerService
from service.visualizer.base_visualizer import BaseVisualizer


class MarketVisualizer(BaseVisualizer):
    def __init__(self, market):
        super().__init__(market.world.display_level)
        self.market = market
        self.trade_book = market.trade_book
        self.offer_book = market.offer_book
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
            number_of_trades = self.tracker_service.item_analysis(item_class).number_accepted
            print(f"{str(item_class())}: {number_of_trades} trades")

    def display_trade_book_statistic(self):
        for item_class in self.trade_book:
            self.tracker_service.item_analysis(item_class).display()

    def display_offers(self, human):
        for item_class, offers in self.offer_book.items():
            print(f'{item_class()}:')
            human_offers = [offer for offer in offers if offer.seller == human]
            for offer in human_offers:
                print(f'- {offer.price}')
