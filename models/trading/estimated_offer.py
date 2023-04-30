from models.trading.offer import Offer


class EstimatedOffer:
    def __init__(
            self,
            offer: Offer,
            utility_gain: float,
    ):
        self.offer = offer
        self.utility_gain = utility_gain
