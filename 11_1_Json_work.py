# 1. Загружаете исходний json
# 2. Преобразовиваете его в словарь

import json


def load_file(file_1):
    f_1 = open(file_1, 'r')
    load = json.load(f_1)
    f_1.close()
    return load


#8. Словарь записиваете в новий файл.
def new_file(file_2, load):
    f_2 = open(file_2, 'w')
    json.dump(load, f_2)
    f_2.close()


#3. Органицовиваете цикл для итерации исходного списка словорей
# 4. В списке словорей по ключам собираете полное ими персони.
# 5. Припомощи метода items из ключей и значений генерируете список кортежей пари ключ-значение.
# 6. По занчению определяете тип и сортируете по типу согласно результирующему json-ну.
# 7. Генерируете все в новий словарь
def main(load):
    new_dict = {}
    for employee in load['employee']:
        full_name = f"{employee['firstName']} {employee['lastName']}"
        list_znach = {'int': [], 'float': [], 'string': [], 'bool': [], 'none_type': []}
        for item in employee.items():
            if type(item[1]) == int:
                list_znach['int'].append(item[0])
            elif type(item[1]) == float:
                list_znach['float'].append(item[0])
            elif type(item[1]) == str:
                list_znach['string'].append(item[0])
            elif type(item[1]) == bool:
                list_znach['bool'].append(item[0])
            else:
                list_znach['none_type'].append(item[0])
        new_dict.update({full_name: list_znach})
    return {'employee': new_dict}


file_1 = 'HW.json'
file_2 = 'HW_result_Andrey.json'

load = load_file(file_1)
task = main(load)
new_file(file_2, task)
