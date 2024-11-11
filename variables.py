import pytest
from first import Car, Moped
from useful_funcs import for_logging
from second import Conc


for_logging()

a = Car(4, 1, 2, 3)
m = Moped(4)
conc = Conc()

# @pytest.fixture(autouse=True)
# def classic():
#     a = 0
#     a = Car(4, 1, 2, 3)