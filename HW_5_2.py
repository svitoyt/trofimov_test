a = int(input("Введите целочисленное значение 1: "))
b = int(input("Введите целочисленное значение 2: "))
c = int(input("Введите целочисленное значение 3: "))
if (a <= b) and (b <= c):
    print("Среднее число", b)
elif (a <= c) and (b >= c):
    print("Среднее число", c)
elif (b <= a) and (a <= c):
    print("Среднее число", a)
elif (b <= c) and (a >= c):
    print("Среднее число", c)
elif (c <= a) and (a <= b):
    print("Среднее число", a)
elif (c <= b) and (a >= b):
    print("Среднее число", b)
