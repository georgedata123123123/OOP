class People:

    @classmethod
    def check_type(cls, x):
        return type(x) in [list]


    def __init__(self, names):
        if self.check_type(names):
            for x in names:
                if not isinstance(x, str):
                    raise ValueError("Имена пишутся строкой")
                else:
                    self.x = x
        else:
            raise TypeError("На вход необходимо подавать список")


    def __setattr__(self, key, value):
        if key == 'index':
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, value, value)


    def __getitem__(self, item):
        return list(self.__dict__.keys())[item]

    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        a = list(self.__dict__.keys())
        if len(a) >= self.index:
            self.index += 1
        if len(a) == self.index:
            raise StopIteration
        return a[self.index-1]




p = People(['Frank', '123'])
print(p.__dict__)