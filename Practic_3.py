import random
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__psw_chars = psw_chars
        self.__min_lenght = min_length
        self.__max_lenght = max_length

    def __call__(self, *args, **kwargs):
        num = random.randint(self.__min_lenght, self.__max_lenght)
        psw = ''.join([random.choice(self.__psw_chars) for _ in range(num)])
        return psw


# Next test

class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, st, *args, **kwargs):
        format = st.split('.')
        for i in self.extensions:
            if i == format[-1]:
                return True

# Next test

class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, st, *args, **kwargs):
        if isinstance(st, str):
            return len(st) in range(self.min_length, self.max_length)

class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, st, *args, **kwargs):
        return set(st).issubset(set(self.chars))

from string import ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True

#Next test

class DigitRetrieve:

    def __call__(self, st, *args, **kwargs):
        if isinstance(st, str):
            if st.isdigit() or st[0] == '-' and st[1:].isdigit():
                return int(st)
            else:
                return None


#Next test

class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, lst, *args, **kwargs):
        if self.type_list not in ('ul', 'ol'):
            text = f'<ul>\n'
            for c in lst:
                text += f'<li>{c}</li>\n'
            text += f'</ul>'
        else:
            text = f'<{self.type_list}>\n'
            for c in lst:
                text += f'<li>{c}</li>\n'
            text += f'</{self.type_list}>'
        return text
#Next text

class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, func, request, *args, **kwargs):
        if 'method' in request and request['method'] == 'GET':
            res = f'GET: {func(request)}'
        elif 'method' not in request:
            res = f'GET: {func(request)}'
        else:
            res = None
        return res

    def __call__(self, request, *args, **kwargs):
        return self.get(self.func, request)

@HandlerGET
def contact(request):
    return "Сергей Балакирев"

#Next test

class Handler:
    def __init__(self, methods=('GET',)):
        self.method = methods

    def get(self, func, request, *args, **kwargs):
        res = f'GET: {func(request)}'
        return res

    def post(self, func, request, *args, **kwargs):
        res = f'POST: {func(request)}'
        return res


    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            name = request.get('method', 'GET')
            if name in self.method:
                if name == 'GET':
                    return self.get(func, request)
                if name == 'POST':
                    return self.post(func, request)

        return wrapper


# Next test

class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        my_list = self.func().split()
        return [int(i) for i in my_list]

# Next test

class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        my_list = []
        def wrapper(*args, **kwargs):
            for i in func().split():
                my_list.append(self.render(i))
            return my_list
        return wrapper

class RenderDigit:
    def __call__(self, st, *args, **kwargs):
        try:
            return int(st)
        except:
            return None


# Next test

class Book:
    MY_DICT = {'title': str, 'author': str, 'pages': int}
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __setattr__(self, key, value):
        if key in self.MY_DICT:
            if self.MY_DICT[key] == type(value):
                object.__setattr__(self, key, value)
            else:
                return
        else:
            return
    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'

# Next test

class Model:
    def __init__(self):
        self.my_list = []
    def query(self, *args, **kwargs):
        self.my_list = [f'{k}={v}' for k,v in kwargs.items()]

    def __str__(self):
        if self.my_list:
            return f'Model:{",".join(self.my_list)}'
        return f'Model'

# Next test

class WordString:
    def __init__(self, string=''):
        self.__string = string

    @property
    def string(self):
        return self.__string
    @string.setter
    def string(self, value):
        self.__string = value

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, indx, *args, **kwargs):
        if self.__len__() > indx:
            return self.__string.split()[indx]
        else:
            raise IndexError('Нет слова с таким индексом')


#Next Test

class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head == None and self.tail == None:
            self.head = obj

        elif self.head != None and self.tail == None:
            self.tail = obj
            self.tail.prev = self.head
            self.head.next = self.tail

        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def __len__(self):
        if self.head == None:
            return 0
        elif self.head and not self.tail:
            return 1
        val = self.head
        n = 1
        while val.next != None:
            n += 1
            val = val.next
        return n

    def remove_obj(self, indx):
        if self.__len__() <= indx:
            raise IndexError('Такого индекса нет')
        if self.__len__() == 0:
            return
        if indx == 0:
            if self.__len__() == 1:
                self.head = self.tail = None
            elif self.__len__() > 1:
                self.head = self.head.next
                self.head.prev = None
        elif (indx + 1) == self.__len__():
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            val = self.head
            while indx != 0:
                val = val.next
                indx -= 1
            val.prev.next = val.next
            val.next.prev = val.prev

    def __call__(self, num, *args, **kwargs):
        val = self.head
        while num != 0:
            val = val.next
            num -= 1
        return val.data



# Next test
class Integer:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        setattr(instance, self.name, value)
class Complex:
    real = Integer()
    img = Integer()
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __abs__(self):
        return (self.real**2 + self.img**2)**0.5


#Next test
import math
class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0 for _ in range(args[0])]
        else:
            self.coords = [i for i in args]

    # def __setattr__(self, key, value):
    #     print(value)
    #     if type(value) in (int, float):
    #         object.__setattr__(self, key, value)
    #     else:
    #         raise ValueError('Не правильный ввод координат')

    def set_coords(self, *args):
        try:
            for i in range(len(args)):
                self.coords[i] = args[i]
        except IndexError:
            return
    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return math.sqrt(sum(map(lambda x: x**2, self.coords)))



#Next test

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.h = hours
        self.m = minutes
        self.s = seconds

    def get_time(self):
        return (self.h * 3600 + self.m * 60 + self.s)

class DeltaClock:
    def __init__(self, cl1, cl2):
        self.cl1 = cl1
        self.cl2 = cl2

    def my_func(self):
        return self.cl1.get_time() - self.cl2.get_time()

    def __str__(self):
        num = self.my_func()
        if num > 0:
            h = num // 3600
            m = (num % 3600) // 60
            s = (num - h * 3600 - m * 60)
        else:
            h = m = s = 0
        return f'{h:02}: {m:02}: {s:02}'

    def __len__(self):
        return self.my_func() if self.my_func() > 0 else 0



#Next test

class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self. measure = measure

    def __setattr__(self, key, value):
        if key == 'name' or key == 'measure' and type(value) == str:
            object.__setattr__(self, key, value)
        if key == 'volume' and type(value) == float:
            object.__setattr__(self, key, value)


    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'

class Recipe:
    def __init__(self, *args):
        self.recept = list(args)

    def add_ingredient(self, ing):
        self.recept.append(ing)

    def remove_ingredient(self, ing):
        self.recept.remove(ing)

    def get_ingredients(self):
        return tuple(self.recept)

    def __len__(self):
        return len(self.recept)


#Next test

class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords

