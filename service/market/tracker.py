from statistics import mean


class MarketTrackerService:
    def __init__(self, market):
        self.trade_book = market.trade_book

    def get_prices(self, item_class, is_accepted):
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
        return prices

    def average_price(self, item_class, is_accepted):
        prices = self.get_prices(item_class, is_accepted)
        if len(prices) == 0:
            return None
        return round(mean(prices), 2)

    def average_prices(self, is_accepted):
        average_prices = {}
        for item_class in self.trade_book:
            average_prices[item_class] = self.average_price(item_class, is_accepted)
        return average_prices

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

    def item_analysis(self, item_class):
        return {
            "average_sold": self.average_price(item_class, is_accepted=True),
            "average_rejected": self.average_price(item_class, is_accepted=False),
            "maximum_sold": self.maximum_price(item_class, is_accepted=True),
            "maximum_rejected": self.maximum_price(item_class, is_accepted=False),
            "minimum_sold": self.minimum_price(item_class, is_accepted=True),
            "minimum_rejected": self.minimum_price(item_class, is_accepted=False),
            "number_accepted": self.number_of_trades(item_class, is_accepted=True),
            "number_rejected": self.number_of_trades(item_class, is_accepted=False),
        }
