from fourth import People
from pytest import raises, mark


def test_check_type_pos():
    assert People.check_type(['1', '1', 'fff']) == True

def test_check_type_neg():
    assert People.check_type(123) == False

def test_init_pos():
    peoples = People(['jack', 'mike', 'frank'])
    assert peoples.jack == 'jack'


@mark.parametrize("errors, value", [(ValueError, [1, 2, 3]),
                                    (TypeError, 1)])
def test_init_neg(errors, value):
    with raises(errors):
        People(value)

def test_setattr_pos():
    peoples = People(['jack', 'mike', 'frank'])
    peoples.karl = 'Nick'
    assert peoples.Nick == 'Nick'

def test_next_pos():
    peoples = People(['jack'])
    peoples_2 = People(['jack', 'mike', 'frank'])
    a = []
    b = []
    for i in peoples:
        a.append(i)
    for j in peoples_2:
        b.append(j)
    assert a == ['jack']
    assert b == ['jack', 'mike', 'frank']
