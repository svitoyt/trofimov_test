x = int(input("Введите значение Х: "))
y = int(input("Введите значение Y: "))
if x > 0 and y > 0:
    print('I четверть')
elif x > 0 and y < 0:
    print('IV четверть')
elif x < 0 and y < 0:
    print('III четверть')
elif x < 0 and y > 0:
    print('II четверть')
else:
    print('Точка лежит на координатной оси')
