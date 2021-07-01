#Дано два списка, Создать из них список кортежей.

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = tuple(zip(list_a, list_b))
print(list_c)
