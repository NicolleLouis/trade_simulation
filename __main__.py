from service.game import GameService

SAVE_NAME = "fisher-cook-exploration"
DAY_NUMBER = 300

game = GameService.open_or_create_game(SAVE_NAME)

game.run(DAY_NUMBER)

GameService.save_game(game=game, save_name=SAVE_NAME)