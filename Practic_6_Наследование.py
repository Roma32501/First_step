class Animal:
    def __init__(self, name, old):
        if type(name) == str:
            self.name = name
        if type(old) == int and old > 0:
            self.old = old

    def get_info(self):
        value = list(self.__dict__.values())
        return f'{value[0]}: {value[1]}, {value[2]}, {value[3]}'


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

# Next test
global_id = 0
class Thing:
    count = 0
    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        Thing.count += 1
        self.name = name
        self.price = price
        self.id = self.count
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)

class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims

class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


# Next test

class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):
    def __init__(self, methods=None):
        if methods == None:
            super().__init__()
        else:
            super().__init__(methods)

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return getattr(self, method.lower())(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f'url: {request['url']}'

# Next test

class Singleton: # Класс в котором можно создать лишь один объект как в базовом так и в дочернем классе
    _instance = None
    _instance_base = None
    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name
class Game2(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


# Next test

class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        if self._is_valid(*args):
            return
        else:
            raise ValueError('данные не прошли валидацию')

class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) != int or not self.min_value <= data <= self.max_value:
            raise ValueError('данные не прошли валидацию')
        return True
class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) != float or not self.min_value <= data <= self.max_value:
            raise ValueError('данные не прошли валидацию')
        return True

# Next test

class Layer:
    def __init__(self, next_layer=None):
        self.next_layer = next_layer
        self.name = 'Layer'

    def __call__(self, *args, **kwargs):
        self.next_layer = args[0]
        return args[0]

class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'

class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'

class NetworkIterator:
    def __init__(self, slot):
        self.slot = slot

    def __iter__(self):
        while self.slot:
            yield self.slot
            self.slot = self.slot.next_layer


# Next test

class Vector:
    def __init__(self, *args):
        if all(map(lambda x: isinstance(x, (int, float)), args)):
            self.coords = args

    def check_size_vector(self, v_1, v_2):
        if len(v_1.coords) != len(v_2.coords):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self.check_size_vector(self, other)
        new_coords = tuple(map(lambda x: sum(x), zip(self.coords, other.coords)))
        return Vector(*new_coords)

    def __sub__(self, other):
        self.check_size_vector(self, other)
        new_coords = tuple(map(lambda x, y: x - y, self.coords, other.coords))
        return Vector(*new_coords)

    def get_coords(self):
        return self.coords

class VectorInt(Vector):
    def __init__(self, *args):
        if not all(map(lambda x: isinstance(x, int), args)):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def check_int(self, coords):
        if not all(map(lambda x: type(x) == int, coords)):
            return False
        return True

    def __add__(self, other):
        if self.check_int(other.coords):
            self.check_size_vector(self, other)
            new_coords = tuple(map(lambda x: sum(x), zip(self.coords, other.coords)))
            return VectorInt(*new_coords)
        return super().__add__(other)

    def __sub__(self, other):
        if self.check_int(other.coords):
            self.check_size_vector(self, other)
            new_coords = tuple(map(lambda x, y: x - y, self.coords, other.coords))
            return VectorInt(*new_coords)
        return super().__sub__(other)



# Next test

class ListInteger(list):
    def __init__(self, *args):
        if not all(map(lambda x: type(x) == int, *args)):
            raise TypeError('можно передавать только целочисленные значения')
        super().__init__(*args)

    def __setitem__(self, key, value):
        if type(key) != int or type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, __object):
        if type(__object) != int:
            raise TypeError('можно передавать только целочисленные значения')
        super().append(__object)

# Next test

class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, things=None):
        if things == None:
            super().__init__()
        elif things and not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        elif things and not all(isinstance(x, Thing) for x in things):
            raise TypeError('ключами могут быть только объекты класса Thing')
        else:
            super().__init__(things)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)

# Next test

class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.old = old
        self.weight = weight
class Plants(Protists):
    pass
class Animals(Protists):
    pass
class Mosses(Plants):
    pass
class Flowering(Plants):
    pass
class Worms(Animals):
    pass
class Mammals(Animals):
    pass
class Human(Mammals):
    pass
class Monkeys(Mammals):
    pass
class Monkey(Monkeys):
    def __init__(self, *args):
        super().__init__(*args)
class Person(Human):
    def __init__(self, *args):
        super().__init__(*args)
class Flower(Flowering):
    def __init__(self, *args):
        super().__init__(*args)
class Worm(Worms):
    def __init__(self, *args):
        super().__init__(*args)


lst = [
    {Monkey: ("мартышка", 30.4, 7)},
    {Monkey: ("шимпанзе", 24.6, 8)},
    {Person: ("Балакирев", 88, 34)},
    {Person: ("Верховный жрец", 67.5, 45)},
    {Flower: ("Тюльпан", 0.2, 1)},
    {Flower: ("Роза", 0.1, 2)},
    {Worm: ("червь", 0.01, 1)},
    {Worm: ("червь 2", 0.02, 1)}
]

# Next test

class Tuple(tuple):
    def __init__(self, iter_object):
        if hasattr(iter_object, '__iter__'):
            self.iter_object = iter_object


    def __add__(self, other):
        if hasattr(other, '__iter__'):
            new_list_self = [i for i in self.iter_object]
            new_list_other = [i for i in other]
            new_list_self.extend(new_list_other)
            return Tuple(tuple(new_list_self))


# Next test

class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

class VideoRating:
    def __init__(self):
        self.__rating = 0
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, val):
        if not isinstance(val, int) or not 0 <= val <= 5:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = val


# Next test

class IteratorAttrs:
    def __init__(self):
        self.a = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.a += 1
        if self.a < len(self.__dict__) - 1:
            return list(self.__dict__.items())[self.a]
        else:
            raise StopIteration

class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):

        if isinstance(model, str):
            self.model = model
        if isinstance(size, tuple) and len(size) == 2:
            self.size = size
        if isinstance(memory, int):
            self.memory = memory
        super().__init__()

# Функция uper() и делегирование
# Nest test

class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm

# Next test

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date

class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu
class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims

class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old

class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel

# Next test

class Thing:
    def __init__(self, name, weight):
        self.name = self.check_name(name)
        self.weight = self.check_weight(weight)

    @staticmethod
    def check_name(_str):
        if type(_str) != str:
            raise ValueError('Not str')
        return _str

    @staticmethod
    def check_weight(_float):
        if type(_float) not in (float, int):
            raise ValueError('Not float')
        return _float

class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = self.check_name(author)
        self.date = self.check_name(date)

class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = self.check_weight(memory)
        self.cpu = self.check_name(cpu)

class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = self.check_weight(dims)

class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = self.check_name(model)
        self.old = old

class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = self.check_name(model)
        self.wheel = self.checl_wheel(wheel)

    @staticmethod
    def checl_wheel(wheel):
        if type(wheel) != bool:
            raise ValueError
        return wheel

# Next tesr

class Thing:
    def __init__(self, name, weight):
        self.name = self.check_name(name)
        self.weight = self.check_weight(weight)

    @staticmethod
    def check_name(_str):
        if type(_str) != str:
            raise ValueError('Not str')
        return _str

    @staticmethod
    def check_weight(_float):
        if type(_float) not in (float, int):
            raise ValueError('Not float')
        return _float

class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = self.check_name(author)
        self.date = self.check_name(date)

class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = self.check_weight(memory)
        self.cpu = self.check_name(cpu)

class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = self.check_weight(dims)

class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = self.check_name(model)
        self.old = old

class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = self.check_name(model)
        self.wheel = self.checl_wheel(wheel)

# Next test

class SellItem:
    def __init__(self, name, price):
        self.name = self.check_str(name)
        self.price = self.check_int_or_float(price)

    @staticmethod
    def check_str(item):
        if type(item) != str:
            raise ValueError
        return item

    @staticmethod
    def check_int_or_float(item):
        if not isinstance(item, (int, float)):
            raise ValueError
        return item

class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square

