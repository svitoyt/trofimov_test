# Дан список стран и городов каждой страны. Затем дан cписок названия городов.
# Для каждого города укажите, в какой стране он находится.

countries = {}
total = int(input('Введите сколько всего стран: '))
for item in range(total):
    country, *cities = input('Страна и Города: ').split()
    for city in cities:
        countries[city] = country

for i in range(total):
    print(countries[input('Введите город для проверки: ')])
