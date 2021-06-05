chislo = int(input('Введите число: '))
list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
if list_.count(chislo) == 0:
    print('В списке нет числа', chislo)
else:
    print('В списке есть', chislo)
