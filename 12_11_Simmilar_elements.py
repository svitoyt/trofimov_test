# Проверьте, есть ли в двух наборах какие-либо общие элементы.
# Если да, отобразите общие элементы.
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1 & set2 == set():
    print('Нет одинаковых элементов')
else:
    print('Одинаковые элементы:', set1 & set2 )