class Triangle:
    def __init__(self, a, b, c):
        self._a = self.check_value(a)
        self._b = self.check_value(b)
        self._c = self.check_value(c)
        self.check_triangle(a, b, c)
    def check_value(self, a):
        if type(a) not in (int, float) or a <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        return a

    def check_triangle(self, a, b, c):
        if a + b < c or a + c < b or c + b < a:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

# Next test
class Validattor:
    def __init__(self, min_val, max_val):
        self.min_value = min_val
        self.max_value = max_val

class FloatValidator(Validattor):
    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], float) or not self.min_value < args[0] <= self.max_value:
            raise ValueError('значение не прошло валидацию')
        else:
            return args[0]

class IntegerValidator(Validattor):
    def __call__(self, *args, **kwargs):
        if type(args[0]) != int or not self.min_value < args[0] <= self.max_value:
            raise ValueError('значение не прошло валидацию')
        else:
            return args[0]

def is_valid(lst: list, validators):
    new_lst = []
    for i in lst:
        for j in validators:
            try:
                new_lst.append(j(i))
            except ValueError:
                continue
    return new_lst

# Next test

class Point:
    def __init__(self, *args):
        if len(args) == 2 and all(map(lambda x: type(x) in (int, float), args)):
            self._x = args[0]
            self._y = args[1]
        else:
            self._x = self._y = 0

# Next test

def get_loss(w1, w2, w3, w4):
    try:
        w1 // w2
    except ZeroDivisionError:
        return 'деление на ноль'
    else:
        return 10 * w1 // w2 - 5 * w2 * w3 + w4

# Next test

class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._x1 = x + width
        self._y1 = y + height

    def __setattr__(self, key, value):
        if key in ('_x', '_y', '_width', '_height') and type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height') and value < 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        axis_x1 = set(range(self._x, self._x1 + 1))
        axis_x2 = set(range(rect._x, rect._x1 + 1))
        axis_y1 = set(range(self._y, self._y1 + 1))
        axis_y2 = set(range(rect._y, rect._y1 + 1))
        if axis_y1 & axis_y2 and axis_x1 & axis_x2:
            raise TypeError('прямоугольники пересекаются')


a, b, c, d =Rect(0, 0, 5, 3),\
            Rect(6, 0, 3, 5),\
            Rect(3, 2, 4, 4),\
            Rect(0, 8, 8, 1)
lst_rect = [a, b, c, d]
st_not_collision = set()
st_collision = set()
for i in range(len(lst_rect)):
    try:
        for j in range(1, len(lst_rect) - i):
            lst_rect[i].is_collision(lst_rect[-j])
    except TypeError:
        st_collision.add(lst_rect[i])
        st_collision.add(lst_rect[-j])
    else:
        st_not_collision.add(lst_rect[i])

st_not_collision -= st_collision
lst_not_collision = list(st_not_collision)

# Next test

class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_lenght = self.check_int(min_length)
        self.max_lenght = self.check_int(max_length)
        self.chars = chars if type(chars) == str else ''

    def is_valid(self, string):
        if not self.min_lenght <= len(string) <= self.max_lenght:
            raise ValueError('недопустимая строка')
        if len(self.chars) > 0:
            if all(map(lambda x: x not in string, self.chars)):
                print('проверка 2')
                raise ValueError('недопустимая строка')


    def check_int(self, value):
        if type(value) != int:
            raise ValueError('диапазон должен быть целым числом')
        return value

class LoginForm:
    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request: dict):
        if 'password' not in request.keys() or 'login' not in request.keys():
            raise TypeError('в запросе отсутствует логин или пароль')
        self.login_validator.is_valid(request['login'])
        self.password_validator.is_valid(request['password'])
        self._login = request['login']
        self._password = request['password']

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
lg.form({'login': login, 'password': password})

# Next test



