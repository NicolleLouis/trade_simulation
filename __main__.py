from models.human import Human
from models.job.gatherer import Gatherer
from models.world import World

world = World()
world.add_human(Human(display=True, jobs=[Gatherer]))

for _ in range(100):
    world.run_day()
