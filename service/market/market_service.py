from service.market.market_buyer import MarketBuyerService
from service.market.market_seller import MarketSellerService


class MarketService:
    def __init__(
            self,
            market,
            human
    ):
        self.market = market
        self.human = human
        self.buyer_service = MarketBuyerService(self)
        self.seller_service = MarketSellerService(self)
        # Utility book is a dictionary of item type: utility of the item
        self.utility_book = {}

    def buy(self):
        self.clean_data()
        self.buyer_service.run()

    def sell(self):
        self.seller_service.sell()

    def remove_all_offers(self):
        for item_class in self.market.offer_book:
            self.market.offer_book[item_class] = list(
                filter(
                    lambda offer: offer.seller != self.human,
                    self.market.offer_book[item_class]
                )
            )

    def clean_data(self):
        self.remove_all_offers()
        self.utility_book = {}

    def add_item_to_utility_book(self, item_class):
        if item_class not in self.utility_book:
            self.utility_book[item_class] = item_class().utility(self.human)

    def get_utility(self, item):
        self.add_item_to_utility_book(item.__class__)
        return self.utility_book[item.__class__]
