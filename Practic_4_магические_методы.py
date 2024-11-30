import random


class Clock:
    __DAY = 86400
    def __init__(self, second: int):
        if not isinstance(second, int):
            raise TypeError
        self.second = second % self.__DAY

    def get_second(self):
        s = self.second % 60
        m = (self.second // 60) % 60
        h = (self.second // 3600) % 24

        return f'{self.__get_format(h)}:{self.__get_format(m)}:{self.__get_format(s)}'

    @classmethod
    def __get_format(self, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError
        sc = other
        if isinstance(other, Clock):
            sc = other.second
        return Clock(self.second + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print('_______')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError
        sc = other
        if isinstance(other, Clock):
            sc = other.second
        self.second += sc
        return self

# New test
class NewList:
    def __init__(self, lst=None):
        if not lst:
            self.lst = []
        else:
            self.lst = lst

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError
        val = other
        if isinstance(val, NewList):
            val = other.lst
        lst_1z = list(map(lambda x: (type(x), x), self.lst))
        my_list = lst_1z.copy()
        val = [(type(x), x) for x in val]

        for i in my_list:
            if i in val:
                lst_1z.remove(i)
                val.remove(i)
        lst_1z = list(map(lambda x: x[1], lst_1z))
        return NewList(lst_1z)

    def __rsub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError
        val = other
        if isinstance(val, NewList):
            val = other.lst
        l = list(map(lambda x: (type(x), x), self.lst))
        val = [(type(x), x) for x in val]
        my_list = val.copy()

        for i in my_list:
            if i in l:
                l.remove(i)
                val.remove(i)
        val = list(map(lambda x: x[1], val))
        return NewList(val)

    def get_list(self):
        return self.lst




# Next test

class ListMath:
    def __init__(self, my_list=None):
        self.lst_math = list(filter(lambda x: type(x) in (int, float), my_list)) if my_list and isinstance(my_list, list) else []
    @staticmethod
    def func(x):
        if not isinstance(x, (int, float)):
            raise ArithmeticError('Значение должно быть числом')

    def __add__(self, other):
        self.func(other)
        return ListMath(list(map(lambda x: x + other, self.lst_math)))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.func(other)
        self.lst_math = list(map(lambda x: x + other, self.lst_math))
        return self

    def __sub__(self, other):
        self.func(other)
        return ListMath(list(map(lambda x: x - other, self.lst_math)))

    def __rsub__(self, other):
        self.func(other)
        return ListMath([other - i for i in self.lst_math])

    def __isub__(self, other):
        self.func(other)
        self.lst_math = [round(i - other, 2) for i in self.lst_math]
        return self

    def __mul__(self, other):
        self.func(other)
        return ListMath(list(map(lambda x: x * other, self.lst_math)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self.func(other)
        self.lst_math = list(map(lambda x: x * other, self.lst_math))
        return self

    def __truediv__(self, other):
        self.func(other)
        if other == 0:
            raise ArithmeticError('На ноль делить нельзя')
        return ListMath(list(map(lambda x: x / other, self.lst_math)))

    def __rtruediv__(self, other):
        self.func(other)
        return ListMath(list(map(lambda x: other / x, self.lst_math)))

    def __itruediv__(self, other):
        self.func(other)
        self.lst_math = list(map(lambda x: x / other, self.lst_math))
        return self

# Next test

class Stack:
    def __init__(self):
        self.top = None
    def push_back(self, obj):
        if not self.top:
            self.top = obj
        elif self.top and self.top.next == None:
            self.top.next = obj
        else:
            j = self.top
            while j.next:
               j = j.next
            j.next = obj

    def pop_back(self):
        if not self.top:
            return
        if self.top.next == None:
            self.top = None
        else:
            j = self.top
            while j.next:
                c = j
                j = j.next
            c.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self

    def show(self):
        j = self.top
        while j.next:
            j = j.next
            print(j.data)

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, val):
        self.__next = val

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, val):
        self.__data = val


# Next test

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        if isinstance(other, int):
            if other < len(self.book_list):
                self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)

# Next test

class Item:
    def __init__(self, name, money):
        self.name = name
        if isinstance(money, (int, float)):
            self.money = money

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.money = self.money + other
        if isinstance(other, Item):
            self.money = self.money + other.money
        return self.money

    def __radd__(self, other):
        self.money = self.money + other
        return self.money

class Budget:
    def __init__(self):
        self.item_list = []

    def add_item(self, it):
        self.item_list.append(it)

    def remove_item(self, indx):
        self.item_list.pop(indx)

    def get_items(self):
        return self.item_list


# Next test

class Box3D:
    def __init__(self, width, height, depth):
        self.w = width
        self.h = height
        self.d = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.w + other.w, self.h + other.h, self.d + other.d)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Box3D(self.w * other, self.h * other, self.d * other)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.w - other.w, self.h - other.h, self.d - other.d)

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Box3D(self.w // other, self.h // other, self.d // other)

    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return Box3D(self.w % other, self.h % other, self.d % other)

# Next test

class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, *args, **kwargs):
        pass

# Next test

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.x = to_x
        self.y = to_y
        self.speed = max_speed


class Track:

    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.track_line = []

    def add_track(self, tr):
        if isinstance(tr, TrackLine):
            self.track_line.append(tr)

    def get_tracks(self):
        return tuple(self.track_line)

    def length_track(self):
        st_x, st_y = self.start_x, self.start_y
        l = 0
        for x in self.get_tracks():
            l += ((x.x - st_x)**2 + (x.y - st_y)**2)**0.5
            st_x, st_y = x.x, x.y
        return l

    def __eq__(self, other):
        if not isinstance(other, Track):
            raise ValueError('Сравниваемые элементы должны быть классом Track')
        return len(self) == len(other)

    def __lt__(self, other):
        if not isinstance(other, Track):
            raise ValueError('Сравниваемые элементы должны быть классом Track')
        return len(self) < len(other)

    def __len__(self):
        return int(self.length_track())


# Next test
class Integer:
    def __init__(self, min_dim, max_dim):
        self.max_dim = max_dim
        self.min_dim = min_dim

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value in range(self.min_dim, self.max_dim):
            setattr(instance, self.name, value)
class Dimensions:
    a = Integer(10, 10000)
    b = Integer(10, 10000)
    c = Integer(10, 10000)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __gt__(self, other):
        if isinstance(other, Dimensions):
            return self.a * self.b * self.c > other.a * other.b * other.c

    def __ge__(self, other):
        if isinstance(other, Dimensions):
            return self.a * self.b * self.c >= other.a * other.b * other.c

class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]


lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)


# Next test
import re
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

lst_words_all = [re.findall(r'\w{1,}', i) for i in stich]

class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __len__(self):
        return len(self.lst_words)

lst_text = []
for i in lst_words_all:
    lst_text.append(StringText(i))

lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(i.lst_words) for i in lst_text_sorted]

# Next test

class Morph:
    def __init__(self, *args):
        self.morph_list = list(args)

    def add_word(self, word):
        self.morph_list.append(word)

    def get_words(self):
        return tuple(self.morph_list)

    def __eq__(self, other):
        if isinstance(other, str):
            return any(map(lambda x: other == x, self.morph_list))
        if isinstance(other, Morph):
            for i in self.morph_list:
                for j in other.morph_list:
                    if i == j:
                        return True

dict_words = [['связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'],
              ['формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам',
'формулами', 'формулах'],
              ['вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'],
              ['эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'],
              ['день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях']]
dict_words = [Morph(*i) for i in dict_words ]


# Next test

class FileAcceptor:
    def __init__(self, *args):
        self.args = args

    def __call__(self, vol, *args, **kwargs):
        for j in self.args:
            if vol.endswith('.' + j):
                return True

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            return FileAcceptor(*self.args + other.args)
f = FileAcceptor('fgh')

# Next test

