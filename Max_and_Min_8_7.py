user_list = [float(figure) for figure in input('Введите ряд чисел через пробел: ').split()]
maxi = user_list.index(max(user_list))
mini = user_list.index(min(user_list))
user_list[maxi], user_list[mini] = user_list[mini], user_list[maxi]
print('Список с перевёрнутыми MAX и MIN:', user_list)
