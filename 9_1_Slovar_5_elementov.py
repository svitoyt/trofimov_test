# Создайте словарь с количеством элементов не менее 5-ти.
person = {'first_name': 'Andrey',
       'second_name': 'Trofimov',
       'age': 25,
       'city': 'Moscow',
       'language': 'python'
       }
print(person)

# Поменяйте местами первый и последний элемент объекта.
name = person['first_name']
person['first_name'] = person['language']
person['language'] = name
print(person)

# Удалите второй элемент.
person.pop('second_name')
print(person)

# Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
person['new_key'] = 'new_value'
print(person)


