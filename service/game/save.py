import pickle
from os.path import exists

from models.game import Game


class GameSaveService:
    @staticmethod
    def file_address(save_name):
        return f"saved_state/{save_name}"

    @classmethod
    def open_or_create_game(cls, save_name):
        file_address = cls.file_address(save_name)
        if exists(file_address):
            file = open(file_address, "rb")
            game = pickle.load(file)
            file.close()
        else:
            game = Game()
        return game

    @classmethod
    def save_game(cls, game, save_name):
        file_address = cls.file_address(save_name)
        file = open(file_address, "wb")
        pickle.dump(game, file)
        file.close()
