from models.human import Human
from models.world import World

world = World()

for _ in range(10):
    human = Human()
    world.add_human(human)

for _ in range(55):
    world.run_day()
