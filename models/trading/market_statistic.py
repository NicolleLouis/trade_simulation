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
        maximum = self.add_maximum(other)
        minimum = self.add_minimum(other)
        average = self.add_average(other)
        number = self.number + other.number
        return MarketStatistic(
            maximum=maximum,
            minimum=minimum,
            average=average,
            number=number
        )

    def add_average(self, other):
        if other.number == 0:
            return self.average
        if self.number == 0:
            return other.average
        new_number = self.number + other.number
        average = ((self.number * self.average) + (other.number * other.average)) / new_number
        return round(average, 2)

    def add_maximum(self, other):
        if other.maximum is None:
            return self.maximum
        if self.maximum is None:
            return other.maximum
        return max(self.maximum, other.maximum)

    def add_minimum(self, other):
        if other.minimum is None:
            return self.minimum
        if self.minimum is None:
            return other.minimum
        return min(self.minimum, other.minimum)
