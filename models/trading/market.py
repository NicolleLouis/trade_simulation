from models.trading.trade import Trade
from service.market.tracker import MarketTrackerService
from service.visualizer.market_visualizer import MarketVisualizer


class Market:
    def __init__(self, world):
        self.world = world
        # books are organized like:
        # {
        #     item_class: [list_of: trades/offers]
        # }
        self.offer_book = {}
        self.trade_book = {}
        self.tracker = MarketTrackerService(self)

        self.visualizer = MarketVisualizer(self)

    def trade(self, offer, buyer):
        if not self.is_trade_valid(offer, buyer):
            raise BaseException("Illegal purchase")

        self.remove_from_offer_book(offer, buyer)
        self.transfer_item(offer, buyer)
        self.transfer_money(offer, buyer)
        self.add_to_trade_book(offer, is_accepted = True)

    @staticmethod
    def is_trade_valid(offer, buyer):
        return buyer.money >= offer.price

    @staticmethod
    def transfer_item(offer, buyer):
        offer.seller.remove_item(offer.item)
        buyer.gain_item(offer.item)

    @staticmethod
    def transfer_money(offer, buyer):
        buyer.money -= offer.price
        offer.seller.money += offer.price

    def add_to_trade_book(self, offer, is_accepted):
        if offer.item.__class__ not in self.trade_book:
            self.trade_book[offer.item.__class__] = [Trade(
                price=offer.price,
                day=self.world.day,
                item=offer.item.__class__,
                is_accepted=is_accepted,
            )]
        else:
            self.trade_book[offer.item.__class__].append(
                Trade(
                    price=offer.price,
                    day=self.world.day,
                    item=offer.item.__class__,
                    is_accepted=is_accepted,
                )
            )

    def add_to_offer_book(self, offer):
        if offer.item.__class__ not in self.offer_book:
            self.offer_book[offer.item.__class__] = [offer]
        else:
            self.offer_book[offer.item.__class__].append(offer)

    def remove_from_offer_book(self, offer, buyer):
        self.offer_book[offer.item.__class__].remove(offer)
