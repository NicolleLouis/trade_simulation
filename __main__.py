from models.human import Human
from models.world import World

world = World()

for _ in range(1):
    human = Human()
    world.add_human(human)

for _ in range(20):
    world.run_day()
