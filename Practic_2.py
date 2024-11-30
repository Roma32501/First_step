class Car:
    def __init__(self, model=None):
        self.__model = model

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        if type(model) == str and 2 < len(model) < 100:
            self.__model = model


# Следующая задача

class WindowDlg:
    def __init__(self, title: str, width: int, height: int):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) == int and 0 <= width <= 1000:
            self.__width = width
            return self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) == int and 0 <= height <= 1000:
            self.__height = height
            return self.show()


# Слудеющая задача
class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next == None:
            self.__next = next

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

class Stack:
    MY_LIST = []
    def __init__(self):
        self.top = None
        self.next_obj = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
        elif self.top.next == None:
            self.next_obj = obj
            self.top.next = self.next_obj
        else:
            self.next_obj.next = obj
            self.next_obj = obj
    def pop(self):
        if self.top == None:
            return None
        elif self.top.next == None:
            c = self.top
            self.top = None
            return c
        else:
            obj_1 = self.top
            while obj_1.next != self.next_obj:
                obj_1 = obj_1.next
            c = self.next_obj
            obj_1.next = None
            self.next_obj = obj_1
            return c


    def get_data(self):
        my_list = []
        if self.top == None:
            return my_list
        obj_1 = self.top
        my_list.append(obj_1.data)
        while obj_1.next != None:
            obj_1 = obj_1.next
            my_list.append(obj_1.data)
        return my_list


#Следующая задача

class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    def __init__(self, x=0, y=0):
        if self.check(x) and self.check(y):
            self.__x = x
            self.__y = y
        else:
            self.__x = 0
            self.__y = 0

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if self.check(x):
            self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if RadiusVector2D.check(y):
            self.__y = y
    @classmethod
    def check(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return (vector.x**2 +vector.y**2)

cor = RadiusVector2D(-102, 123)
r4 = RadiusVector2D(4.5, 5.5)



# Следующая задача

class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_obj(obj, x)
            if obj_next is None:
                break
            obj = obj_next
        return obj.value
    @classmethod
    def get_obj(cls, obj, x):
        if x[obj.index] == 1:
            return obj.left
        return obj.right

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


class TreeObj:
    def __init__(self, index, value=None):
        self.index = index
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
            return self.__right
    @right.setter
    def right(self, right):
        self.__right = right



# 03.10.2024
class Person:
    def __init__(self, old=0, name=0):
        self.__old = old
        self.__name = name
    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

#Следующая задача
class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x0 = self.y0 = 0
class PathLines:
    def __init__(self, *args):
        self.args = args
        for i in range(1, len(self.args)):
            args[i].x0 = args[i-1].x
            args[i].y0 = args[i-1].y

    def get_path(self):
        my_list = []
        for i in self.args:
            my_list.append(i)
        return my_list

    def get_length(self):
        lenght = 0
        for i in self.args:
            lenght += ((i.x-i.x0)**2 + (i.y-i.y0)**2)**0.5
        return lenght

    def add_line(self, line):
        line.x0 = self.args[-1].x
        line.y0 = self.args[-1].y
        lst = list(self.args)
        lst.append(line)
        self.args = tuple(lst)

# Следующая задача
class PhoneBook():
    def __init__(self):
        self.my_list = []

    def add_phone(self, phone):
        self.my_list.append(phone)

    def remove_phone(self, indx):
        self.my_list.pop(indx)
    def get_phone_list(self):
        return self.my_list

class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
    @property
    def num(self):
        return self.__number
    @num.setter
    def num(self, number):
        if isinstance(number, int) and len(str(number)) == 11:
            self.__number = number

    @property
    def name(self):
        return self.__fio
    @name.setter
    def name(self, fio):
        if isinstance(fio, str):
            self.__fio = fio


#Дескрипторы
class Integer:
    @classmethod
    def value_int(cls, coord):
        if type(coord) != int:
            raise ValueError('Не правильно введённые значения')

    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        self.value_int(value)
        print(f'__set__:{self.name} = {value}')
        setattr(instance, self.name, value)

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

#следующая задача
class FloatValue:
    @classmethod
    def value_float(cls, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        self.value_float(value)
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()
    def __init__(self, value = 0.0):
        self.value = value

class TableSheet:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.cells = [[Cell() for _ in range(m)]for _ in range(n)]



table = TableSheet(5, 3)
k = 0.0
for i in range(len(table.cells)):
    for j in range(len(table.cells[0])):
        table.cells[i][j] = Cell(k)
        k += 1.0

#Следующая задача

# class ValidateString:
#     def __init__(self, min_length=3, max_length=100):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def validate(self, st):
#         return isinstance(st, str) and self.min_length <= len(st) <= self.max_length

# class StringValue:
#     def __init__(self, validator=ValidateString()):
#         self.validator = validator
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if self.validator.validate(value):
#             instance.__dict__[self.name] = value

# class RegisterForm:
#     login = StringValue()
#     password = StringValue()
#     email = StringValue()
#
#     def __init__(self, login, password, email):
#         self.login = login
#         self.password = password
#         self.email = email
#
#     def get_fields(self):
#         return [self.login, self.password, self.email]
#
#     def show(self):
#         print(f'<form> \n'
#               f'Логин: {self.login} \n'
#               f'Пароль:  {self.password} \n'
#               f'Email: {self.email} \n'
#               f'</form>')

#Следующая задача

class SuperShop:
    def __init__(self, name=None):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class StringValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) == str and 2 <= len(value) <= 50:
            instance.__dict__[self.name] = value

class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)

