from first import MeansOfTransport
from useful_funcs import for_logging


for_logging()


def test_check_type_pos():
    assert MeansOfTransport.check_type('fff') == True

def test_check_type_neg():
    assert MeansOfTransport.check_type(123) == False



def test_get_value_color_pos():
    a = MeansOfTransport('Honda', 'silver')
    assert MeansOfTransport.get_value_color(a) == 'silver'

def test_get_value_color_neg():
    a = MeansOfTransport()
    assert MeansOfTransport.get_value_color(a) == ''



def test_get_value_brand_pos():
    a = MeansOfTransport('Honda', 'silver')
    assert MeansOfTransport.get_value_brand(a) == 'Honda'

def test_get_value_brand_neg():
    a = MeansOfTransport()
    assert MeansOfTransport.get_value_brand(a) == ''

def test_set_value_color_pos():
    a = MeansOfTransport('Honda', 'silver')
    a.color = 'blue'
    assert MeansOfTransport.get_value_color(a) == 'blue'

# def test_set_value_color_neg():
#     a = MeansOfTransport('Honda', 'silver')
#     with raises(TypeError):
#         a.color = 2 Бесполезная функция, в основном файле надо переписать через __setattr__

def test_init_pos():
    a = MeansOfTransport('Honda', 'Silver')
    assert a.__dict__ == {'brand': 'Honda', 'color': 'Silver'}

def test_init_neg():
    a = MeansOfTransport()
    assert a.__dict__ == {'brand': '', 'color': ''}

def test_show_color_pos(capsys):
    a = MeansOfTransport('Honda', 'silver')
    a.show_color()
    captured = capsys.readouterr()
    assert captured.out == "Цвет машины: silver\n"

def test_show_brand_pos(capsys):
    a = MeansOfTransport('Honda', 'silver')
    a.show_brand()
    captured = capsys.readouterr()
    assert captured.out == "Марка машины: Honda\n"