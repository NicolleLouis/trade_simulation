from statistics import mean


class MarketTrackerService:
    def __init__(self, market):
        self.trade_book = market.trade_book

    def average_prices(self):
        average_prices = {}
        for item_class in self.trade_book:
            trades = self.trade_book[item_class]
            prices = list(
                map(
                    lambda trade: trade.price,
                    trades
                )
            )
            if len(prices) == 0:
                average_prices[item_class] = None
            else:
                average_prices[item_class] = round(mean(prices), 2)
        return average_prices
