user_list = [float(figure) for figure in input('Введите ряд чисел через пробел: ').split()]
mult = 1
summ = 0
for figure in user_list:
    summ = summ + figure
    mult = mult * figure
print('Сумма = ', summ, 'Произведение = ', mult)
