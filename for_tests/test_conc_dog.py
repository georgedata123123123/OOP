from useful_funcs import for_logging
from second import Conc, Dog
from pytest import raises, mark
from variables import conc

for_logging()

def test_summa_pos():
    assert conc.summa("f", "f") == "ff"

def test_summa_neg():
    with raises(ValueError):
        conc.summa(2, 4)

def test_dog_pos():
    dog_1 = Dog(35, 'grey')
    assert dog_1.get_instance() == Dog.get_instance()

def test_dog_neg():
    with raises(Exception):
        dog_4 = Dog(22, 'white') # Попали на зависимость тестов,
                                            # так как dog_1 - лающая собака)

