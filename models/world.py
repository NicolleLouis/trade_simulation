import random

from models.trading.market import Market
from service.visualizer.world_visualizer import WorldVisualizer


class World:
    def __init__(self, display_level=0):
        self.display_level = display_level
        self.day = 0
        self.humans = []
        self.hero = None
        self.events = []

        self.dead_humans = []

        self.market = Market(self)

        self.visualizer = WorldVisualizer(self, display_level)

    def add_human(self, human):
        self.humans.append(human)

    def add_event(self, event):
        self.events.append(event)

    def add_hero(self, hero):
        self.add_human(hero)
        self.hero = hero

    def update_dead(self):
        new_dead = filter(
            lambda human: human.dead,
            self.humans
        )
        self.dead_humans.extend(new_dead)
        self.humans = [human for human in self.humans if not human.dead]

    def run_humans(self):
        random.shuffle(self.humans)
        for human in self.humans:
            human.run_day()

    def run_events(self):
        for event in self.events:
            event.run()

    def run_day(self):
        self.visualizer.display()
        self.day += 1

        self.run_humans()
        self.run_events()

        self.market.clean_data()
        self.update_dead()
