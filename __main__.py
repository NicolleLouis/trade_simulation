from service.game.save import GameSaveService

SAVE_NAME = "fisher-cook-exploration"
DAY_NUMBER = 300

game = GameSaveService.open_or_create_game(SAVE_NAME)

game.run(DAY_NUMBER)

GameSaveService.save_game(game=game, save_name=SAVE_NAME)