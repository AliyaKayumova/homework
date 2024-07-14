def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [5, 'Отчет', True]
values_dict = {'a' : [1, 2, 3], 'b' : False, 'c' : 18}
print('Распаковка списка: ')
print_params(*values_list)
print('Распаковка словаря: ')
print_params(**values_dict)


values_list_2 = [[57, 'Age'], True]
print('Распаковка + отдельный параметр: ')
print_params(*values_list_2, 42)