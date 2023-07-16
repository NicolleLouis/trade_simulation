from statistics import fmean

from models.trading.market_statistic import MarketStatistic


class MarketTrackerService:
    def __init__(self, market):
        self.trade_book = market.trade_book
        self.stats_book = {}

    def clean_data(self):
        self.stats_book = {}

    def get_prices(self, item_class, is_accepted):
        if item_class not in self.trade_book:
            return []
        trades = self.trade_book[item_class]
        is_accepted_trades = list(
            filter(
                lambda trade: trade.is_accepted == is_accepted,
                trades
            )
        )
        prices = list(
            map(
                lambda trade: trade.price,
                is_accepted_trades
            )
        )
        prices = [price for price in prices if price is not None]
        return prices

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
            stats = MarketStatistic(
                item_class=item_class,
                average_sold=self.average_price(item_class, is_accepted=True),
                average_rejected=self.average_price(item_class, is_accepted=False),
                maximum_sold=self.maximum_price(item_class, is_accepted=True),
                maximum_rejected=self.maximum_price(item_class, is_accepted=False),
                minimum_sold=self.minimum_price(item_class, is_accepted=True),
                minimum_rejected=self.minimum_price(item_class, is_accepted=False),
                number_accepted=self.number_of_trades(item_class, is_accepted=True),
                number_rejected=self.number_of_trades(item_class, is_accepted=False),
            )
            self.stats_book[item_class] = stats
        return self.stats_book[item_class]
