import random

from constants.human_name import FIRST_NAMES, LAST_NAMES


class HumanService:
    @classmethod
    def random_name(cls):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        return f'{first_name} {last_name}'
