# Выполнил: Мальцев Георгий Павлович


import json

import logging.config
from logging import getLogger

with open("logging_2.conf") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()
logging.info("logging is working!")

class Human:

    @classmethod
    def check_type(cls, x):
        return type(x) in [int]

    def __init__(self, hands, foots, eyes):
        if self.check_type(hands) and self.check_type(foots) and self.check_type(eyes):
            self.hands = hands
            self._eyes = eyes
            self.__foots = foots
            logging.warning("Кто-то записал в __init__ количества рук, глаз и ног")
        else:
            raise TypeError("Введите количество рук, ног и глаз цифрами")

    def __setattr__(self, key, value):
        if key in ['hands', '_Human__foots', '_eyes']:
            logging.warning(f"Кто-то меняет то, что не стоит: {key}. Было {self.__dict__} стало {key}: {value}")
        object.__setattr__(self, key, value)

kolr = Human(2, 2, 2)
kolr.hands = 1
print(Human.__dict__)


