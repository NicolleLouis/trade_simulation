import pdb

from service.game.save import GameSaveService

SAVE_NAME = "fisher-cook-exploration"

game = GameSaveService.open_or_create_game(SAVE_NAME)

world = game.world
