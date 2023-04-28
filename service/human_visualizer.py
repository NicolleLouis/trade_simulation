class HumanVisualizer:
    def __init__(self, human):
        self.human = human

    def display(self):
        print(f'{self.human.name}: {self.human.stomach_level} food left - {self.human.age} old')