class Money:
    type_class = None
    def __init__(self, volum=0):
        self.__volume = volum
        self.__cd = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vol):
        self.__volume = vol

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, vol):
        self.__cd = vol

    def converter(self, type_class, money):
        if type_class == 'dollar':
            return round(money * CentralBank.rates['rub'], 1)
        elif type_class == 'euro':
            return round(money * CentralBank.rates['rub'] * CentralBank.rates['euro'], 1)
        else:
            return round(money, 1)

    def __eq__(self, other):
        if self.cd:
            vol1 = self.converter(self.type_class, self.volume)
            vol2 = self.converter(other.type_class, other.volume)
            return vol1 == vol2
        else:
            raise ValueError("Неизвестен курс валют.")


    def __gt__(self, other):
        if self.cd:
            vol1 = self.converter(self.type_class, self.volume)
            vol2 = self.converter(other.type_class, other.volume)
            return vol1 > vol2
        else:
            raise ValueError("Неизвестен курс валют.")

    def __ge__(self, other):
        if self.cd:
            vol1 = self.converter(self.type_class, self.volume)
            vol2 = self.converter(other.type_class, other.volume)
            return vol1 >= vol2
        else:
            raise ValueError("Неизвестен курс валют.")

class MoneyR(Money):
    type_class = 'rub'

class MoneyD(Money):
    type_class = 'dollar'

class MoneyE(Money):
    type_class = 'euro'
class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None
    @classmethod
    def register(cls, money):
        money.cd = cls


# Next test

class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        if len(self.box) != len(other.box):
            return False
        return all(map(lambda x,y: x == y, sorted(self.box, key=lambda x: x.name), sorted(other.box, key=lambda x: x.name)))

class Thing:
    def __init__(self, name: str, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

# Next tes магический метод __hash__

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.height, self.width))

# Next test

class ShopItem:
    def __init__(self, name: str, weight: int | float, price: int | float):
        self.name = name.lower()
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst = ['Системный блок: 1500 75890.56',
       'Монитор Samsung: 2000 34000',
       'Клавиатура: 200.44 545',
       'Монитор Samsung: 2000 34000']

my_dict = {}
for i in lst:
    n = re.findall(r'.{1,}:', i)
    w, h = re.findall(r'\d+[.]?\d', i)[0], re.findall(r'\d+[.]?\d', i)[1]
    vol = ShopItem(*n, w, h)
    if vol not in my_dict:
        my_dict[vol] = [vol, 1]
    else:
        my_dict[vol][1] += 1


# Next test

class DataBase:
    def __init__(self, path: str):
        self.path = path  # Путь к файлу c данными БД
        self.dict_db = {}

    def write(self, record):
        self.dict_db[record] = self.dict_db.get(record, []) + [record]
        # self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        for i in self.dict_db:
            if i.pk == pk:
                return i

class Record:
    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio if type(fio) == str else None
        self.descr = descr if type(descr) == str else None
        self.old = old if type(old) == int else None
        self.pk = random.choice(range(1, 100000))

    def __hash__(self):
        return hash((self.old, self.fio))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst = ['Балакирев С.М.; программист; 33', 'Кузнецов Н.И.; разведчик-нелегал; 35',
       'Суворов А.В.; полководец; 42', 'Иванов И.И.; фигурант всех подобных списков; 26',
       'Балакирев С.М.; преподаватель; 33', 'Балакирев С.М.; раммист; 33' ]

db = DataBase('путь1')

for i in lst:
    k = Record(i.strip().split('; ')[0], i.strip().split('; ')[1], int(i.strip().split('; ')[2]))
    db.write(k)

# Next test

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name if isinstance(name, str) else None
        self.author = author if isinstance(author, str) else None
        self.year = year if isinstance(year, int) else None

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

lst_in = ['Python; Балакирев С.М.; 2020', 'Python ООП; Балакирев С.М.; 2021',
          'Python ООП; Балакирев С.М.; 2022', 'Python; Балакирев С.М.; 2021']

