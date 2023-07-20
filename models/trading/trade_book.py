from models.trading.trade import Trade


class TradeBook:
    NUMBER_OF_DAYS = 30

    def __init__(self, market):
        # Only contains trades from the last NUMBER_OF_DAYS days
        # {
        #     item_class: [list_of: trades]
        # }
        self.detailed_book = {}
        # Contains a concatenated version of the past trades (Before NUMBER_OF_DAYS)
        # {
        #       item_class: {
        #               accepted: market_stats
        #               rejected: market_stats
        #       }
        # }
        #
        self.past_stats = {}
        self.market = market

    def add_to_trade_book(self, offer, is_accepted):
        item_class = offer.item.__class__
        if item_class not in self.detailed_book:
            self.detailed_book[item_class] = []
        self.detailed_book[item_class].append(
            Trade(
                price=offer.price,
                day=self.day(),
                item=item_class,
                is_accepted=is_accepted,
            )
        )

    def day(self):
        return self.market.world.day
