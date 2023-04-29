class HumanVisualizer:
    def __init__(self, human):
        self.human = human

    def display(self):
        print(f'{self.human.name}: ')
        print(f'Last action: {str(self.human.last_action)}')
        print(f'Stomach level: {self.human.stomach_level}')
        print(f'Age: {self.human.age}')
        inventory = ", ".join([str(item) for item in self.human.inventory])
        print(f'Inventory: {inventory}')
        print("######")
