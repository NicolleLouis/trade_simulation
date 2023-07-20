class MarketStatistic:
    def __init__(
            self,
            average,
            maximum,
            minimum,
            number,
    ):
        self.average = average
        self.maximum = maximum
        self.minimum = minimum
        self.number = number

    def is_empty(self):
        return self.number == 0

    def display(self):
        print(f"Average: {self.average}€")
        print(f"Min/Max: {self.minimum}/{self.maximum}€")
        print(f"Number: {self.number}")

    def __add__(self, other):
        self.maximum = max(self.maximum, other.maximum)
        self.maximum = max(self.maximum, other.maximum)
        new_number = self.number + other.number
        self.average = ((self.number * self.average) + (other.number * other.average))/new_number
        self.number = new_number
