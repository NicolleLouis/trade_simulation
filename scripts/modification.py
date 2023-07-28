from scripts.switch_hero import SwitchHero
from service.game.save import GameSaveService

SAVE_NAME = "main"

game = GameSaveService.open_or_create_game(SAVE_NAME)

SwitchHero(game=game).switch_hero_with_highest_job_number()

GameSaveService.save_game(game=game, save_name=SAVE_NAME)
