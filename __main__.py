from models.human import Human
from models.job.gatherer import Gatherer
from models.world import World

world = World(display_level=1)
world.add_human(Human(display_level=1, jobs=[Gatherer]))

for _ in range(0):
    world.add_human(Human(jobs=[Gatherer]))

for _ in range(1000):
    world.run_day()