class Agency:
    def __init__(self, name):
        if type(name) == str:
            self.name = name
        self.list_obj = []

    @staticmethod
    def check_obj_in_class(obj):
        if not isinstance(obj, (Land, Flat, House)):
            raise ValueError

    def add_object(self, obj):
        self.check_obj_in_class(obj)
        self.list_obj.append(obj)

    def remove_object(self, obj):
        self.check_obj_in_class(obj)
        self.list_obj.remove(obj)

    def get_objects(self):
        return self.list_obj

# Next test

class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


# Next test

def integer_params_decorated(func):
    def wrapper(*args, **kwargs):
        for i in args[1::]:
            if type(i) != int:
                raise TypeError("аргументы должны быть целыми числами")
        for i in kwargs.values():
            if type(i) != int:
                raise TypeError("аргументы должны быть целыми числами")
        return func(*args, **kwargs)
    return wrapper

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
    return cls
@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]

# Next test

class SoftList(list):
    def __getitem__(self, item):
        if item not in range(-len(self), len(self)):
            return False
        else:
            return super().__getitem__(item)

# Next test

class StringDigit(str):
    def __init__(self, string: str):
        self.string = string
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        super().__init__()

    def __add__(self, other):
        if type(other) == str and not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return self.__class__(self.string + other)

    def __radd__(self, other):
        if type(other) == str and not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return self.__class__(other + self.string)

# Next test

class ItemAttrs:

    def __getitem__(self, item):
        attr = {k:v for k, v in enumerate(self.__dict__.values())}
        return attr[item]

    def __setitem__(self, key, value):
        attr = {k: v for k, v in enumerate(self.__dict__.items())}
        self.__dict__[attr[key][0]] = value

class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Private and protect atribute

# Next test
class Integer:
    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Animal:
    name = Integer()
    kind = Integer()
    old = Integer()
    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old

animal_1 = Animal('Васька', 'дворовый кот', 5)
animal_2 = Animal('Рекс', 'немецкая овчарка', 8)
animal_3 = Animal('Кеша', 'попугая', 3)
animals = [animal_1, animal_2, animal_3]

class Animal_2:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if type(val) == str:
            self.__name = val

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, val):
        if type(val) == str:
            self.__kind = val

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, val):
        if type(val) == int:
            self.__old = val



# Next test

class Furniture:
    def __init__(self, name, weight):
        self._name = self.__verify_name(name)
        self._weight = self.__verify_weight(weight)

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        return name

    def __verify_weight(self, weight):
        if not weight > 0 or not isinstance(weight, (int, float)):
            raise TypeError('вес должен быть положительным числом')
        return weight

    def __setattr__(self, key, value):
        if key == '_name' and type(value) != str:
            raise TypeError('название должно быть строкой')
        if key == '_weight' and type(value) not in (int, float) or not value > 0:
            raise TypeError('вес должен быть положительным числом')
        object.__setattr__(self, key, value)

    def get_attrs(self):
        return tuple(self.__dict__.values())

class Closet(Furniture):
    def __init__(self, name, weight, tp: bool, doors: int):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


# Next test

class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность

class TemperatureView(Observer):
    def update(self, data):
        print(f'Текущая температура {data.temp}')

class PressureView(Observer):
    def update(self, data):
        print(f'Текущее давление {data.press}')

class WetView(Observer):
    def update(self, data):
        print(f'Текущая влажность {data.wet}')

# Next test

class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = self.check_str(model)
        self._mass = self.check_int_float(mass)
        self._speed = self.check_int_float(speed)
        self._top = self.check_int_float(top)

    def check_int_float(self, item):
        if type(item) not in (int, float) or not item > 0:
            raise TypeError('неверный тип аргумента')
        return item

    def check_str(self, item):
        if type(item) != str:
            raise TypeError('неверный тип аргумента')
        return item

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self.check_int(chairs)

    def check_int(self, item):
        if type(item) != int:
            raise TypeError('неверный тип аргумента')
        return item

