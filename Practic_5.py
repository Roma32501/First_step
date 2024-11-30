# Магическиу методы __iter__, __next__
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

class FRange2D:
    def __init__(self, start=0, stop=0, step=0, rows=0):
        self.fr = FRange(start, stop, step)
        self.rows = rows

    def __next__(self):
        if self.value > self.rows:
            raise StopIteration
        else:
            self.value += 1
            return iter(self.fr)

    def __iter__(self):
        self.value = 0
        return self

fr = FRange2D(0, 10, 1.5, 5)

# Next test

class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst_v = list(self.__dict__.values())
        self.lst_k = list(self.__dict__.keys())

    def __getitem__(self, item):
        if type(item) != int or not 0 <= item < 5:
            raise IndexError('неверный индекс')
        return self.__dict__[self.lst_k[item]]

    def __setitem__(self, key, value):
        if type(key) != int or not 0 <= key < 5:
            raise IndexError('неверный индекс')
        self.__dict__[self.lst_k[key]] = value
        self.lst_v[key] = value

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self):
        if self.value + 1 < 4:
            self.value += 1
            return self.lst_v[self.value]
        else:
            raise StopIteration

# Next test

class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i + 1):
                yield self.lst[i][j]



# Next test

class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
            yield self.lst[i][self.column]

# Next test

class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top == None:
            self.top = obj
        else:
            j = self.top
            while j.next:
                j = j.next
            j.next = obj

    def push_front(self, obj):
        obj.next = self.top
        self.top = obj

    def __len__(self):
        j = self.top
        n = 1
        while j.next:
            j = j.next
            n += 1
        return n

    def check_item(self, item):
        if type(item) != int or not item < self.__len__():
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_item(item)
        j = self.top
        while item:
            j = j.next
            item -= 1
        return j.data

    def __setitem__(self, key, value):
        self.check_item(key)
        j = self.top
        while key:
            j = j.next
            key -= 1
        j.data = value

    def __iter__(self):
        j = self.top
        while j:
            yield j.data
            j = j.next

# Next test

class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value

class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.typ_data = type_data
        self.my_table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def check_item(self, item):
        if len(item) == 2:
            a, b = item
            if type(a) != int or type(b) != int or a not in range(0, self.rows) or b not in range(0, self.cols):
                raise IndexError('неверный индекс')
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_item(item)
        a, b = item
        return self.my_table[a][b].data

    def __setitem__(self, key, value):
        self.check_item(key)
        a, b = key
        if type(value) != self.typ_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.my_table[a][b].data = value

    def __iter__(self):
        for row in self.my_table:
            yield (row[i].data for i in range(len(row)))


# Next test

class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value

class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.typ_data = type_data
        self.my_table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def check_item(self, item):
        if len(item) == 2:
            a, b = item
            if type(a) != int or type(b) != int or a not in range(0, self.rows) or b not in range(0, self.cols):
                raise IndexError('неверный индекс')
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_item(item)
        a, b = item
        return self.my_table[a][b].data

    def __setitem__(self, key, value):
        self.check_item(key)
        a, b = key
        if type(value) != self.typ_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.my_table[a][b].data = value

    def __iter__(self):
        for row in self.my_table:
            yield (row[i].data for i in range(len(row)))


