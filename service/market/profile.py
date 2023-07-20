import random
from math import inf

from constants.profile_type import ProfileType
from models.trading.item_market_statistics import ItemMarketStatistic


class ProfileService:
    def __init__(
            self,
            market_service,
    ):
        self.market_service = market_service
        self.market = market_service.market
        self.human = market_service.human

        self.tracker_service = self.market.tracker

    # Return (min, max) value of an item
    def get_interval(self, intrinsic_value, item_market_stats):
        if item_market_stats.accepted_statistics.is_empty():
            min_price, max_price = self.get_empty_interval(intrinsic_value)
        else:
            min_price, max_price = self.get_real_interval(
                intrinsic_value=intrinsic_value,
                item_market_stats=item_market_stats,
            )

        max_price = max(min_price, max_price)
        return min_price, max_price

    def get_empty_interval(self, intrinsic_value):
        min_price = None
        max_price = None

        match self.human.profile:
            case ProfileType.CAREFUL:
                min_price = intrinsic_value
                max_price = intrinsic_value
            case ProfileType.NORMAL:
                min_price = intrinsic_value
                max_price = intrinsic_value
            case ProfileType.ADVENTUROUS:
                min_price = intrinsic_value
                max_price = intrinsic_value * 2
        return min_price, max_price

    def get_real_interval(self, intrinsic_value, item_market_stats: ItemMarketStatistic):
        min_price = None
        max_price = None
        accepted_stats = item_market_stats.accepted_statistics
        rejected_stats = item_market_stats.rejected_statistics

        match self.human.profile:
            case ProfileType.CAREFUL:
                min_price = intrinsic_value
                max_price = accepted_stats.average
            case ProfileType.NORMAL:
                min_price = max(intrinsic_value, accepted_stats.minimum)
                max_price = accepted_stats.maximum
            case ProfileType.ADVENTUROUS:
                min_price = max(intrinsic_value, accepted_stats.average)
                if rejected_stats.is_empty():
                    max_price = accepted_stats.maximum*2
                else:
                    max_price = min(
                        accepted_stats.maximum * 2,
                        rejected_stats.average
                    )
        return min_price, max_price

    def get_price(self, item_class, money_need=None):
        if money_need is None:
            money_need = random.random()
        if money_need < 0 or money_need > 1:
            raise BaseException(f'Money need should be a positive ratio: {money_need}')

        intrinsic_value = self.market_service.get_utility(item_class)
        item_market_stats = self.tracker_service.item_analysis(item_class)

        if intrinsic_value == inf:
            return None

        min_price, max_price = self.get_interval(intrinsic_value, item_market_stats)
        price = round(min_price + money_need*(max_price - min_price), 2)
        return price
