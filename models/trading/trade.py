class Trade:
    def __init__(self, price, day, item):
        self.price = price
        self.day = day
        self.item = item

    def __str__(self):
        return f'{self.item} at {self.price}'
