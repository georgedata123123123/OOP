# Выполнил: Мальцев Георгий Павлович


import json

import logging.config
from logging import getLogger

from abc import ABC
from abc import abstractmethod

with open("logging.conf") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()
logging.info("logging is working!")

class Calculator:

    def summa(self, a, b):

        return a + b

class Conc(Calculator):

    def summa(self, a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError("Use string")
        else:
            return a + b


class Animals(ABC):

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        logging.info("Animals __init__")

    @abstractmethod
    def voice(self):
        print('Это животное делает: ')

class Cat(Animals):


    def voice(self):
        super().voice()
        print('Мяу')

c = Cat(5, 'blue')
c.voice()


class Dog(Animals):

    __barking=None


    def __init__(self, weight, color):

        super().__init__(weight,color)
        if Dog.__barking is None:
            Dog.__barking = self
        else:
            raise Exception("Лает только одна собака, иначе громко!")
        logging.info("Dog __init__")

    @staticmethod
    def get_instance():
        # We define the static method to fetch instance
        logging.info("get_instance")
        if not Dog.__barking:
            Dog()
        return Dog.__barking

    def voice(self):
        print('Гав')




# dog_1 = Dog(25, 'grey')
# print(dog_1.get_instance())
# new_dog_barking = Dog.get_instance()
# print(new_dog_barking)
# dog_2 = Dog(34, 'orange')
# print(dog_2.get_instance())

