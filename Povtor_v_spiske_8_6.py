user_list = list(map(int, input('Введите строки через пробел: ').split()))
repeat_list = [item for item in set(user_list) if user_list.count(item) > 1]
print('Повторяющиеся эллементы:', *repeat_list)
