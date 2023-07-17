import pdb

from service.game import GameService

SAVE_NAME = "fisher-cook-exploration"

game = GameService.open_or_create_game(SAVE_NAME)

hero = game.world.hero
visualizer = hero.visualizer
market = game.world.market.visualizer

pdb.set_trace()
