# 1. Загружаете исходний json
# 2. Преобразовиваете его в словарь.

import json

file_1 = 'HW.json'
file_2 = 'HW_result_Andrey.json'


file = open(file_1, 'r')
date = json.load(file)
print(date)

# 3. Органицовиваете цикл для итерации исходного списка словорей
# 4. В списке словорей по ключам собираете полное ими персони.
# 5. Припомощи метода items из ключей и значений генерируете список кортежей пари ключ-значение.
# 6. По занчению определяете тип и сортируете по типу согласно результирующему json-ну.
# 7. Генерируете все в новий словарь

emp_new = {}
for employee in date['employee']:
    full_name = f"{employee['firstName']}, {employee['lastName']}"
    dict_new = {'int': [], 'float': [], 'str': [], 'bool': [], 'non_type': []}
    for item in employee:
        if type(item[1]) == int:
            dict_new['int'].append(item[0])
        elif type(item[1]) == float:
            dict_new['float'].append(item[0])
        elif type(item[1]) == str:
            dict_new['str'].append(item[0])
        elif type(item[1]) == bool:
            dict_new['bool'].append(item[0])
        elif type(item[1]) is None:
            dict_new['non_type'].append(item[0])
    emp_new.update({full_name: dict_new})
print(emp_new)

# 8. Словарь записиваете в новий файл.
json.dump(file_2)
