class MarketStatistic:
    def __init__(
            self,
            item_class,
            average_sold,
            average_rejected,
            maximum_sold,
            maximum_rejected,
            minimum_sold,
            minimum_rejected,
            number_accepted,
            number_rejected,
    ):
        self.item_class = item_class
        self.average_sold = average_sold
        self.average_rejected = average_rejected
        self.maximum_sold = maximum_sold
        self.maximum_rejected = maximum_rejected
        self.minimum_sold = minimum_sold
        self.minimum_rejected = minimum_rejected
        self.number_accepted = number_accepted
        self.number_rejected = number_rejected

    def __str__(self):
        return f'{self.item_class()} stats ({self.average_sold}€ avg)'

    def is_empty(self):
        return self.number_rejected == 0 or self.number_accepted == 0

    def display(self):
        print(f"{str(self.item_class())}:")
        print(f"Number of Trades: {self.number_accepted}")
        print(f"Average price: {self.average_sold}€")
        print(f"Max/Min accepted: {self.minimum_sold}/{self.maximum_sold}€")
        print(f"Number of offers rejected: {self.number_rejected}")
        print(f"Average price rejected: {self.average_rejected}€")
        print(f"Max/Min rejected: {self.minimum_rejected}/{self.maximum_rejected}€")
