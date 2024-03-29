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
        # Empty caches
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

    def get_day_prices(self, item_class, is_accepted, day):
        trades = self.trade_book[item_class]
        correct_day_trades = [trade for trade in trades if trade.day == day]
        is_accepted_trades = [trade for trade in correct_day_trades if trade.is_accepted is is_accepted]
        prices = [trade.price for trade in is_accepted_trades]
        return [price for price in prices if price is not None]

    def average_prices(self, is_accepted):
        averages = {}
        for item_class in self.trade_book:
            accepted_prices = self.get_prices(item_class, is_accepted=is_accepted)
            averages[item_class] = self.average_price(accepted_prices)
        return averages

    @staticmethod
    def average_price(prices):
        if len(prices) == 0:
            return None
        return round(fmean(prices), 2)

    @staticmethod
    def maximum_price(prices):
        if len(prices) == 0:
            return None
        return max(prices)

    @staticmethod
    def number_of_trades(prices):
        return len(prices)

    @staticmethod
    def minimum_price(prices):
        if len(prices) == 0:
            return None
        return min(prices)

    def generate_item_market_statistic(self, item_class, accepted_prices, rejected_prices):
        accepted = MarketStatistic(
            average=self.average_price(accepted_prices),
            maximum=self.maximum_price(accepted_prices),
            minimum=self.minimum_price(accepted_prices),
            number=self.number_of_trades(accepted_prices),
        )
        rejected = MarketStatistic(
            average=self.average_price(rejected_prices),
            maximum=self.maximum_price(rejected_prices),
            minimum=self.minimum_price(rejected_prices),
            number=self.number_of_trades(rejected_prices),
        )
        return ItemMarketStatistic(
            item_class=item_class,
            accepted_statistics=accepted,
            rejected_statistics=rejected,
        )

    def item_analysis(self, item_class) -> MarketStatistic:
        if item_class not in self.stats_book:
            accepted_prices = self.get_prices(item_class, is_accepted=True)
            rejected_prices = self.get_prices(item_class, is_accepted=False)
            stats = self.generate_item_market_statistic(
                item_class=item_class,
                accepted_prices=accepted_prices,
                rejected_prices=rejected_prices
            )
            self.stats_book[item_class] = stats
        return self.stats_book[item_class]

    def get_day_analysis(self, item_class, day):
        accepted_prices = self.get_day_prices(
            item_class=item_class,
            day=day,
            is_accepted=True,
        )
        rejected_prices = self.get_day_prices(
            item_class=item_class,
            day=day,
            is_accepted=False,
        )
        return self.generate_item_market_statistic(
            item_class=item_class,
            accepted_prices=accepted_prices,
            rejected_prices=rejected_prices
        )

    def remove_day(self, item_class, day):
        self.trade_book[item_class] = [
            trade for trade in self.trade_book[item_class] if trade.day != day
        ]
