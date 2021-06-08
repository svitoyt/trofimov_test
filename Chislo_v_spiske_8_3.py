user_list = [float(figure) for figure in input('Введите ряд чисел через пробел: ').split()]
numder = float(input('Введите число для проверки: '))
if numder in user_list:
    print('Число есть в списке')
else:
    print('Числа нет в списке')