class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons: dict):
        super().__init__(model, mass, speed, top)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = self.check(weapons)

    def check(self, item: dict):
        if not all(map(lambda x: type(x[0]) == str and type(x[1]) == int, item.items())):
            raise TypeError('неверный тип аргумента')


# Next test

def class_log(lof_lst):
    def log_method(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, integer_params_decorated(v))
        return cls
    def integer_params_decorated(func):
        def wrapper(*args, **kwargs):
            lof_lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return log_method

vector_log = []   # наименование (vector_log) в программе не менять!
@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

# Next test

CURRENT_OS = 'windows'   # 'windows', 'linux'

class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

class FileDialogFactory:
    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)

    def __new__(cls, title, path, exts):
        if CURRENT_OS == 'windows':
             return cls.create_windows_filedialog(title, path, exts)
        if CURRENT_OS == 'linux':
            return cls.create_linux_filedialog(title, path, exts)
        return

# Next test, Полиморфизм и абстрактные методы

class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

class Lector(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f'Лектор {self._fio}: предмет {self._subject}'

class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return f'Эксперт {self._fio}: предмет {self._subject}'

# Next test

class ShopInterface:
    ID = 0
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(ShopInterface):
    @classmethod
    def id_valid(cls):
        cls.ID += 1
        return cls.ID
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.id_valid()

    def __setattr__(self, key, value):
        if key == '_name' and not isinstance(value, str):
            raise  ValueError
        if key in ('_weight', '_price') and not isinstance(value, (int, float)):
            raise ValueError
        object.__setattr__(self, key, value)

    def get_id(self):
        return self.__id

# Next test

class Validator:
    def __is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __is_valid(self, data):
        if not isinstance(data, float) or not self.min_value <= data <= self.max_value:
            return False
        return True

    def __call__(self, *args, **kwargs):
        return self.__is_valid(args[0])

# Next test
from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        return

    def get_info(self):
        return f'Базовый класс Model'

class ModelForm(Model):
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self.id = hash((self._login, self._password))

    def get_pk(self):
        return self.id

# Next test

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass

class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top == None:
            self._top = obj
        else:
            my_obj = self._top
            while my_obj._next:
                my_obj = my_obj._next
            my_obj._next = obj

    def pop_back(self):
        my_obj = self._top
        if self._top == None:
            return None
        elif self._top._next == None:
            self._top = None
            return my_obj
        else:
            c = my_obj._next
            while c._next:
                my_obj = my_obj._next
                c = my_obj._next
            my_obj._next = None
            return c

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

# Next test

class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.__name = name
        self.__population = population
        self.__square = square

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, item):
        if type(item) == int and item > 0:
            self.__population = item

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, item):
        if isinstance(item, (int, float)) and item > 0:
            self.__square = item

    def get_info(self):
        return f'{self.__name}: {self.__square}, {self.__population}'

# Next test

class Track:
    def __init__(self, *args):
        self.__points = []
        if type(args[0]) == int and type(args[1]) == int:
            self.__points.append(PointTrack(args[0], args[1]))
        for i in args:
            if isinstance(i, PointTrack):
                self.__points.append(i)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points = [pt] + self.__points

    def pop_back(self):
        self.__points.pop(-1)

    def pop_front(self):
        self.__points.pop(0)

class PointTrack:
    def __init__(self, x, y):
        self.x, self.y = self.check(x), self.check(y)

    def check(self, item):
        if isinstance(item, (int, float)):
            return item
        raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.x}, {self.y} '

# Next test

class Food:
    def __init__(self, name, weight, calories):
        self._name = name if type(name) == str else None
        self._weight = weight if type(weight) in (int, float) and weight > 0 else None
        self._calories = calories if type(calories) == int and calories > 0 else None

class BreadFood(Food):
    def __init__(self, name, weight, calories, white: bool):
        super().__init__(name, weight, calories)
        self._white = white

class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary: bool):
        super().__init__(name, weight, calories)
        self._dietary = dietary

class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish  = fish

# Множественное наследование
# Next test

