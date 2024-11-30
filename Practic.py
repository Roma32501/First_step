# m2_5_25 = 4_741.98
# m2_25_ = 3_013.06
#
# total = 3_000_000
# sum70 = total*0.8
# sum30 = total*0.3
#
# Площадь_до_25м2 = sum70/m2_5_25
# Площадь_от_25_ = (total-sum70)/m2_25_
#
# print('Итого м2 ям.рем. от 5 до 25 м2 = ', Площадь_до_25м2)
# print('Итого м2 ям.рем. свыше 25 м2 = ', Площадь_от_25_)
import re


class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        return ' '.join(str(i) for i in data)
    def show_table(self):
        if self.is_show == False:
            print('Отображение данных закрыто')
        else:
            print(*self.data)

    def show_graph(self):
        if self.is_show == False:
            print('Отображение данных закрыто')
        else:
            print(f'Графическое отображение данных: {self.set_data(self.data)}')

    def show_bar(self):
        if self.is_show == False:
            print('Отображение данных закрыто')
        else:
            c = ' '.join(str(i) for i in self.data)
            print(f'Столбчатая диаграмма: {c}')

    def set_show(self, fl_show):
        self.is_show = fl_show


#Следующая задача

class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *mem_slots: list):
        self.name = name
        self.z = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]
    def get_config(self):
        text = '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots ))
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.z.name}, {self.z.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {text}']


cpu = CPU('Name', 345)
mem = Memory('Name2', 10)
mem2 = Memory('Name3', 13)
mem3 = Memory('Name4', 20)
mem4 = Memory('Name5', 30)

mb = MotherBoard('Name', cpu, mem, mem2, mem3, mem4)

mb2 = MotherBoard('name2345', CPU('Anather', 340), Memory('Name8', 890))

# Следующая задача!

class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)
    def remove(self, indx):
        del self.goods[indx]
    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
gd1 = TV('Samsung', 13444)
gd2 = TV('LG', 15999)
gd3 = Table('IKEA', 599)
gd4 = Notebook('ASUS', 21000)
gd5 = Notebook('Apple', 42000)
gd6 = Cup('Кружка', 340)
my_list = [gd1, gd2, gd3, gd4, gd5, gd6]
for c in my_list:
    cart.add(c)
(cart.get_list())

# Следующая задача !
import sys
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_object = None


    def link(self, obj):
        self.next_object = obj

#lst_in = list(map(str.strip, sys.stdin.readlines()))


# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     new_obj = ListObject(lst_in[i])
#     obj.link(new_obj)
#     obj = new_obj

# Следующая задача
from random import *
class Cell:
    def __init__(self, mine: bool, around_mines=0, ):
        self.around_mines = around_mines      # число мин вокруг данно клетки
        self.mine = mine        # является ли данная клетка миной
        self.fl_open = True    # открыта клетка или нет

class GamePole:
    def __init__(self, N, M):
        self.N = N     #размер поля
        self.M = M     #число мин на поле
        self.pole = [[Cell(False) for _ in range(self.N)] for _ in range(self.N)]  #двумерный список, размер поля с объектами класса Cell
        self.init()

    def init(self):
        """Растановка М мин в рандомном порядке"""
        count = 0
        while count != self.M:
            x = randint(0, self.N-1)
            y = randint(0, self.N-1)
            if self.pole[x][y].mine:
                continue
            self.pole[x][y].mine = True
            count += 1
        indx = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)

        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].mine == True:
                    for x, y in indx:
                        if 0 <= x + i < self.N and 0 <= y + j < self.N:
                            self.pole[i+x][j+y].around_mines += 1

    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].fl_open == False:
                    self.pole[i][j] = '#'
                else:
                    if self.pole[i][j].mine == True:
                        self.pole[i][j] = '*'
                    else:
                        self.pole[i][j] = self.pole[i][j].around_mines
        return self.pole
        """Отображение поля"""


# Следующая задача
class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка"
obj = AbstractClass()


# Следующая задача
class SingletonFive:
    instance = None
    k = 0
    def __new__(cls, *args, **kwargs):
        cls.k += 1
        if cls.k <= 5:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]


# Следующая задача

TYPE_OS = 2 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    instance = None
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            instance = DialogWindows()
            instance.name = args[0]
            return instance
        elif TYPE_OS != 1:
            instance = DialogLinux()
            instance.name = args[0]
            return instance

    def __int__(self, name):
        self.name = name

dlg = Dialog(123)


#Следующая задача
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(2, 5)
pt_clone = pt.clone()


#Следующая задача
class Factory:
    def build_sequence():
        return []
    def build_number(string):
        return int(string)
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

res = Loader.parse_format("1, 2, 3, -5, 10", Factory)

#Следующая задача

from string import ascii_lowercase, digits
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def __init__(self, name, size=10):
        self.check_name(name) # TextInput.check_name(name) - это означает эту запись
        self.name = name
        self.size = size
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
    @classmethod
    def check_name(cls, name):
        if 2 < len(name) < 50 and map(lambda x: x in cls.CHARS_CORRECT, name):
            return
        else:
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 2 < len(name) < 50 and map(lambda x: x in cls.CHARS_CORRECT, name):
            return
        else:
            raise ValueError("некорректное поле name")
