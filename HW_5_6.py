a = int(input("Введите значение стороны 1: "))
b = int(input("Введите значение стороны 2: "))
c = int(input("Введите значение стороны 3: "))
if (a + b < c) or (a + c < b) or (c + b < a):
    print("Треугольника не существует")
elif a == b == c:
    print("Треугольник - равносторонний")
elif a == b or a == c or b == c:
    print("Треугольник - равнобедренный")
elif a != b or a != c or b != c:
    print("Треугольник - разносторонний")
