from models.trading.estimated_offer import EstimatedOffer


class MarketBuyerService:
    def __init__(
            self,
            market_service,
    ):
        self.market_service = market_service
        self.market = market_service.market
        self.human = market_service.human
        self.available_offers = []
        self.estimated_offers = []

    def run(self):
        self.clean_data()
        self.buy()

    def clean_data(self):
        self.available_offers = []
        self.update_available_offers()
        self.estimated_offers = []
        self.update_estimated_offers()

    def update_available_offers(self):
        for item in self.market.offer_book:
            item_available_offer = [
                offer for offer in self.market.offer_book[item] if offer.price <= self.human.money
            ]
            self.available_offers.extend(item_available_offer)

    def update_estimated_offers(self):
        for offer in self.available_offers:
            item_utility = self.market_service.get_utility(offer.item.__class__)
            if item_utility > offer.price:
                self.estimated_offers.append(
                    EstimatedOffer(
                        offer,
                        item_utility - offer.price
                    )
                )
        self.estimated_offers.sort(
            key=lambda estimated_offer: estimated_offer.utility_gain,
            reverse=True
        )

    def buy(self):
        for estimated_offer in self.estimated_offers:
            if self.human.money >= estimated_offer.offer.price:
                self.market.trade(estimated_offer.offer, self.human)
            else:
                break