lst_bs = []
for i in lst_in:
    k = i.split('; ')
    lst_bs.append(BookStudy(k[0], k[1], int(k[2])))


# Next test
class Integration:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 < value:
            setattr(instance, self.name, value)
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")
class Dimensions:
    a = Integration()
    b = Integration()
    c = Integration()
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

# Next test
class Intege:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or 0 >= value:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        instance.__dict__[self.name] = value

class Triangle:
    a = Intege()
    b = Intege()
    c = Intege()
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _is_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self._is_triangle(value, self.b, self.c)) or \
                (key == 'b' and not self._is_triangle(self.a, value, self.c)) or \
                (key == 'c' and not self._is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

        def __len__(self):
            return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = (self.a + self.b + self.c)/2
        return (p * (p-self.a) * (p-self.b) * (p-self.c)) ** 0.5

# Next test

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            return
        if key in ('old', 'score') and type(value) != int:
            return
        super().__setattr__(key, value)



# Next test

class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                  'mail@list.ru; Выгодное предложение; Вам одобрен кредит.']

        for i in lst_in:
            i = i.split('; ')
            self.inbox_list.append(MailItem(i[0], i[1], i[2]))
class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read

#Next test

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def __len__(self):
        if ((self.x2 - self.x1) ** 2 + (self.y2 - self.y2) ** 2) ** 0.5 < 1:
            return False
        else:
            return True

# Next test

class Ellipse:
    def __init__(self, *args):
        if len(args) != 4:
            return
        self.x1 = args[0]
        self.y1 = args[1]
        self.x2 = args[2]
        self.y2 = args[3]

    def __bool__(self):
        if self.__dict__:
            return True
        else:
            return False

    def get_coords(self):
        if self.__bool__():
            return (self.x1, self.y1, self.x2, self.y2)
        raise AttributeError('нет координат для извлечения')

# Next test

class Vector:
    def __init__(self, *args):
        self.args = args

    @staticmethod
    def func(len_1, len_2):
        return len(len_1.args) == len(len_2.args)

    def __add__(self, other):
        if isinstance(other, Vector):
            if not self.func(self, other):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*(map(lambda x, y: x + y, self.args, other.args)))
        if isinstance(other, int):
            return Vector(*(map(lambda x: x + other, self.args)))

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if not self.func(self, other):
                raise ArithmeticError('размерности векторов не совпадают')
            self.args = tuple(map(lambda x, y: x + y, self.args, other.args))
        if isinstance(other, int):
            self.args = tuple(map(lambda x: x + other, self.args))
        return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            if not self.func(self, other):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*(map(lambda x, y: x - y, self.args, other.args)))
        if isinstance(other, int):
            return Vector(*(map(lambda x: x - other, self.args)))

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        if isinstance(other, Vector):
            if not self.func(self, other):
                raise ArithmeticError('размерности векторов не совпадают')
            self.args = tuple(map(lambda x, y: x - y, self.args, other.args))
        if isinstance(other, int):
            self.args = tuple(map(lambda x: x - other, self.args))
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            if not self.func(self, other):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*(map(lambda x, y: x * y, self.args, other.args)))
        if isinstance(other, int):
            return Vector(*(map(lambda x: x * other, self.args)))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return all(map(lambda x, y: x == y, self.args, other.args))
        if isinstance(other, int):
            return all(map(lambda x: x == other, self.args))


# next test

class GamePole:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, N, M, total_mines):
        self.M = M
        self.N = N
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.M)) for _ in range(self.N))  #Должен быть двумерный кортеж рамером N строк и M столбцов

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        n = self.total_mines
        while n != 0:
            i, j = random.randint(0, self.N-1), random.randint(0, self.M-1)
            if not self.pole[i][j].is_mine:
                self.pole[i][j].is_mine = True
                n -= 1
        indx = ((-1, -1), (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1), (1, 1), (-1, 1))
        for i in range(self.N):
            for j in range(self.M):
                if not self.pole[i][j].is_mine:
                    mines = sum(self.pole[i+x][j+y].is_mine for x, y in indx if 0 <= i+x < self.N and 0 <= j+y < self.M)
                    self.pole[i][j].number = mines


    def open_cell(self, i, j):
        try:
            self.pole[i][j].is_open = True
        except:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in self.pole:
            print()
            for j in i:
                # j.is_open = True
                if j.is_mine == True:
                    print('*', end=' ')
                elif j.is_open == True:
                    print(j.number, end=' ')
                else:
                    print('#', end=' ')

