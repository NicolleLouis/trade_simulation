from service.market.buyer import MarketBuyerService
from service.market.profile import ProfileService
from service.market.seller import MarketSellerService


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
        self.profile_service = ProfileService(self)

        # Utility book is a dictionary of item type: utility of the item
        self.utility_book = {}

    def buy(self):
        self.clean_data()
        self.buyer_service.run()

    def sell(self):
        self.seller_service.sell()

    def remove_all_offers(self):
        for item_class in self.market.offer_book:
            self.track_rejected_offers(item_class)
            self.market.offer_book[item_class] = [
                offer for offer in self.market.offer_book[item_class] if offer.seller != self.human
            ]

    def track_rejected_offers(self, item_class):
        rejected_offers = [
            offer for offer in self.market.offer_book[item_class] if offer.seller == self.human
        ]
        for offer in rejected_offers:
            self.market.add_to_trade_book(offer, is_accepted=False)

    def clean_data(self):
        self.remove_all_offers()
        self.utility_book = {}

    def add_item_to_utility_book(self, item_class):
        if item_class not in self.utility_book:
            if item_class().utility(self.human) is None:
                self.utility_book[item_class] = 0
            else:
                self.utility_book[item_class] = round(item_class().utility(self.human), 2)

    def get_utility(self, item_class):
        self.add_item_to_utility_book(item_class)
        return self.utility_book[item_class]