class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

login = FormLogin(TextInput("fgh"), PasswordInput("Пароль"))
html = login.render_template()

#Следующая задача

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    @staticmethod
    def check_card_number(number):
        return all(map(lambda x: len(x) == 4 and x.isdigit(), number.split('-'))) and len(number.split('-')) == 4

    @classmethod
    def check_name(cls, name):
        cls.name = name.split()
        if len(cls.name) == 2:
            return all(map(lambda x: set(x) <= set(cls.CHARS_FOR_NAME), cls.name))
        else:
            return False

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

#Следующая задача
class Video:
    def create(self, name):
        self.name = name
    def play(self):
        print(f'Воспроизведение видео {self.name}')

class YouTube:
    videos = []
    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        k = cls.videos[video_indx]
        Video.play(k)




# Следующая задача
class AppStore:
    app_list = []
    def add_application(self, app):
        self.app_list.append(app)
    def remove_application(self, app):
        self.app_list.remove(app)
    def block_application(self, app):
        app.blocked = True
    def total_apps(self):
        return len(self.app_list)

class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)

#Следующая задача

class Viber:
    list_message = []
    @staticmethod
    def add_message(msg):
        Viber.list_message.append(msg.text)

    @staticmethod
    def remove_message(msg):
        Viber.list_message.remove(msg.text)

    @staticmethod
    def set_like(msg):
        msg.fl_like = [True, False][msg.fl_like]

    @staticmethod
    def show_last_message(number: int):

        return Viber.list_message[-number:]
    @staticmethod
    def total_messages():
        return len(Viber.list_message)

class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))

Viber.set_like(msg)
Viber.remove_message(msg)


#Следующая задача


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.id] = server
        server.router = self
    def unlink(self, server):
        s = self.servers.pop(server.id, False)
        if s:
            s.router = None
    def send_data(self):
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()

class Server:
    server_ip = 1
    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)
    def get_data(self):
        b = self.buffer[:]
        self.buffer.clear()
        return b
    def get_ip(self):
        return self.ip

class Data:
    def __init__(self, msg, ip):
        self.data = msg
        self.ip = ip




class Get:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float) and 0 < x <= 100

    def set_obj(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Не правильные входные данные")
    def get_obj(self):
        return self.__x + 15, self.__y - 12

object = Get()
object.set_obj(100,75)


class Clock:
    def __init__(self, time=0):
        self.__time = time
    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
        else:
            raise ValueError('Нельзя')
    def ger_time(self):
        return self.__time
    def __check_time(self, tm):
        return True if type(tm) == int and 0 <= tm < 1000 else False


class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
    def get_money(self):
        return self.__money
    def add_money(self, mn):
        self.__money += mn.__money
    def __check_money(self, money):
        return type(money) == int and money >= 0


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.__sp = args[0]
                self.__ep = args[1]
        elif len(args) == 4 and all(map(lambda x: type(x) in (int, float), args)):
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


#Следующая задача

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.new_obj = None

    def add_obj(self, obj):
        if self.tail == self.head == None:
            self.new_obj = obj
            self.tail = self.new_obj
            self.head = self.new_obj

        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        if self.head == self.tail == None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            l = self.tail.get_prev()
            self.tail.set_prev(None)
            l.set_next(None)
            self.tail = l

    def get_data(self):
        if self.head == None:
            return []
        k = self.head
        my_list = []
        while k:
            my_list.append(k.get_data())
            k = k.get_next()
        return my_list

class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__prev = prev
        self.__next = next
        self.__data = data

    def set_next(self, obj):
        self.__next = obj
    def set_prev(self, obj):
        self.__prev = obj
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data




import random
import string
class EmailValidator:
    simvol_string = string.ascii_letters + string.digits + '_' + '.'
    def __new__(cls, *args, **kwargs):
        return None
    @classmethod
    def get_random_email(cls):
        random_word_1 = (f'{"".join(random.sample(cls.simvol_string, 7))}...{"".join(random.sample(cls.simvol_string, 3))}')
        e_mail = f'{random_word_1}@gmail.com'
        return e_mail

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        cls.email = email
        if not all(map(lambda x: x in (cls.simvol_string+'@'), email)) or cls.email.count('@') != 1:
            return False
        beginning = re.findall(r'.+@', email)
        if len(*beginning) > 101:
            return False
        end = re.findall(r'@.+', email)
        if len(*end) >51:
            return False
        if re.findall(r'[.][.]', email):
            return False
        if not re.findall(r'@\w+[.]', email):
            return False
        return True
    @staticmethod
    def __is_email_str(email):
        return type(email) == str


res = EmailValidator.check_email("sc_lib@list.ru") # True
print(res)
res = EmailValidator.check_email("sc_lib@list_ru") # False
print(res)

my_mail = EmailValidator.get_random_email()
print(EmailValidator._EmailValidator__is_email_str(123))