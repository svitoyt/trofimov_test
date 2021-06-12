#Для английского алфовита сгенерировать словарь-шифратор, то есть словарь,
# где ключ буква алфавита, а значение являются случайное значение.
# Используя словарь, зашифровать/расшифровать введенное сообщение.

alphabet = {}
alphabet['a'] = str(input('a = '))
alphabet['b'] = str(input('b = '))
alphabet['c'] = str(input('c = '))
alphabet['d'] = str(input('d = '))
alphabet['e'] = str(input('e = '))
alphabet['f'] = str(input('f = '))
alphabet['g'] = str(input('g = '))
alphabet['h'] = str(input('h = '))
alphabet['i'] = str(input('i = '))
alphabet['j'] = str(input('j = '))
alphabet['k'] = str(input('k = '))
alphabet['l'] = str(input('l = '))
alphabet['m'] = str(input('m = '))
alphabet['n'] = str(input('n = '))
alphabet['o'] = str(input('o = '))
alphabet['p'] = str(input('p = '))
alphabet['q'] = str(input('q = '))
alphabet['r'] = str(input('r = '))
alphabet['s'] = str(input('s = '))
alphabet['t'] = str(input('t = '))
alphabet['u'] = str(input('u = '))
alphabet['v'] = str(input('v = '))
alphabet['w'] = str(input('w = '))
alphabet['x'] = str(input('x = '))
alphabet['y'] = str(input('y = '))
alphabet['z'] = str(input('z = '))
password = [str(simbol) for simbol in input('Введите кодовую фразу: ').split()]
for simbol in password:
    for k, v in alphabet.items():
        if v == simbol:
            print(k, end='')
