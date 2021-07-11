from _datetime import datetime


def time_of_function(function):
    def wrapper(n: int):
        start = datetime.now()
        result = function(n)
        print(datetime.now() - start)
    return wrapper


@time_of_function
def squar_n(n):
    dict_sq = {}
    final_list = []
    for j in range(n + 1):
        dict_sq = {i: i ** 2 for i in range(j + 1)}
        final_list.append(dict_sq)
    print(final_list)


squar_n(n=int(input("Введите число: ")))