class Product:
    name = StringValue()
    price = PriceValue()
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Следующая задача

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if sum(map(lambda x: x.weight, self.things)) + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.things.pop(indx)

    def get_total_weight(self):
        return sum(map(lambda x: x.weight, self.things))


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# Следующая задача

class TVProgram:
    def __init__(self, name_tv):
        self.name = name_tv
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i in self.items:
            if indx == i.uid:
                self.items.remove(i)


class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id
    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = duration

# Магический метод __getattribute__

class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):
        if item == '_Point__x':
            raise ValueError('Приватный атрибут')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError('Не называть свойство z')
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print(f'Атрибута {item} не существует')
        return ''

    def __delattr__(self, item):
        object.__delattr__(self, item)

#Следующая задача

class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    def __setattr__(self, key, value):
        if key in ('title', 'author') and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key in ('pages', 'year') and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

# Следующая задача

class Shop:
    def __init__(self, name_shop):
        self.name_shop = name_shop
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    ID = 0
    @classmethod
    def my_id(cls):
        cls.ID += 1
        return cls.ID

    def __init__(self, name, weight, price):
        self.id = self.my_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key in ('price', 'weight') and (type(value) not in (int, float) or value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


# Следующая задача

class LessonItem:
    my_dict = {'title': str, 'practices': int, 'duration': int}
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.my_dict and self.my_dict[key] != type(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('practices', 'duration') and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)
    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        return

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)

#Следующая задача

class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        res = self.exhibits[indx]
        return f'Описание экспоната {res.name}: {res.descr}'

class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr

class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr

class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr




# Следующая задача

class SmartPhone:
    def __init__(self, name):
        self.name = name
        self.apps = []

    def add_app(self, app):
        if type(app) not in [type(x) for x in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)

class AppVK:
    def __init__(self):
        self.name = 'ВКонтакте'

class AppYouTube:
    def __init__(self, memory_max):
        self.name = 'YouTube'
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, phone_list: dict):
        self.name = 'Phone'
        self.phone_list = phone_list


# Next test

class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, r):
        self.__radius = r

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value < 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


# Next test
class D:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return property() if instance is None else instance.__dict__[self.name]

    def __set__(self, instance, value):
        if Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION:
            setattr(instance, self.name, value)
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    a = D()
    b = D()
    c = D()
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key == 'MIN_DIMENSION' or key == 'MAX_DIMENSION':
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)

# Next test
import time
class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        try:
            if self.date is None:
                object.__setattr__(self, key, value)
            else:
                return
        except AttributeError:
            object.__setattr__(self, key, value)



class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        try:
            if self.date is None:
                object.__setattr__(self, key, value)
            else:
                return
        except AttributeError:
            object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    MY_DICT = {'Mechanical': 1, 'Aragon': 2, 'Calcium': 3}

    def __init__(self):
        self.slot = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if not self.slot[slot_num]:
            if self.MY_DICT[filter.__class__.__name__] == slot_num:
                self.slot[slot_num] = filter

    def remove_filter(self, slot_num):
        self.slot[slot_num] = None

    def get_filters(self):
        return tuple(map(lambda x: x, self.slot.values()))

    def water_on(self):
        flag = False
        if all(map(lambda x: x is not None, self.slot.values())):
            flag = True
        else:
            return flag
        if all(map(lambda x: 0 < (time.time() - x.date) < self.MAX_DATE_FILTER, self.slot.values())):
            flag = True
        else:
            flag = False
        return flag

