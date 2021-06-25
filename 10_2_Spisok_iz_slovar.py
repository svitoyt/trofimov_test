#Дано словарь, преобразовать его в список кортежей.

a_dictionary = {"a": 1, "b": 2, "c": 3}
list_1 = [(k, v) for k, v in a_dictionary.items()]
print(list_1)