import datetime

def time_of_function(function):
    def squar_n(n):
        start = datetime.now()
        result = function(**n)
        end = datetime.now()
        timer = (end - start)
        print(timer)
        return result
    return squar_n


@time_of_function
def squar_n(n):
    dict_sq = {}
    dict_fin = []
    for j in range(n + 1):
        dict_sq = {i: i ** 2 for i in range(j + 1)}
        dict_fin.append(dict_sq)
    print(dict_fin)


squar_n(n=int(input("Введите число: ")))

