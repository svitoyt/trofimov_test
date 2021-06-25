#Дано два списка, Создать из них список кортежей.

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = list(zip(list_a, list_b))
print(list_c)

#Еще один вариант решения. Через for.

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
merged_list = [(list_a[i], list_b[i]) for i in range(len(list_a))]
print(merged_list)
