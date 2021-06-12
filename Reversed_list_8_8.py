user_list = [float(figure) for figure in input('Введите ряд чисел через пробел: ').split()]
for figure in reversed(user_list):
    print(figure, end=' ')