# Next test
import numpy as np
class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            k = len(args[0][0])
            for i in args[0]:
                if k != len(i):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
                for j in i:
                    if type(j) not in (int, float):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.my_matrix = args[0]
        if len(args) == 3:
            self.rows, self.cols, self.fill_value = args[0], args[1], args[2]
            self.my_matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]


    def __setattr__(self, key, value):
        if key in ('rows', 'cols', 'fill_value'):
            if type(value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def check_indx(self, indx):
        if len(indx) == 2:
            a, b = indx
            try:
                self.my_matrix[a][b]
            except IndexError:
                raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        self.check_indx(item)
        a, b = item
        return self.my_matrix[a][b]

    def __setitem__(self, key, value):
        self.check_indx(key)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        a, b = key
        self.my_matrix[a][b] = value

    def check_len_matrix(self, matrix_1, matrix_2):
        if np.shape(matrix_1) != np.shape(matrix_2):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        self.check_len_matrix(self.my_matrix, other.my_matrix)
        if type(other) != int:
            new_matrix = [[self.my_matrix[i][j] + other.my_matrix[i][j] for j in range(len(self.my_matrix[0]))] for i in range(len(self.my_matrix))]
            return Matrix(new_matrix)
        else:
            new_matrix = [[self.my_matrix[i][j] + other for j in range(len(self.my_matrix[0]))] for i in range(len(self.my_matrix))]
            return Matrix(new_matrix)

    def __sub__(self, other):
        if type(other) != int:
            new_matrix = [[self.my_matrix[i][j] - other.my_matrix[i][j] for j in range(len(self.my_matrix[0]))] for i in
                          range(len(self.my_matrix))]
            return Matrix(new_matrix)
        else:
            new_matrix = [[self.my_matrix[i][j] - other for j in range(len(self.my_matrix[0]))] for i in
                          range(len(self.my_matrix))]
            return Matrix(new_matrix)

    def __rsub__(self, other):
        if type(other) != int:
            new_matrix = [[- self.my_matrix[i][j] + other.my_matrix[i][j] for j in range(len(self.my_matrix[0]))] for i in
                          range(len(self.my_matrix))]
            return Matrix(new_matrix)
        else:
            new_matrix = [[- self.my_matrix[i][j] + other for j in range(len(self.my_matrix[0]))] for i in
                          range(len(self.my_matrix))]
            return Matrix(new_matrix)


# Next test
from random import randint
class Cell_1:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0

class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    def __init__(self):
        self.pole = tuple(tuple(Cell_1() for _ in range(3)) for _ in range(3))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    @staticmethod
    def check_item(item):
        if len(item) == 2:
            a, b = item
            if type(a) != int or type(b) != int or a not in range(3) or b not in range(3):
                raise IndexError('некорректно указанные индексы')
        else:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.check_item(item)
        a, b = item
        return self.pole[a][b].value

    def __setitem__(self, key, value):
        self.check_item(key)
        a, b = key
        self.pole[a][b].value = value
        self.check_win_1()
        self.check_win_2()
        self.check_win_3()

    def init(self):
        for i in self.pole:
            for j in i:
                j.value = 0

    def show(self):
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    print('#', end=' ')
                elif j.value == 1:
                    print('X', end=' ')
                elif j.value == 2:
                    print('0', end=' ')
            print()

    def human_go(self):
        while True:
            human_lets_go = str(input('Введите координаты хода, два числа через запятую от 0 до 2 '))
            a, b = tuple(filter(lambda x: x.isdigit(), human_lets_go))
            if int(a) in range(3) and int(b) in range(3):
                if self.pole[int(a)][int(b)].__bool__():
                    self.pole[int(a)][int(b)].value = self.HUMAN_X
                    break
            else:
                print('Эта клетка уже занята')
                continue

    def computer_go(self):
        while True:
            a, b = randint(0, 2), randint(0, 2)
            if self.pole[a][b].__bool__():
                self.pole[a][b].value = self.COMPUTER_O
                break
            else:
                continue
    @property
    def is_human_win(self):
        return self.__is_human_win
    @is_human_win.setter
    def is_human_win(self, vol):
        self.__is_human_win = vol

    @property
    def is_computer_win(self):
        return self.__is_computer_win
    @is_computer_win.setter
    def is_computer_win(self, vol):
        self.__is_computer_win = vol

    @property
    def is_draw(self):
        return self.__is_draw
    @is_draw.setter
    def is_draw(self, vol):
        self.__is_draw = vol

    def check_win_1(self):
        for i in range(len(self.pole)):
            if all(map(lambda x: x.value == 1, self.pole[i])):
                self.is_human_win = True
                return True
            elif all(map(lambda x: x.value == 2, self.pole[i])):
                self.is_computer_win = True
                return True
        return False

    def check_win_2(self):
        if all(self.pole[i][i].value == 1 for i in range(len(self.pole))) \
                or all(self.pole[i][2-i].value == 1 for i in range(len(self.pole))):
            self.is_human_win = True
            return True
        elif all(self.pole[i][i].value == 2 for i in range(len(self.pole))) \
                or all(self.pole[i][2-i].value == 2 for i in range(len(self.pole))):
            self.is_computer_win = True
            return True
        return False

    def check_win_3(self):
        for i in range(len(self.pole)):
            n, k = 0, 0
            for j in range(len(self.pole)):
                if self.pole[j][i].value == 1:
                    n += 1
                    if n == 3:
                        self.is_human_win = True
                        return True
                elif self.pole[j][i].value == 2:
                    k += 1
                    if k == 3:
                        self.is_computer_win = True
                        return True
        return False



    def check_end(self):
        if self.check_win_1() or self.check_win_2() or self.check_win_3():
            return True
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == 0:
                    return False
            self.is_draw = True
            return True
        return False

    def __bool__(self):
        return not self.check_end()

