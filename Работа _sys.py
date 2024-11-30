import sys

print('Имя скрипта', sys.argv[0])
print('Аргументы командной строки', sys.argv[1:])


a = [i for i in range(3**10)]
print(sys.getsizeof(a))

print(sys.exec_prefix)
print(sys.base_exec_prefix)
print(sys.base_prefix)

print(sys.getwindowsversion())
print(sys.winver)
print(sys.builtin_module_names)