# Выполнил: Мальцев Георгий Павлович


import json

import logging.config
from logging import getLogger

with open("logging.conf") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()
logging.info("logging is working!")





class MeansOfTransport:


    @classmethod
    def check_type(cls, x):
        return type(x) in [str]

    def get_value_color(self):
        return self.color

    def get_value_brand(self):
        return self.brand


    def set_value_color(self, color):
        if self.check_type(color):
            self.color = color
        else:
            raise TypeError("Write string")
        logging.info("Ввели не строку")


    def set_value_brand(self, brand):
        if self.check_type(brand):
            self.brand = brand
        else:
            raise TypeError("Write string")
        logging.info("Ввели не строку")


    def __init__(self, brand='', color=''): # __init__ по умолчанию не ждет аргументов

        self.brand = self.color = 0
        if self.check_type(color) and self.check_type(brand):
            self.color = color
            self.brand = brand
        else:
            raise TypeError("Use string")
        logging.info("initialization of MeansOfTransport is correct!")

    def show_color(self):
        print(f"Цвет машины: {self.color}")
        logging.info("show color def")

    def show_brand(self):
        print(f"Марка машины: {self.brand}")
        logging.info("show brand def")



class Integer():# data descriptor, дескриптор в приоритете над объектом класса дочернего


    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner , name): # owner - Ccылка на класс, name - имя объекта класса, автоматически создает name, когда создается объект класса интеджер
        logging.info("Сработал метод __set_name__")
        self.name = "_" + name

    def __get__(self, instance, owner): # self ссылается на объект переменной в основном классе (х в классе Car)
        logging.info("Сработал метод __get__")
        return instance.__dict__(self.name)

    def __set__(self, instance, value): # value передает значение переменной которая будет записываться в объект b класса Car при __инит__, instance ссылается на b
        logging.info("Сработал метод __set__")
        print('1')
        instance.__dict__[self.name] = value




