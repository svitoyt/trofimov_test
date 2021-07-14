import json


class NewClass:

    def __init__(self, load_file='HW.json', new_file='HW_result_Andrey.json'):
        if not load_file.endswith('.json'):
            load_file += '.json'
        if not new_file.endswith('.json'):
            new_file += '.json'
        self.in_f_1 = load_file
        self.out_f_2 = new_file
        self.in_main_1 = None
        self.out_main_1 = None

    def load_file(self):
        f_1 = open(self.in_f_1, 'r')
        self.in_main_1 = json.load(f_1)
        f_1.close()


    def main(self):
        if self.in_main_1 is None:
            return
        new_dict = {}
        for employee in self.in_main_1['employee']:
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
        self.out_main_1 = {'employee': new_dict}


    def get_out_main_1(self):
        if self.out_main_1 is None:
            if self.in_main_1 is None:
                self.load_file()
            self.main()
        return self.out_main_1


    def main_total(self):
        f_1 = open(self.out_f_2, 'w')
        json.dump(self.out_main_1, f_1)
        f_1.close()


    def main_del_func(self):
        self.in_main_1 = None
        self.out_main_1 = None


    def creating_input(self, name_of_file: str):
        if not name_of_file.endswith('.json'):
            name_of_file += '.json'
        self.in_f_1 = name_of_file




if __name__ == '__main__':
    func = NewClass(load_file='HW.json')
    func.load_file()
    func.main()
    func.main_total()
