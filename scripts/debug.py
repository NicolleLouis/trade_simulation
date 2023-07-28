from service.game.save import GameSaveService

SAVE_NAME = "main"

game = GameSaveService.open_or_create_game(SAVE_NAME)

world = game.world
