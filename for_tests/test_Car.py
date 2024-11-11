from first import Car
from pytest import raises, mark
from useful_funcs import for_logging
from variables import a


for_logging()



def test_check_type_int_pos():
    assert a._Car__check_type_int(10) == True

def test_check_type_int_neg():
    assert a._Car__check_type_int('fff') == False




@mark.parametrize("value", [4, -2])
def test_init_pos(value):
    b = Car(value, 1, 2, 3)
    assert b.wheels == value

def test_init_neg():
    c = Car('ddd', 1, 2, 3)
    assert c.wheels == 0



def test_call_pos():
    d = Car(1, 2, 3, 4)
    d()
    assert d._Car__counter == 1

def test_call_neg():
    assert a._Car__counter == 0


def test_str():
    assert str(a) == 'cabrio'


@mark.parametrize("other", [1, Car(1, 1, 2, 3)])
def test_add_pos(other):
    assert a + other == 5

def test_add_neg():
    with raises(ArithmeticError):
        a + 'ddd'


@mark.parametrize("other", [1, Car(1, 1, 2, 3)])
def test_iadd_pos(other):
    e = Car(4, 1, 2, 3)
    e += 1
    assert e.wheels == 5

def test_iadd_neg():
    f = Car(4, 1, 2, 3)
    with raises(ArithmeticError):
        f += 'ddd'

@mark.parametrize("other", [4, Car(4, 1, 2, 3)])
def test_for_wheels_eq_pos(other):
    assert (a == other) == True


def test_for_wheels_eq_neg():
    with raises(TypeError):
        a == 'ddd'

@mark.parametrize("index, value", [(14, None),
                                   (15, 3)])
def test_setitem_pos(index, value):
    a[15] = 3
    assert a[index] == value

@mark.parametrize("errors, index", [(IndexError, -30),
                                    (TypeError, 'fff')])
def test_setitem_neg(index, errors):
    with raises(errors):
        a[index] == 5


def test_iter_next():
    spisok = []
    for i in a:
        spisok.append(i)
    assert spisok == a.marks







