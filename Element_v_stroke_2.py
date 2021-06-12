checklist = [str(word) for word in input('Введите строки через пробел: ').split()]
symbol = str(input('Введите символ: '))
for word in checklist:
    counter = word.count(symbol)
    print(f"{word} символ {symbol} встречается: {counter} раз")