class Digit:
    def __init__(self, value):
        self._value = self.check_digit(value)

    def check_digit(self, value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        return value

class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Positive(Digit):
    def __init__(self, value):
        if type(value) in (int, float) and not value > 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Negative(Digit):
    def __init__(self, value):
        if type(value) in (int, float) and not value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class PrimeNumber(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass

#Next test

class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id

class ShopGenericView:
    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items())

class ShopUserView:
    def __str__(self):
        st = ''
        for k, v in self.__dict__.items():
            if k == '_id':
                continue
            st += f'{k}: {v}\n'
        return st

class Book(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


# Next test
class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')

class GeneralView:
    allowed_methods = ('POST', 'PUT', 'DELETE')

    def render_request(self, request: dict):
        if len(request) == 2 and request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        else:
            method_request = request.get('method').lower()
            c = getattr(self, method_request)
            return c(request)

class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )

# Next test

class Money:
    def __init__(self, value):
        self.check_int_or_float(value)
        self._money = value

    def check_int_or_float(self, value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self.check_int_or_float(value)
        self._money = value

class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)
        if type(self) != type(other):
            raise TypeError('Разные типы объектов')
        return self.__class__(self.money - other.money)

    def __rsub__(self, other):
        if type(other) in (int, float):
            return self.__class__(other - self.money)
        if type(self) != type(other):
            raise TypeError('Разные типы объектов')
        return self.__class__(other.money - self.money)


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"

class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"

# __slots__
import timeit
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def get_line(self):
        self.x += 1
        del self.y
        self.y = self.x + 10
        return (self.x**2 + self.y**2) ** 0.5

class Point2D:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def get_line(self):
        self.x += 1
        del self.y
        self.y = self.x + 10
        return (self.x**2 + self.y**2) ** 0.5

# pt = Point(1, 2)
# pt2D = Point(10, 20)
#
# t = timeit.timeit(pt.get_line)
# t2 = timeit.timeit(pt2D.get_line)
# print(t, t2)

# Next test

class Person:
    __slots__ = ('_fio', '_old', '_job')
    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job

persons = [Person('Суворов', 52, 'полководец'),
           Person('Рахманинов', 50, 'пианист, композитор'),
           Person('Балакирев', 34, 'программист и преподаватель'),
           Person('Пушкин', 32, 'поэт и писатель')
           ]

# Next test

class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period

class SolarSystem:
    INSTANCE = None
    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE == None:
            cls.INSTANCE = object.__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune',)
    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)

# Next test

class Star:
    __slots__ = ('_name', '_massa', '_temp')
    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp

class Star_ship(Star):
    __slots__ = ('_type_star', '_radius')
    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius
class WhiteDwarf(Star_ship):
    __slots__ = ()

class YellowDwarf(Star_ship):
    __slots__ = ()

class RedGiant(Star_ship):
    __slots__ = ()

class Pulsar(Star_ship):
    __slots__ = ()


# Next test

class Note:
    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)

class Notes:
    INSTANCE = None
    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE is None:
            cls.INSTANCE = super().__new__(cls, *args, **kwargs)
        return cls.INSTANCE
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)

    def __getitem__(self, item):
        if type(item) != int and not 0 <= item < 7:
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])

# Next test

class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj

    # здесь добавляйте еще один магический метод для умножения

class Linear(Function):
    def __init__(self, *args):
        super().__init__()
        if len(args) == 2:
            self._k = args[0]
            self._b = args[1]
        elif len(args) == 1 and isinstance(args[0], self.__class__):
            self._k = args[0]._k
            self._b = args[0]._b

    def _get_function(self, x):
        return self._k * x + self._b

# Next test

class Vertex:
    def __init__(self):
        self._links = [] #Объекты класса Link

    @property
    def links(self):
        return self._links

class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, item):
        self._dist = item

class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        if not any(filter(lambda x: {x.v1, x.v2} == {link.v2, link.v1}, self._links)):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def find_path(self, start_v: Vertex, stop_v: Vertex):
        pass





map_graph = LinkedGraph()

v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
v6 = Vertex()
v7 = Vertex()

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))
print(map_graph.find_path(v1, v5))












