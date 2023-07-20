from statistics import fmean

from models.trading.item_market_statistics import ItemMarketStatistic
from models.trading.market_statistic import MarketStatistic


class DetailedBookService:
    def __init__(self, trade_book):
        # List all the history of trades
        self.trade_book = trade_book.detailed_book
        # Cache object
        # item_class -> stats
        self.stats_book = {}
        # Cache object
        # In charge of caching the prices from the detailed book
        self.prices_book = {}

    def clean_data(self):
        self.stats_book = {}
        self.prices_book = {}

    def generate_price_book(self, item_class, is_accepted):
        trades = self.trade_book[item_class]
        is_accepted_trades = [trade for trade in trades if trade.is_accepted is is_accepted]
        prices = [trade.price for trade in is_accepted_trades]
        self.prices_book[item_class][is_accepted] = [price for price in prices if price is not None]

    def generate_total_price_book(self, item_class):
        self.prices_book[item_class] = {}
        self.generate_price_book(item_class, True)
        self.generate_price_book(item_class, False)

    def get_prices(self, item_class, is_accepted):
        if item_class not in self.trade_book:
            return []
        if item_class not in self.prices_book:
            self.generate_total_price_book(item_class)
        return self.prices_book[item_class][is_accepted]

    def average_price(self, item_class, is_accepted):
        prices = self.get_prices(item_class, is_accepted)
        if len(prices) == 0:
            return None
        return round(fmean(prices), 2)

    def average_prices(self, is_accepted):
        averages = {}
        for item_class in self.trade_book:
            averages[item_class] = self.average_price(item_class, is_accepted)
        return averages

    def maximum_price(self, item_class, is_accepted):
        prices = self.get_prices(item_class, is_accepted)
        if len(prices) == 0:
            return None
        return max(prices)

    def number_of_trades(self, item_class, is_accepted):
        prices = self.get_prices(item_class, is_accepted)
        return len(prices)

    def minimum_price(self, item_class, is_accepted):
        prices = self.get_prices(item_class, is_accepted)
        if len(prices) == 0:
            return None
        return min(prices)

    def item_analysis(self, item_class) -> MarketStatistic:
        if item_class not in self.stats_book:
            accepted = MarketStatistic(
                average=self.average_price(item_class, is_accepted=True),
                maximum=self.maximum_price(item_class, is_accepted=True),
                minimum=self.minimum_price(item_class, is_accepted=True),
                number=self.number_of_trades(item_class, is_accepted=True),
            )
            rejected = MarketStatistic(
                average=self.average_price(item_class, is_accepted=False),
                maximum=self.maximum_price(item_class, is_accepted=False),
                minimum=self.minimum_price(item_class, is_accepted=False),
                number=self.number_of_trades(item_class, is_accepted=False),
            )
            stats = ItemMarketStatistic(
                item_class=item_class,
                accepted_statistics=accepted,
                rejected_statistics=rejected,
            )
            self.stats_book[item_class] = stats
        return self.stats_book[item_class]
