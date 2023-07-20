from models.trading.trade import Trade
from service.market.detailed_boook import DetailedBookService


class TradeBook:
    NUMBER_OF_DAYS_DETAILED = 60

    def clean_data(self):
        self.detailed_book_service.clean_data()
        self.compact_day()

    def __init__(self, market):
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
        self.detailed_book_service = DetailedBookService(self)
        # Only contains trades from the last NUMBER_OF_DAYS days
        # {
        #     item_class: [list_of: trades]
        # }

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

    def compact_day_item(self, item_class, day):
        day_statistics = self.detailed_book_service.get_day_analysis(
            item_class=item_class,
            day=day,
        )
        if item_class in self.past_stats:
            if self.past_stats[item_class] is None:
                self.past_stats[item_class] = day_statistics
            else:
                self.past_stats[item_class] = self.past_stats[item_class] + day_statistics
        else:
            self.past_stats[item_class] = day_statistics
        self.detailed_book_service.remove_day(item_class=item_class, day=day)

    def compact_day(self):
        if self.day() < self.NUMBER_OF_DAYS_DETAILED:
            return

        day_compacted = self.day() - self.NUMBER_OF_DAYS_DETAILED

        for item_class in self.detailed_book:
            self.compact_day_item(item_class=item_class, day=day_compacted)

    def get_complete_analysis(self, item_class):
        return self.past_stats[item_class] + self.detailed_book_service.item_analysis(item_class)
