from first import Moped
from pytest import raises
from useful_funcs import for_logging
from variables import m


for_logging()


def test_check_type_int_pos():
    assert m._Moped__check_type_int(10) == True

def test_check_type_int_neg():
    assert m._Moped__check_type_int('int') == False


def test_init_pos(capsys):
    for_print = Moped(4)
    captured = capsys.readouterr()
    assert captured.out == "5\n"
    assert m.wheels == 4

def test_time_pos():
    assert m.time_calc(10, 5) == 2

def test_time_neg():
    with raises(TypeError):
        m.time_calc('fff', 3)