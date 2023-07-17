import random
from math import inf

from constants.profile_type import ProfileType


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
    def get_interval(self, intrinsic_value, market_stats):
        if market_stats.is_empty():
            min_price, max_price = self.get_empty_interval(intrinsic_value)
        else:
            min_price, max_price = self.get_real_interval(
                intrinsic_value=intrinsic_value,
                market_stats=market_stats,
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

    def get_real_interval(self, intrinsic_value, market_stats):
        min_price = None
        max_price = None

        match self.human.profile:
            case ProfileType.CAREFUL:
                min_price = intrinsic_value
                max_price = market_stats.average_sold
            case ProfileType.NORMAL:
                min_price = max(intrinsic_value, market_stats.minimum_sold)
                max_price = market_stats.maximum_sold
            case ProfileType.ADVENTUROUS:
                min_price = max(intrinsic_value, market_stats.average_sold)
                max_price = min(
                    market_stats.maximum_sold * 2,
                    market_stats.average_rejected
                )
        return min_price, max_price

    def get_price(self, item_class, money_need=None):
        if money_need is None:
            money_need = random.random()
        if money_need < 0 or money_need > 1:
            raise BaseException(f'Money need should be a positive ratio: {money_need}')

        intrinsic_value = self.market_service.get_utility(item_class)
        market_stats = self.tracker_service.item_analysis(item_class)

        if intrinsic_value == inf:
            return None

        min_price, max_price = self.get_interval(intrinsic_value, market_stats)
        price = round(min_price + money_need*(max_price - min_price), 2)
        return price
