from models.human import Human
from models.world import World

world = World()
world.add_human(Human(display=True))

for _ in range(0):
    world.add_human(Human())

for _ in range(25):
    world.run_day()