class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_mine(self, value):
        if isinstance(value, bool):
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, value):
        if type(value) == int and 0 <= value <= 8:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open
    @is_open.setter
    def is_open(self, value):
        if isinstance(value, bool):
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self.is_open

# __getitem__, __setitem__, __delitem__
# Next test

class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __getitem__(self, item):
        if not isinstance(item, int) or item > len(self.__dict__) - 1 or item < - len(self.__dict__):
            raise IndexError('неверный индекс поля')
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        keys = list(self.__dict__.keys())
        if not isinstance(key, int) or key > len(self.__dict__) - 1:
            raise IndexError('неверный индекс поля')
        self.__dict__[keys[key]] = value


# Next test

class Track2:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.all_track = {}

    def add_point(self, x, y, speed):
        self.all_track[x, y] = speed

    def check(self, vol):
        if not 0 <= vol <= len(self.all_track) - 1:
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.check(item)
        return tuple(self.all_track.items())[item]

    def __setitem__(self, key, value):
        self.check(key)
        self.all_track[list(self.all_track.keys())[key]] = value


# Next test

class Array:
    def __init__(self, max_length: int, cell):
        self.max_length = max_length
        self.cell = cell
        self.my_massiv = [self.cell() for _ in range(self.max_length)]

    def check_cell(self, val):
        if not isinstance(val, int) or not 0 <= val < self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.check_cell(item)
        if self.my_massiv[item].value:
            return self.my_massiv[item].value
        return self.my_massiv[item].start_value

    def __setitem__(self, key, value):
        self.my_massiv[key].value = value

    def __str__(self):
        lst = ''
        for i in self.my_massiv:
            if i.value:
                lst += str(i.value) + ' '
            else:
                lst += str(i.start_value) + ' '
        return lst.strip()

class Integer:
    def __init__(self, start_value=0):
        self.start_value = start_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__value = value

# Next test

class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

class CellInteger:
    value = IntegerValue()
    def __init__(self, value=0):
        self.value = value

class TableValues:
    def __init__(self, rows, cols, cell):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(self.cols)) for _ in range(self.rows))

    def __getitem__(self, item):
        a, b = item
        if b >= self.cols or a >= self.rows:
            return
        return self.cells[a][b].value

    def __setitem__(self, key, value):
        a, b = key
        if b >= self.cols or a >= self.rows:
            return
        self.cells[a][b].value = value

# Next test


class StackObjAAA:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackAAA:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if not self.top:
            self.top = obj
        elif self.top.next == None:
            self.top.next = obj
        else:
            slider = self.top
            while slider.next:
                slider = self.top.next
            slider.next = obj

    def pop(self):
        if not self.top:
            return
        if self.top.next == None:
            self.top = None
        else:
            slider = self.top
            while slider.next:
                c = slider
                slider = slider.next
            c.next = None
            return slider

    def check_indx(self, indx):
        if not isinstance(indx, int):
            raise IndexError('неверный индекс')
        if not (0 <= indx < self.__len__()):
            raise IndexError('неверный индекс')

    def __len__(self):
        n = 1
        slider = self.top
        while slider.next:
            slider = slider.next
            n += 1
        return n

    def __getitem__(self, item):
        self.check_indx(item)
        slider = self.top
        while item:
            slider = slider.next
            item -= 1
        return slider

    def __setitem__(self, key, value):
        self.check_indx(key)
        slider = self.top
        while key:
            c = slider
            slider = slider.next
            key -= 1
        c.next = value
        value.next = slider.next

