spisok = [str(strk) for strk in input('Введите строки через пробел: ').split()]
simvol = str(input('Введите символ: '))
for strk in spisok:
    counter = strk.count(simvol)
    print(f"{strk} символ {simvol} встречается: {counter} раз")