class Car(MeansOfTransport):


    car_drive = 4
    x = Integer()
    y = Integer()
    z = Integer()

    @classmethod
    def __check_type_int(cls, x):
        return type(x) in [int]



    def __new__(cls, *args, **kwargs): # При создании объекта (переменные будут удалены)
        logging.info("new отработал!")
        return super().__new__(cls)

    def __init__(self, wheels, x, y, z): # После метода new как объект создан
        self.wheels = 0
        self.type = 'cabrio'
        self.fuel = 95

        self.x = x
        self.y = y
        self.z = z

        self.__counter = 0
        self.lemght = []
        self.marks = [1, 2, 3]

        if self.__check_type_int(wheels):
            self.wheels = wheels



    def __call__(self, *args, **kwargs):
        # Срабатывает при вызове экземпляра класса(тогда класс функтер)
        logging.info("Вызов call")
        self.__counter += 1
        return self.__counter

    def __getattribute__(self, item):
        # При получении заданного атрибута
        # Здесь надо помнить что это имя атрибута!!!
        logging.info(f'Use getattribute for {item}')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # При создании атрибута или перезаписи
        logging.info('Using setattr')
        object.__setattr__(self, key, value)

    def  __getattr__(self, name):
        # При обращении к несуществующему атрибуту
        logging.info('Using getattr')
        return False

    def __delattr__(self, item):
        # При удалении атрибута Экземпляра класса
        logging.info(f'Delete atribute {item}')
        object.__delattr__(self, item)


    # Если не реализованы репр и стр, то возвращается адрес в памяти
    def __repr__(self): # Меняет информацию о экземпляре класса(просто информационка),
                        # выводится при отладке через консоль или через f-строку
        logging.info("__repr__")
        return f'{self.__class__}: {self.car_drive}'

    def __str__(self): # как repr, только выводится через принт, для пользователя
        logging.info("__str__")
        return self.type

    def __len__(self): # При вызове метода len

        return len(self.lemght)

    def __bool__(self): # Завязан на методе __len__, возвращает true or False,
                        # если в лен пустое множество(в нашем случае пустой массив). \\\Если не реализовано len/bool выводит True
        logging.info("__bool__")
        return self.wheels != 0

    def __abs__(self): # При вызове модуля

        return list(map(abs, self.lemght))

    def __add__(self, other):
        # При прибавлении к экземпляру класса создается новый экземпляр с новым значением
        logging.info("__add__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо прибавлять целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(self.wheels + wh, self._x, self._y, self._z)

    def __radd__(self, other):
        # Когда прибавляют класс к чему-то
        logging.info("__radd__")
        return self + other

    def __iadd__(self, other):
        #   Когда используют +=(при этом не создается новый объект, а изменяется текущий, это топ для памяти)
        logging.info("__iadd__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо прибавлять целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = wh.wheels
        self.wheels += wh
        return self

    def __sub__(self, other):
        # Вычитание
        logging.info("__sub__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо вычитать целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(self.wheels - wh)

    def __isub__(self, other):
        #   Когда используют +=(при этом не создается новый объект, а изменяется текущий, это топ для памяти)
        logging.info("__isub__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо прибавлять целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = wh.wheels
        self.wh -= wh
        return self

    def __rsub__(self, other):

        logging.info("__rsub__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо вычитать  из целого числа или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(wh - self.wheels)

    def __mul__(self, other):
        # Умножение
        logging.info("__mul__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо умножать целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(self.wheels * wh)

    def __rmul__(self, other):

        logging.info("__rmul__")
        return self * other

    def __imul__(self, other):
        #   Когда используют *=(при этом не создается новый объект, а изменяется текущий, это топ для памяти)
        logging.info("__imul__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо умножать целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = wh.wheels
        self.wh *= wh
        return self

    def __truediv__(self, other):  # Деление

        logging.info("__mul__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо делить на целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(self.wheels / wh)

    def __itruediv__(self, other):
        #   Когда используют /=(при этом не создается новый объект, а изменяется текущий, это топ для памяти)
        logging.info("__itruediv__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо  делить на целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = wh.wheels
        self.wh /= wh
        return self

    def __rtruediv__(self, other):

        logging.info('__rtruediv__')
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо  делить целое числа или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(wh/self.wheels)

    def __floordiv__(self, other):  # Целочисленное деление

        logging.info("__floordiv__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо делить на целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(self.wheels // wh)

    def __ifloordiv__(self, other):
        #   Когда используют //=(при этом не создается новый объект, а изменяется текущий, это топ для памяти)
        logging.info("__ifloordiv__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо  делить на целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = wh.wheels
        self.wh //= wh
        return self

    def __rfloordiv__(self, other):

        logging.info('__rfloordiv__')
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо делить целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(wh // self.wheels)

    def __mod__(self, other):  # Остаток от деления

        logging.info("__mod__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо делить на целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(self.wheels % wh)

    def __imod__(self, other):
        #   Когда используют %=(при этом не создается новый объект, а изменяется текущий, это топ для памяти)
        logging.info("__imod__")
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо  делить на целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = wh.wheels
        self.wh %= wh
        return self

    def __rmod__(self, other):

        logging.info('__rmod__')
        if not isinstance(other, (int, Car)):
            raise ArithmeticError("Необходимо делить целое число или Car()!")
        wh = other
        if isinstance(other, Car):
            wh = other.wheels
        return Car(wh % self.wheels)

    @classmethod
    def __for_wheels(cls, other):
        if not isinstance(other, (int, Car)):
            raise TypeError("Use int or Car()")

        return other if isinstance(other, int) else other.wheels

    def __eq__(self, other): # Равенство экземпляра класса, при этом != это not(b1==b2) __ne__

        logging.info("__eq__")
        wh = self.__for_wheels(other)
        return self.wheels == wh

    def __hash__(self): # Меняет хеш-значение объекта, при использовании __eq__ объект становится нехешируемым типом,
                        # так как нарушается внутренний алгоритм работы функции hsh(встроенной)

        return hash(self.wheels)

    def __ne__(self, other):

        logging.info("__ne__")
        wh = self.__for_wheels(other)
        return self.wheels != wh


    def __lt__(self, other): # если не реализованы методы сравнения, то вылезет ошибка

        logging.info("__lt__") # Сравнение меньше, при этом больше (__gt__) срабатывает тоже также(в обратную)
        wh = self.__for_wheels(other)
        return self.wheels < wh

    def __gt__(self, other):

        logging.info("__gt__")
        wh = self.__for_wheels(other)
        return self.wheels > wh

    def __le__(self, other): # строгое сравнение меньше, при этом строгое больше __ge__  также работает в обратную

        logging.info("__le__")
        wh = self.__for_wheels(other)
        return self.wheels <= wh

    def __ge__(self, other): # строгое сравнение меньше, при этом строгое больше __ge__  также работает в обратную

        logging.info("__ge__")
        wh = self.__for_wheels(other)
        return self.wheels >= wh

    def __getitem__(self, item): # Когда идет обращение к индексу элемента класса Car()[3]
                                # Делает объект итерируемым, если не реализован __iter__, вау питон!!!

        return self.marks[item]

    def __setitem__(self, key, value):

        if not isinstance(key, int) or key < 0:
            raise TypeError("Bad key")
        if key >= len(self.marks): # Для добавления индексов, если элементов не хватает
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value


    def __contains__(self, item): # Для реализации оператора in

        logging.info("__contains__")
        return item in self.__dict__

    def __iter__(self): # Делает объект иттерируемым

        logging.info("__iter__ in car")
        self.index = 0
        return self

    def __next__(self): # Возвращает следующее значение иттерируемого объекта, после __некст__ объект итератор

        logging.info("__next__ in car")
        if len(self.marks) >= self.index:
            self.index += 1

        if len(self.marks)+1 == self.index:
            raise StopIteration
        return self.marks[self.index - 1]





    @classmethod
    def show_car_drive(cls):
        print(cls.car_drive)



a = Car(1, 2, 3,4)
print(a._type)


class Moped(MeansOfTransport):

    @classmethod
    def __check_type_int(cls, x):
        return type(x) in [int]

    def __init__(self, wheels):
        self.__wheels = 0
        if self.__check_type_int(wheels):
            self.wheels = wheels
        print(self.time_calc(10, 2))

    @staticmethod
    def time_calc(lenghth, speed):
        time = lenghth/speed
        return  int(time)







#
# a = MeansOfTransport('Honda', 'Silver')
# a.set_value_color('Green')
# a.get_value_color()
#
# b = Car('Volandemort')
# b = Car(4)
# print(Car(2) == Car(4))
# print(b.show_car_drive())
# for i in Car(4):
#     print(i)
#
# a = Car(4, 1, 2, 3)
# a._z = 33
# print(bool(MeansOfTransport))


