a = float(input("Введите коэффициент а: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
d = b ** 2 - 4 * a * c
x1 = ((-b + d ** (1/2)) / (2 * a))
x2 = ((-b - d ** (1/2)) / (2 * a))
if a == 0:
    print('Уравнение не квадратное')
elif d <= 0:
    print('Нет корней уровнения')
elif x1 != x2:
    print('x1 =', x1, 'x2 =', x2)
elif x1 == x2:
    print('x =', x1)
