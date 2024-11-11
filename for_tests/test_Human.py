from fifth import Human
from pytest import raises, mark
from useful_funcs import for_logging_2



for_logging_2()


def test_check_type_neg():
    assert Human.check_type(['1', '1', 'fff']) == False

def test_check_type_pos():
    assert Human.check_type(123) == True

def test_init_pos():
    human = Human(2, 2, 2)
    assert human.hands == 2
    assert human._eyes == 2
    assert human._Human__foots == 2

@mark.parametrize("hands, foots, eyes", [('f', 2, 2),
                                         (2, 'f', 2),
                                         (2, 2, 'f')])
def test_init_neg(hands, foots, eyes):
    with raises(TypeError):
        Human(hands, foots, eyes)