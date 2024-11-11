from first import Integer, Car
from pytest import raises, mark
from useful_funcs import for_logging


for_logging()


def test_verify_coord_pos():
    assert Integer.verify_coord(int(10)) == None

def test_verify_coord_neg():
    with raises(TypeError):
        Integer.verify_coord('hhh')

@mark.parametrize("index, value", [('_x', 1),
                                   ('_y', 2),
                                   ('_z', 3)])
def test_set_name_pos(index, value):
    a = Car(4, 1, 2, 3)
    assert a.__dict__[index] == value

@mark.parametrize("index, value", [('_x', 1),
                                   ('_y', 2),
                                   ('_z', 3)])
def test_get_pos(index, value):
    a = Car(4, 1, 2, 3)
    assert a.__dict__[index] == value

def test_get_neg():
    with raises(TypeError):
        a = Car(4, 1, 2)

def test_set_pos(capsys):

    a = Car(4, 1, 2, 3)
    captured = capsys.readouterr()
    assert captured.out == "1\n1\n1\n"

