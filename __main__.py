from models.human import Human
from models.job.gatherer import Gatherer
from models.world import World

world = World(display_level=1)
world.add_human(Human(display_level=0, jobs=[Gatherer], world=world))

for _ in range(9):
    world.add_human(Human(jobs=[Gatherer], world=world))

for _ in range(100):
    world.run_day()
