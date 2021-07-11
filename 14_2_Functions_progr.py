def home_work(num1, num2, num3):
    num1 = list(filter(lambda i: i % 2 == 0, num1))
    num3 = list(filter(lambda i: i % 2 == 0, num3))
    num2 = list(filter(lambda i: i % 2 != 0, num2))
    total_list = list(zip(num1, num2, num3))
    sum_list = list(map(lambda i: sum(i), total_list))
    odd_num = list(filter(lambda i: i % 2 != 0, sum_list))
    print('Список 1, чётные:', num1)
    print('Список 2, нечётные:', num2)
    print('Список 3, чётные:', num3)
    print('Список кортежей пар:', total_list)
    print('Список суммы значений в кортеже:', sum_list)
    print('Список нечётных значений в кортеже:', odd_num)


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
home_work(list_1, list_2, list_3)
