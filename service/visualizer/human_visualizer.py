from service.visualizer.base_visualizer import BaseVisualizer


class HumanVisualizer(BaseVisualizer):
    def __init__(self, human):
        super().__init__(human.display_level)
        self.human = human

    def config_lite(self):
        return [
            self.display_basic,
            self.display_market_behaviour,
            self.display_health_infos,
        ]

    def config_full(self):
        return [
            self.display_basic,
            self.display_market_behaviour,
            self.display_last_action,
            self.display_health_infos,
            self.display_inventory,
            self.display_jobs,
        ]

    def display_basic(self):
        print(f'{str(self.human)}: ')

    def display_market_behaviour(self):
        print(f'Behaviour: {self.human.profile.name}')

    def display_last_action(self):
        print(f'Last action: {str(self.human.last_action)}')

    def display_health_infos(self):
        print(f'Stomach level: {self.human.stomach_level}')
        print(f'Age: {self.human.age}')

    def display_inventory(self):
        print(f'Available Money: {self.human.money}')
        match self.display_level:
            case 1:
                print(f'Inventory size: {len(self.human.inventory)}')
            case 2:
                inventory = ", ".join([str(item) for item in self.human.inventory])
                print(f'Inventory: {inventory}')

    def display_jobs(self):
        for job in self.human.jobs:
            self.display_job(job)

    @staticmethod
    def display_job(job):
        print(f'{str(job)}: lvl {job.level} ({job.experience})')
