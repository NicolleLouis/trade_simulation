class Trade:
    def __init__(self, price, day, item, is_accepted):
        self.price = price
        self.day = day
        self.item = item
        self.is_accepted = is_accepted

    def __str__(self):
        return f'{self.item} at {self.price}'