# Next test

class  RadiusVector:
    def __init__(self, *args):
        self.coords = (args)

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        c = list(self.coords)
        c[key] = value
        self.coords = tuple(c)


# Next test

class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell_1() for _ in range(3)) for _ in range(3))

    def clear(self):
        for i in self.pole:
            for j in i:
                j.is_free = True
                j.value = 0

    def check_int(self, item):
        if not all(map(lambda x: 0 <= x < len(self.pole), item)):
            raise IndexError('неверный индекс клетки')

    def check_slice(self, item):
        c = list(filter(lambda x: type(x) == int, item))
        if c:
            for i in c:
                if not 0 <= i < len(self.pole):
                    raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        if all(map(lambda x: type(x) == int, item)):
            self.check_int(item)
            return self.pole[item[0]][item[1]].value
        if any(map(lambda x: type(x) == slice, item)):
            self.check_slice(item)
            if type(item[1]) == slice:
                return tuple(map(lambda x: x.value, self.pole[item[0]][item[1]]))
            if type(item[0]) == slice:
                my_list = []
                for i in self.pole:
                    my_list.append(i[item[1]].value)
                return tuple(my_list)

    def __setitem__(self, key, value):
        if all(map(lambda x: type(x) == int, key)):
            self.check_int(key)
            if self.pole[key[0]][key[1]].is_free == False:
                raise ValueError('клетка уже занята')
            self.pole[key[0]][key[1]].is_free = False
            self.pole[key[0]][key[1]].value = value
        elif any(map(lambda x: type(x) == slice, key)):
            self.check_slice(key)
            for i in range(len(value)):
                if not self.pole[key[0]][key[1]][i]:
                    raise ValueError(f'клетка {self.pole[key[0]][key[1]][i]} уже занята')
                self.pole[key[0]][key[1]][i].value = value[i]


class Cell_1:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

# Next test

class Thing:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if isinstance(value, (int, float)):
            self.__weight = value

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.thing_list = []

    def max_w(self):
        max_w = sum(map(lambda x: x.weight, self.thing_list))
        return max_w

    def add_thing(self, thing):
        if self.max_weight <= thing.weight + self.max_w():
            raise ValueError('превышен суммарный вес предметов')
        self.thing_list.append(thing)

    def check_indx(self, item):
        if type(item) != int or not -len(self.thing_list) <= item < len(self.thing_list):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        return self.thing_list[item]

    def __setitem__(self, key, value):
        self.check_indx(key)
        if self.max_w() - self.thing_list[key].weight + value.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.thing_list[key] = value

    def __delitem__(self, key):
        self.check_indx(key)
        del self.thing_list[key]

# Next test

class Cell_2:
    def __init__(self, value):
        self.value = value

class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.my_dict = {}

    def my_func(self):
        lst_1 = []
        lst_2 = []
        for a, b in self.my_dict.keys():
            lst_1.append(a)
            lst_2.append(b)
        return max(lst_1) + 1, max(lst_2) + 1

    def add_data(self, row, col, data):
        if (row, col) in self.my_dict:
            self.my_dict[(row, col)] = data
        else:
            self.my_dict[(row, col)] = data
            self.rows, self.cols = self.my_func()

    def remove_data(self, row, col):
        if (row, col) not in self.my_dict:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.my_dict[(row, col)]
        self.rows, self.cols = self.my_func()

    def check(self, val):
        if type(val) != tuple or len(val) != 2:
            raise ValueError('данные по указанным индексам отсутствуют')
        if (val[0], val[1]) not in self.my_dict.keys():
            raise ValueError('данные по указанным индексам отсутствуют')

    def __getitem__(self, item):
        self.check(item)
        a, b = item
        return self.my_dict[(a,b)].value

    def __setitem__(self, key, value):
        a, b = key
        if (a, b) in self.my_dict:
            self.my_dict[(a, b)].value = value
        else:
            self.add_data(a, b, Cell_2(value))


