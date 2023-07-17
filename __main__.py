from service.game import GameService

SAVE_NAME = "zozo-a-faim"
DAY_NUMBER = 10

game = GameService.open_or_create_game(SAVE_NAME)

game.run(DAY_NUMBER)

GameService.save_game(game=game, save_name=SAVE_NAME)
