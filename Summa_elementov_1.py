spisok_a = [int(item) for item in input('Введите данные: ').split()]
summa = 0
for item in spisok_a:
    summa += item
print(f'Сумма элементов списка: {summa}')
