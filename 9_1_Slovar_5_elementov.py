# Создайте словарь с количеством элементов не менее 5-ти.
person = {'first_name': 'Andrey',
       'second_name': 'Trofimov',
       'age': 25,
       'city': 'Moscow',
       'language': 'python'
       }
print(person)

# Поменяйте местами первый и последний элемент объекта.
i_first = list(person.items())[0][1]
i_last = list(person.items())[-1][1]
person['first_name'] = i_last
person['language'] = i_first
print(person)

# Удалите второй элемент.
second = list(person.items())[1]
del person[second[0]]
print(person)

# Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
person.update({'new_key': 'new_value'})
print(person)
