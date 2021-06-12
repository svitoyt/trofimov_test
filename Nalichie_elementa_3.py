item = int(input('Введите число: '))
list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
if item in list_:
    print('В списке есть', item)
else:
    print('В списке нет числа', item)
