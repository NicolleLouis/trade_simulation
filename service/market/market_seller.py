from models.trading.offer import Offer


class MarketSellerService:
    def __init__(
            self,
            market_service,
    ):
        self.market_service = market_service
        self.market = market_service.market
        self.human = market_service.human
        self.inventory = market_service.human.inventory

    def sell(self):
        for item in self.inventory:
            self.market.add_to_offer_book(
                Offer(
                    seller=self.human,
                    price=self.market_service.get_utility(item) + 1,
                    item=item
                )
            )
