#Дано словарь, Создать кортеж занчений для первих трьох єлементов словоря.

dict_1 = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
list_1 = [(k, v) for k, v in dict_1.items()]
list_1 = list_1[:3]
print(list_1)
